#!/usr/bin/env python3
"""Fetch reservations-related endpoints and export them as CSV files."""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, MutableMapping, Sequence
import time

import requests
from dotenv import load_dotenv

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python < 3.9 is unsupported but guard for clarity
    ZoneInfo = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT / ".env"
CONFIG_PATH = ROOT / "config" / "reservations_endpoints.json"
DATE_RANGE_PATH = ROOT / "config" / "reservation_date_range.json"
OUTPUT_CONFIG_PATH = ROOT / "config" / "reservations_output.json"
DATA_DIR = ROOT / "data"
SWAGGER_PATH = ROOT / "API" / "swagger.json"
TIMEZONE = ZoneInfo("Asia/Tokyo") if ZoneInfo is not None else None
REQUEST_TIMEOUT = 30
RETRY_STATUSES = {429, 503, 504}
MAX_RETRIES = 3
RETRY_BACKOFF_SECONDS = 2
DEFAULT_OUTPUT_FORMATS: tuple[str, ...] = ("csv",)
GROUPED_EXPORTS: dict[str, tuple[str, ...]] = {
    "reservations": (
        "reservations",
        "reservation_meal_reservations",
    ),
    "sales": (
        "reservation_slip_reservations",
        "reservation_revenue",
    ),
    "rooms": (
        "reservation_rooms",
        "reservation_room_check_in",
    ),
}

ENSURE_COLUMNS_OVERRIDE: dict[str, tuple[str, ...]] = {
    "reservations": (
        "id",
        "reservation_number",
        "check_in_date",
        "check_out_date",
        "created",
        "created_at",
        "control_status",
        "last_modified",
        "person_count",
        "person_count_adult",
        "person_count_child_a",
        "person_count_child_b",
        "person_count_child_c",
        "person_count_child_d",
        "price",
        "reservationRoutes",
        "sales_package_name",
        "meal_name",
        "marketing_area",
        "agent_reservation_number",
        "name",
        "address",
        "phone_no",
        "gender",
        "birthday",
        "email",
        "customer_number",
    ),
    "reservation_rooms": (
        "reservation_number",
        "date",
        "room_number",
        "request_url",
    ),
    "reservation_room_check_in": (
        "reservation_number",
        "date",
        "room_number",
        "request_url",
    ),
    "reservation_slip_reservations": (
        "reservation_number",
        "date",
        "item",
        "total_price",
        "tax_include",
        "quantity",
        "request_url",
    ),
    "reservation_revenue": (
        "reservation_number",
        "date",
        "item",
        "total_price",
        "tax_include",
        "quantity",
        "request_url",
    ),
}

GROUPED_ALLOWED_COLUMNS: dict[str, tuple[str, ...]] = {
    "reservations": ENSURE_COLUMNS_OVERRIDE["reservations"],
    "rooms": ENSURE_COLUMNS_OVERRIDE["reservation_rooms"],
    "sales": ENSURE_COLUMNS_OVERRIDE["reservation_slip_reservations"],
}

@dataclass
class EndpointConfig:
    name: str
    path: str
    method: str = "GET"
    params: Mapping[str, str] = field(default_factory=dict)
    context_fields: Sequence[str] = field(default_factory=list)
    ensure_columns: Sequence[str] = field(default_factory=list)
    inherit_ensure_columns: bool = False
    children: Sequence["EndpointConfig"] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any]) -> "EndpointConfig":
        try:
            name = str(payload["name"]).strip()
            path = str(payload["path"]).strip()
        except KeyError as exc:
            raise ValueError(f"config is missing required key: {exc}") from exc
        if not name:
            raise ValueError("config entry has empty 'name'")
        if not path:
            raise ValueError("config entry has empty 'path'")

        method = str(payload.get("method", "GET")).upper()
        params = payload.get("params", {})
        if not isinstance(params, Mapping):
            raise ValueError(f"params for '{name}' must be an object")
        context_fields = payload.get("context_fields", [])
        if not isinstance(context_fields, Sequence) or isinstance(context_fields, (str, bytes, bytearray)):
            raise ValueError(f"context_fields for '{name}' must be an array of strings")
        context_fields = [str(field) for field in context_fields]

        ensure_columns = payload.get("ensure_columns", [])
        if not isinstance(ensure_columns, Sequence) or isinstance(ensure_columns, (str, bytes, bytearray)):
            raise ValueError(f"ensure_columns for '{name}' must be an array of strings")
        ensure_columns = [str(column) for column in ensure_columns]

        inherit_ensure_columns = payload.get("inherit_ensure_columns", False)
        if not isinstance(inherit_ensure_columns, bool):
            raise ValueError(f"inherit_ensure_columns for '{name}' must be a boolean")

        children_payload = payload.get("children", [])
        if not isinstance(children_payload, Sequence):
            raise ValueError(f"children for '{name}' must be an array")
        children = [cls.from_mapping(item) for item in children_payload]

        return cls(
            name=name,
            path=path,
            method=method,
            params=params,  # type: ignore[arg-type]
            context_fields=context_fields,
            ensure_columns=ensure_columns,
            inherit_ensure_columns=inherit_ensure_columns,
            children=children,
        )


def _load_env() -> None:
    if not ENV_PATH.exists():
        print(f".env が見つかりません: {ENV_PATH}", file=sys.stderr)
        sys.exit(1)
    load_dotenv(ENV_PATH)


def _load_config(path: Path) -> list[EndpointConfig]:
    if not path.exists():
        print(f"設定ファイルが見つかりません: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"設定ファイルの JSON 解析に失敗しました: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(payload, Sequence):
        print("設定ファイルのルート要素は配列である必要があります。", file=sys.stderr)
        sys.exit(1)
    try:
        configs = [EndpointConfig.from_mapping(item) for item in payload]
    except ValueError as exc:
        print(f"設定ファイルの形式が不正です: {exc}", file=sys.stderr)
        sys.exit(1)
    return configs


def _load_output_formats(path: Path) -> tuple[str, ...]:
    if not path.exists():
        return DEFAULT_OUTPUT_FORMATS

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"出力設定ファイルの JSON 解析に失敗しました: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(payload, Mapping):
        print("出力設定ファイルのルート要素はオブジェクトである必要があります。", file=sys.stderr)
        sys.exit(1)

    formats = payload.get("formats", DEFAULT_OUTPUT_FORMATS)
    if not isinstance(formats, Sequence) or isinstance(formats, (str, bytes, bytearray)):
        print("formats は配列で指定してください。例: [\"csv\", \"json\"]", file=sys.stderr)
        sys.exit(1)

    allowed = {"csv", "json"}
    cleaned: list[str] = []
    for fmt in formats:
        fmt_str = str(fmt).lower().strip()
        if not fmt_str:
            continue
        if fmt_str not in allowed:
            print(f"未知の出力形式が指定されています: {fmt}", file=sys.stderr)
            sys.exit(1)
        if fmt_str not in cleaned:
            cleaned.append(fmt_str)

    if not cleaned:
        cleaned = list(DEFAULT_OUTPUT_FORMATS)
    return tuple(cleaned)


def _apply_inherited_ensure_columns(
    endpoints: Sequence[EndpointConfig],
    parent_required: Sequence[str] | None = None,
) -> None:
    parent_required = tuple(parent_required or [])
    for endpoint in endpoints:
        effective_required: Sequence[str]
        if endpoint.inherit_ensure_columns:
            endpoint.ensure_columns = tuple(parent_required)
            effective_required = endpoint.ensure_columns
        else:
            effective_required = endpoint.ensure_columns or parent_required
        _apply_inherited_ensure_columns(endpoint.children, effective_required)


def _load_swagger(path: Path) -> Mapping[str, Any] | None:
    if not path.exists():
        print(f"(warn) Swagger ファイルが見つかりません: {path}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"(warn) Swagger ファイルの JSON 解析に失敗しました: {exc}")
    return None


def _resolve_ref(spec: Mapping[str, Any], ref: str) -> Mapping[str, Any]:
    _, _, path = ref.partition("#/")
    target: Mapping[str, Any] = spec
    for segment in path.split("/"):
        target = target[segment]
    if "$ref" in target:
        return _resolve_ref(spec, target["$ref"])
    return target


def _collect_schema_properties(
    spec: Mapping[str, Any], schema: Mapping[str, Any], prefix: str = ""
) -> set[str]:
    resolved = _resolve_ref(spec, schema["$ref"]) if "$ref" in schema else schema
    properties: set[str] = set()

    if "allOf" in resolved:
        for part in resolved["allOf"]:
            properties.update(_collect_schema_properties(spec, part, prefix))
        return properties

    schema_type = resolved.get("type")
    if schema_type == "object":
        for key, value in resolved.get("properties", {}).items():
            next_prefix = f"{prefix}.{key}" if prefix else str(key)
            properties.add(next_prefix)
            properties.update(_collect_schema_properties(spec, value, next_prefix))
    elif schema_type == "array":
        properties.update(_collect_schema_properties(spec, resolved.get("items", {}), prefix))
    return properties


def _simplify_columns(columns: Sequence[str]) -> list[str]:
    simplified: list[str] = []
    seen: set[str] = set()
    counters: dict[str, int] = defaultdict(int)

    for column in columns:
        base = _simplify_column_name(column)
        counters[base] += 1
        suffix = counters[base]
        name = base if suffix == 1 else f"{base}_{suffix}"
        while name in seen:
            suffix += 1
            counters[base] = suffix
            name = f"{base}_{suffix}"
        seen.add(name)
        simplified.append(name)

    return simplified


def _schema_columns_for_endpoint(
    spec: Mapping[str, Any], endpoint: EndpointConfig, *, base_prefix: str = "/hotels/{hotel_id}/"
) -> Sequence[str] | None:
    relative_path = endpoint.path.lstrip("/")
    swagger_path = f"{base_prefix}{relative_path}"

    path_item = spec.get("paths", {}).get(swagger_path)
    if not isinstance(path_item, Mapping):
        return None

    operation = path_item.get(endpoint.method.lower())
    if not isinstance(operation, Mapping):
        return None

    responses = operation.get("responses", {})
    ok_response = responses.get("200")
    if not isinstance(ok_response, Mapping):
        return None

    content = ok_response.get("content", {})
    json_schema = None
    if isinstance(content, Mapping):
        app_json = content.get("application/json")
        if isinstance(app_json, Mapping):
            json_schema = app_json.get("schema")

    if not isinstance(json_schema, Mapping):
        return None

    properties = _collect_schema_properties(spec, json_schema)
    if not properties:
        return None
    simplified = _simplify_columns(sorted(properties))
    return tuple(simplified)


def _apply_schema_columns(
    endpoints: Sequence[EndpointConfig],
    spec: Mapping[str, Any],
    *,
    parent_required: Sequence[str] | None = None,
) -> None:
    parent_required = tuple(parent_required or [])
    for endpoint in endpoints:
        schema_columns = _schema_columns_for_endpoint(spec, endpoint)
        if endpoint.ensure_columns:
            effective_required = tuple(endpoint.ensure_columns)
        elif endpoint.inherit_ensure_columns and parent_required:
            endpoint.ensure_columns = tuple(parent_required)
            effective_required = endpoint.ensure_columns
        elif schema_columns:
            endpoint.ensure_columns = schema_columns
            effective_required = endpoint.ensure_columns
        else:
            effective_required = parent_required
        _apply_schema_columns(endpoint.children, spec, parent_required=effective_required)


def _default_reservation_range() -> tuple[date, date]:
    if TIMEZONE is not None:
        now = datetime.now(TIMEZONE)
    else:
        now = datetime.now()
    default_date = (now - timedelta(days=1)).date()
    return default_date, default_date


def _parse_iso_date(candidate: str, *, label: str) -> date:
    try:
        return datetime.strptime(candidate, "%Y-%m-%d").date()
    except ValueError as exc:
        print(f"{label} の形式が不正です (YYYY-MM-DD): {exc}", file=sys.stderr)
        sys.exit(1)


def _load_date_range_from_file(path: Path) -> tuple[date, date]:
    if not path.exists():
        return _default_reservation_range()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"予約日ファイルの JSON 解析に失敗しました: {exc}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(payload, Mapping):
        print("予約日ファイルの形式が不正です。オブジェクト形式で 'from' と 'to' を指定してください。", file=sys.stderr)
        sys.exit(1)

    start_raw = payload.get("from") or payload.get("start") or payload.get("reservation_date_from")
    end_raw = payload.get("to") or payload.get("end") or payload.get("reservation_date_to")
    if start_raw is None and end_raw is None:
        return _default_reservation_range()
    if start_raw is None or end_raw is None:
        print("予約日ファイルには 'from' と 'to' の両方を指定してください。", file=sys.stderr)
        sys.exit(1)

    start = _parse_iso_date(str(start_raw), label="from")
    end = _parse_iso_date(str(end_raw), label="to")
    return start, end


def _resolve_reservation_range(
    *,
    single_day: str | None,
    from_date: str | None,
    to_date: str | None,
    file_path: Path,
) -> tuple[str, str]:
    if single_day:
        start = end = _parse_iso_date(single_day, label="--date")
    elif from_date or to_date:
        if not from_date or not to_date:
            print("--from-date と --to-date はセットで指定してください。", file=sys.stderr)
            sys.exit(1)
        start = _parse_iso_date(from_date, label="--from-date")
        end = _parse_iso_date(to_date, label="--to-date")
    else:
        start, end = _load_date_range_from_file(file_path)

    if start > end:
        print("予約日の範囲が不正です。from は to 以前の日付を指定してください。", file=sys.stderr)
        sys.exit(1)

    return start.isoformat(), end.isoformat()


def _build_headers(api_key: str) -> dict[str, str]:
    return {
        "Accept": "application/json",
        "X-API-Key": api_key,
    }


def _build_url(api_base: str, hotel_code: str, path: str) -> str:
    suffix = path.lstrip("/")
    return f"{api_base.rstrip('/')}/hotels/{hotel_code}/{suffix}"


def _format_template(template: str, context: Mapping[str, Any], *, name: str) -> str | None:
    try:
        return template.format(**context)
    except KeyError as exc:
        print(
            f"(警告) {name} の生成に必要なコンテキスト {exc} が不足しているためスキップします。",
            file=sys.stderr,
        )
        return None


def _is_scalar(value: Any) -> bool:
    return isinstance(value, (str, int, float, bool)) or value is None


def _coerce_records(payload: Any) -> list[MutableMapping[str, Any]]:
    def _find_candidate_list(obj: Any) -> list[Any] | None:
        if isinstance(obj, list):
            return obj
        if isinstance(obj, Mapping):
            for key in ("data", "items", "results", "rows", "body"):
                nested = _find_candidate_list(obj.get(key))  # type: ignore[index]
                if nested is not None:
                    return nested
            for value in obj.values():
                nested = _find_candidate_list(value)
                if nested is not None:
                    return nested
        return None

    candidates = _find_candidate_list(payload)
    if candidates is None:
        if isinstance(payload, Mapping):
            candidates = [payload]
        else:
            return []

    records: list[MutableMapping[str, Any]] = []
    for index, item in enumerate(candidates):
        if isinstance(item, MutableMapping):
            records.append(dict(item))
        elif isinstance(item, Mapping):
            records.append(dict(item))
        else:
            records.append({"value": item})
            print(
                f"(注) {index} 番目の要素がオブジェクトではなかったため 'value' 列に変換しました。",
                file=sys.stderr,
            )
    return records


def _stringify_address(address: Mapping[str, Any]) -> str | None:
    parts: list[str] = []
    postal_code = address.get("postal_code")
    if postal_code:
        parts.append(str(postal_code))
    prefecture = address.get("prefecture_code")
    if prefecture:
        parts.append(str(prefecture))
    city = address.get("city")
    if city:
        parts.append(str(city))
    lines = address.get("address_line")
    if isinstance(lines, Sequence) and not isinstance(lines, (str, bytes, bytearray)):
        parts.extend(str(item) for item in lines if item)
    address_text = " ".join(part for part in parts if part).strip()
    return address_text or None


def _normalise_person_count(raw: Any) -> int | None:
    if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes, bytearray)):
        total = 0
        found = False
        for item in raw:
            if isinstance(item, (int, float)):
                total += int(item)
                found = True
                continue
            try:
                total += int(str(item))
            except (TypeError, ValueError):
                continue
            else:
                found = True
        return total if found else None
    if isinstance(raw, (int, float)):
        return int(raw)
    try:
        return int(str(raw))
    except (TypeError, ValueError):
        return None


def _extract_person_counts(raw: Any) -> dict[str, int]:
    if not isinstance(raw, Sequence) or isinstance(raw, (str, bytes, bytearray)):
        total = _normalise_person_count(raw)
        return {"person_count": total or 0}

    labels = ["person_count_adult"]
    labels.extend(
        [f"person_count_child_{chr(ord('a') + index)}" for index in range(10)]
    )

    counts: dict[str, int] = {}
    total = 0
    for index, value in enumerate(raw):
        normalised = _normalise_person_count(value)
        if normalised is None:
            continue
        total += normalised
        if index < len(labels):
            counts[labels[index]] = normalised
    counts["person_count"] = total
    return counts


def _summarise_reservation_routes(record: Mapping[str, Any]) -> str | None:
    reservation_route = record.get("reservation_route")
    if not isinstance(reservation_route, Mapping):
        return None
    routes = reservation_route.get("reservationRoutes")
    if not isinstance(routes, Sequence):
        return None
    names: list[str] = []
    for route in routes:
        if isinstance(route, Mapping):
            name = route.get("name") or route.get("short_name") or route.get("code")
            if name:
                names.append(str(name))
    return " > ".join(names) if names else None


def _summarise_price(record: Mapping[str, Any]) -> int | None:
    if "price" in record and _normalise_person_count(record.get("price")) is not None:
        price = _normalise_person_count(record.get("price"))
        return int(price) if price is not None else None

    price_changes = record.get("price_changes")
    if not isinstance(price_changes, Sequence):
        return None

    total_price = 0
    found = False
    for change in price_changes:
        if not isinstance(change, Mapping):
            continue
        prices = change.get("prices")
        if not isinstance(prices, Sequence):
            continue
        for price_entry in prices:
            if not isinstance(price_entry, Mapping):
                continue
            price_value = _normalise_person_count(price_entry.get("price"))
            if price_value is None:
                continue
            found = True
            total_price += int(price_value)

    return total_price if found else None


def _extract_reservation_id(record: Mapping[str, Any]) -> Any:
    """Return the reservation id, tolerating stray whitespace in keys."""

    for key, value in record.items():
        if str(key).strip().lower() == "id" and value:
            return value

    return record.get("reservation_id") or record.get("reservation_number")


def _enrich_reservation_record(
    record: MutableMapping[str, Any],
    required_fields: Sequence[str],
) -> None:
    required = set(required_fields)

    reservation_id = _extract_reservation_id(record)
    if reservation_id:
        record["id"] = reservation_id
        record["reservation_id"] = reservation_id

    if "check_in_date" in required and "check_in_date" not in record:
        stay_period = record.get("stay_period")
        if isinstance(stay_period, Mapping):
            check_in = stay_period.get("check_in") or stay_period.get("from")
            if check_in:
                record["check_in_date"] = check_in

    if "created_at" in required and "created_at" not in record and "created" in record:
        record["created_at"] = record["created"]

    if "control_status" in required:
        control_status = record.get("control_status")
        status_value = None
        if isinstance(control_status, Mapping):
            status_value = control_status.get("status")
        elif _is_scalar(control_status):
            status_value = control_status

        record["control_status"] = status_value if status_value is not None else ""

    if "last_modified" in required and "last_modified" in record and not _is_scalar(record["last_modified"]):
        last_modified = record["last_modified"]
        if isinstance(last_modified, Mapping):
            timestamp = last_modified.get("timestamp") or last_modified.get("value")
            if timestamp:
                record["last_modified"] = timestamp

    if "person_count" in required:
        raw_person_count = record.get("person_count")
        counts = _extract_person_counts(raw_person_count)
        record.update(counts)

    if "price" in required:
        price = _summarise_price(record)
        if price is not None:
            record["price"] = price

    if "reservationRoutes" in required:
        routes = _summarise_reservation_routes(record)
        if routes:
            record["reservationRoutes"] = routes

    pricing = record.get("pricing") if isinstance(record.get("pricing"), Mapping) else {}
    if "sales_package_name" in required and isinstance(pricing, Mapping):
        sales_package = pricing.get("sales_package")
        if isinstance(sales_package, Mapping):
            name = sales_package.get("name")
            if name:
                record["sales_package_name"] = name

    if "meal_name" in required and isinstance(pricing, Mapping):
        meal = pricing.get("meal")
        if isinstance(meal, Mapping):
            meal_name = meal.get("name")
            if meal_name:
                record["meal_name"] = meal_name

    if "marketing_area" in required and "marketing_area" not in record:
        marketing_area = record.get("marketing_area")
        if marketing_area:
            record["marketing_area"] = marketing_area

    contact_required = {
        field
        for field in (
            "name",
            "address",
            "phone_no",
            "email",
            "customer_number",
            "gender",
            "birthday",
        )
        if field in required
    }
    contact_source: Mapping[str, Any] | None = None
    if contact_required:
        main_guest = record.get("main_guest")
        if isinstance(main_guest, Mapping):
            guest_person = main_guest.get("person")
            if isinstance(guest_person, Mapping):
                contact_source = guest_person
            if "customer_number" in contact_required and "customer_number" not in record:
                customer_number = main_guest.get("customer_number")
                if customer_number:
                    record["customer_number"] = customer_number

        if contact_source is None:
            reserved_by = record.get("reserved_by")
            if isinstance(reserved_by, Mapping):
                reserved_person = reserved_by.get("person")
                if isinstance(reserved_person, Mapping):
                    contact_source = reserved_person
                if "customer_number" in contact_required and "customer_number" not in record:
                    customer_number = reserved_by.get("customer_number")
                    if customer_number:
                        record["customer_number"] = customer_number

    if contact_source is not None:
        if "name" in required and "name" not in record:
            name = contact_source.get("name") or contact_source.get("kana_name")
            if name:
                record["name"] = name

        if "address" in required and "address" not in record and isinstance(contact_source.get("address"), Mapping):
            formatted_address = _stringify_address(contact_source["address"])
            if formatted_address:
                record["address"] = formatted_address

        if "phone_no" in required and "phone_no" not in record:
            phone = (
                contact_source.get("phone_no")
                or contact_source.get("phone_no_mobile")
                or contact_source.get("phone_no_other")
            )
            if phone:
                record["phone_no"] = phone

        if "email" in required and "email" not in record:
            email = contact_source.get("email") or contact_source.get("email_sub")
            if email:
                record["email"] = email

        if "gender" in required and "gender" not in record and contact_source.get("gender"):
            record["gender"] = contact_source.get("gender")

        if "birthday" in required and "birthday" not in record and contact_source.get("birthday"):
            record["birthday"] = contact_source.get("birthday")

    for key in required:
        record.setdefault(key, "")


def _enrich_room_record(record: MutableMapping[str, Any], required_fields: Sequence[str]) -> None:
    if "reservation_number" in required_fields and "reservation_number" not in record:
        reservation_number = record.get("reservation_number")
        if reservation_number:
            record["reservation_number"] = reservation_number

    if "date" in required_fields and "date" not in record:
        stay_period = record.get("stay_period")
        if isinstance(stay_period, Mapping):
            arrival = stay_period.get("arrival_date") or stay_period.get("check_in_date")
            if arrival:
                record["date"] = arrival

    if "room_number" in required_fields and "room_number" not in record:
        room_number = record.get("room_number") or record.get("room_code")
        if not room_number and isinstance(record.get("room_type"), Mapping):
            room_number = record["room_type"].get("code")
        if room_number:
            record["room_number"] = room_number

    for key in required_fields:
        record.setdefault(key, "")


def _enrich_sales_record(record: MutableMapping[str, Any], required_fields: Sequence[str]) -> None:
    if "reservation_number" in required_fields and "reservation_number" not in record:
        reservation_number = record.get("reservation_number")
        if reservation_number:
            record["reservation_number"] = reservation_number

    if "date" in required_fields and "date" not in record:
        date_value = record.get("date") or record.get("stay_date")
        if date_value:
            record["date"] = date_value

    if "item" in required_fields and "item" not in record:
        item = record.get("item") or record.get("name") or record.get("description")
        if item:
            record["item"] = item

    if "total_price" in required_fields and "total_price" not in record:
        price = record.get("total_price") or record.get("price") or record.get("amount")
        if price is None:
            price = _summarise_price(record)
        if price is not None:
            record["total_price"] = price

    if "tax_include" in required_fields and "tax_include" not in record:
        tax_include = record.get("tax_include") or record.get("tax_included")
        if isinstance(tax_include, bool):
            record["tax_include"] = tax_include
        elif tax_include is not None:
            record["tax_include"] = tax_include

    if "quantity" in required_fields and "quantity" not in record:
        quantity = record.get("quantity") or record.get("count")
        if quantity is not None:
            record["quantity"] = quantity

    for key in required_fields:
        record.setdefault(key, "")


def _enrich_record_for_endpoint(
    endpoint_name: str,
    record: MutableMapping[str, Any],
    required_fields: Sequence[str],
) -> None:
    if endpoint_name == "reservations":
        _enrich_reservation_record(record, required_fields)
    elif endpoint_name in {"reservation_rooms", "reservation_room_check_in"}:
        _enrich_room_record(record, required_fields)
    elif endpoint_name in {"reservation_slip_reservations", "reservation_revenue"}:
        _enrich_sales_record(record, required_fields)
    elif required_fields:
        for key in required_fields:
            record.setdefault(key, "")


def _resolve_required_fields(endpoint: EndpointConfig) -> Sequence[str]:
    return tuple(ENSURE_COLUMNS_OVERRIDE.get(endpoint.name, endpoint.ensure_columns))


def _resolve_column_order(
    *,
    endpoint: EndpointConfig,
    normalised_records: Sequence[Mapping[str, str]],
) -> list[str]:
    columns: list[str]
    enforced = ENSURE_COLUMNS_OVERRIDE.get(endpoint.name, endpoint.ensure_columns)
    if enforced:
        columns = list(dict.fromkeys(enforced))
    else:
        columns = _collect_columns(normalised_records)

    allowed_set = set(columns)
    extras = [
        extra
        for extra in dict.fromkeys(endpoint.context_fields)
        if extra in allowed_set or not allowed_set
    ]
    for extra in extras:
        if extra not in columns:
            columns.append(extra)

    if not columns:
        columns = ["value"]
    return columns

def _augment_record(
    record: MutableMapping[str, Any],
    context_fields: Sequence[str],
    context: Mapping[str, Any],
) -> MutableMapping[str, Any]:
    augmented = dict(record)
    for field in context_fields:
        if field in context and field not in augmented:
            augmented[field] = context[field]
    return augmented


def _build_child_context(
    parent_context: Mapping[str, Any],
    record: Mapping[str, Any],
    additional_fields: Sequence[str],
) -> dict[str, Any]:
    child_context = dict(parent_context)
    for key, value in record.items():
        if _is_scalar(value):
            child_context[key] = value
    for key in additional_fields:
        if key in parent_context:
            child_context[key] = parent_context[key]
    return child_context


def _simplify_column_name(prefix: str) -> str:
    if not prefix:
        return "value"
    tail = prefix.split(".")[-1]
    simplified = re.sub(r"\[\d+\]", "", tail)
    return simplified or "value"


def _next_available_column(name: str, existing: MutableMapping[str, str]) -> str:
    if name not in existing:
        return name
    suffix = 2
    while True:
        candidate = f"{name}_{suffix}"
        if candidate not in existing:
            return candidate
        suffix += 1


def _flatten_value(value: Any, prefix: str, flattened: MutableMapping[str, str]) -> None:
    if isinstance(value, Mapping):
        if not value:
            target = _next_available_column(_simplify_column_name(prefix), flattened)
            flattened[target] = ""
        else:
            for key, nested in value.items():
                next_prefix = f"{prefix}.{key}" if prefix else str(key)
                _flatten_value(nested, next_prefix, flattened)
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        if not value:
            target = _next_available_column(_simplify_column_name(prefix), flattened)
            flattened[target] = ""
        else:
            first_item = next(iter(value))
            base = prefix or "value"
            _flatten_value(first_item, base, flattened)
        return
    target = _next_available_column(_simplify_column_name(prefix), flattened)
    flattened[target] = _serialise_value(value)


def _normalise_records(records: Sequence[Mapping[str, Any]]) -> list[dict[str, str]]:
    normalised: list[dict[str, str]] = []
    for record in records:
        flattened: dict[str, str] = {}
        for key, value in record.items():
            _flatten_value(value, str(key), flattened)
        if not flattened:
            flattened["value"] = ""
        normalised.append(flattened)
    return normalised


def _collect_columns(records: Sequence[Mapping[str, str]]) -> list[str]:
    columns: set[str] = set()
    for record in records:
        columns.update(record.keys())
    ordered = sorted(columns)
    if not ordered:
        ordered = ["value"]
    return ordered


def _serialise_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def _collect_grouped_fields(
    endpoint_names: Sequence[str],
    endpoint_index: Mapping[str, EndpointConfig],
) -> tuple[list[str], list[str]]:
    ensure_columns: list[str] = []
    context_fields: list[str] = []

    for endpoint_name in endpoint_names:
        endpoint = endpoint_index.get(endpoint_name)
        if not endpoint:
            continue
        ensure_columns.extend(endpoint.ensure_columns)
        context_fields.extend(endpoint.context_fields)

    ensure_columns = list(dict.fromkeys(ensure_columns))
    context_fields = list(dict.fromkeys(context_fields))
    return ensure_columns, context_fields


def _collect_grouped_records(
    endpoint_names: Sequence[str],
    aggregated: Mapping[str, Sequence[Mapping[str, Any]]],
) -> list[Mapping[str, Any]]:
    grouped_records: list[Mapping[str, Any]] = []
    for endpoint_name in endpoint_names:
        for record in aggregated.get(endpoint_name, []):
            merged = dict(record)
            merged.setdefault("source_endpoint", endpoint_name)
            grouped_records.append(merged)
    return grouped_records


def _build_grouped_endpoint(
    name: str,
    endpoint_names: Sequence[str],
    endpoint_index: Mapping[str, EndpointConfig],
) -> EndpointConfig:
    ensure_columns, context_fields = _collect_grouped_fields(endpoint_names, endpoint_index)
    allowed_columns = GROUPED_ALLOWED_COLUMNS.get(name)
    if allowed_columns:
        ensure_columns = list(allowed_columns)
        context_fields = [field for field in context_fields if field in allowed_columns]
    if "source_endpoint" not in context_fields:
        context_fields.append("source_endpoint")

    grouped_endpoint = EndpointConfig(
        name=name,
        path=f"grouped:{name}",
        ensure_columns=ensure_columns,
        context_fields=context_fields,
    )
    return grouped_endpoint


def _write_grouped_csv(
    endpoint: EndpointConfig,
    records: Sequence[Mapping[str, Any]],
    timestamp: str,
) -> Path:
    return _write_csv(endpoint, records, timestamp)


def _write_grouped_json(
    endpoint: EndpointConfig,
    records: Sequence[Mapping[str, Any]],
    timestamp: str,
) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    json_path = DATA_DIR / f"{timestamp}_{endpoint.name}.json"

    with json_path.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)
    return json_path


def _write_csv(
    endpoint: EndpointConfig,
    records: Sequence[Mapping[str, Any]],
    timestamp: str,
) -> Path:
    name = endpoint.name
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = DATA_DIR / f"{timestamp}_{name}.csv"

    if records:
        normalised = _normalise_records(records)
    else:
        normalised = []
    columns = _resolve_column_order(endpoint=endpoint, normalised_records=normalised)

    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in normalised:
            writer.writerow({column: record.get(column, "") for column in columns})
    return csv_path


def _request_json(
    session: requests.Session,
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    params: Mapping[str, Any] | None,
) -> tuple[requests.Response | None, str | None]:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.request(
                method,
                url,
                headers=headers,
                params=params,
                timeout=REQUEST_TIMEOUT,
            )
        except requests.RequestException as exc:
            return None, f"HTTP リクエストに失敗しました: {exc}"

        if response.status_code == 204:
            return None, None

        if response.status_code in RETRY_STATUSES:
            if attempt < MAX_RETRIES:
                wait_seconds = RETRY_BACKOFF_SECONDS * attempt
                time.sleep(wait_seconds)
                continue
            return None, f"HTTP {response.status_code} が続いたため中断しました"

        if not response.ok:
            return None, f"HTTP エラー: {response.status_code} {response.text[:200]}"
        return response, None

    return None, f"HTTP エラーが繰り返されたため中断しました"


def _gather_endpoints(endpoints: Sequence[EndpointConfig]) -> dict[str, EndpointConfig]:
    result: dict[str, EndpointConfig] = {}
    for endpoint in endpoints:
        if endpoint.name in result:
            raise ValueError(f"duplicate endpoint name detected: {endpoint.name}")
        result[endpoint.name] = endpoint
        child_map = _gather_endpoints(endpoint.children)
        for key, value in child_map.items():
            if key in result:
                raise ValueError(f"duplicate endpoint name detected: {key}")
            result[key] = value
    return result


def _process_endpoint(
    endpoint: EndpointConfig,
    *,
    api_base: str,
    hotel_code: str,
    headers: Mapping[str, str],
    session: requests.Session,
    context: Mapping[str, Any],
    aggregated: dict[str, list[MutableMapping[str, Any]]],
    errors: list[str],
) -> None:
    formatted_path = _format_template(endpoint.path, context, name=endpoint.name)
    if not formatted_path:
        return
    url = _build_url(api_base, hotel_code, formatted_path)

    request_url: str | None = None
    if endpoint.name != "reservations":
        request_url = url

    params: dict[str, Any] | None = None
    if endpoint.params:
        params = {}
        for key, template in endpoint.params.items():
            rendered = _format_template(str(template), context, name=f"{endpoint.name}:{key}")
            if rendered is None:
                continue
            params[key] = rendered
        if not params:
            params = None

    response, error = _request_json(session, endpoint.method, url, headers=headers, params=params)
    if error:
        errors.append(f"{endpoint.name}: {error}")
    if response is None:
        return

    try:
        payload = response.json()
    except ValueError as exc:
        errors.append(f"{endpoint.name}: JSON 解析に失敗しました ({exc})")
        return

    records = _coerce_records(payload)
    augmented: list[MutableMapping[str, Any]] = []
    for record in records:
        if request_url is not None and "request_url" not in record:
            record = dict(record)
            record["request_url"] = request_url

        enriched = _augment_record(record, endpoint.context_fields, context)
        required_fields = _resolve_required_fields(endpoint)
        _enrich_record_for_endpoint(endpoint.name, enriched, required_fields)
        augmented.append(enriched)

    aggregated[endpoint.name].extend(augmented)

    for record in augmented:
        child_context = _build_child_context(context, record, endpoint.context_fields)
        for child in endpoint.children:
            _process_endpoint(
                child,
                api_base=api_base,
                hotel_code=hotel_code,
                headers=headers,
                session=session,
                context=child_context,
                aggregated=aggregated,
                errors=errors,
            )


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default=str(CONFIG_PATH),
        help="JSON ファイルで定義されたエンドポイント設定へのパス (デフォルト: %(default)s)",
    )
    parser.add_argument(
        "--date",
        help="予約日 (YYYY-MM-DD)。指定すると from/to の両方に同じ日付を利用",
    )
    parser.add_argument(
        "--from-date",
        help="予約日の開始日 (YYYY-MM-DD)。--to-date とセットで使用",
    )
    parser.add_argument(
        "--to-date",
        help="予約日の終了日 (YYYY-MM-DD)。--from-date とセットで使用",
    )
    parser.add_argument(
        "--date-range-file",
        default=str(DATE_RANGE_PATH),
        help=(
            "予約日の範囲を JSON 形式で記述したファイルパス"
            " (デフォルト: %(default)s)。--date または --from-date/--to-date が未指定の場合に使用"
        ),
    )
    parser.add_argument(
        "--swagger",
        default=str(SWAGGER_PATH),
        help="全カラムを取得するために参照する Swagger (OpenAPI) JSON のパス (デフォルト: %(default)s)",
    )
    parser.add_argument(
        "--output-config",
        default=str(OUTPUT_CONFIG_PATH),
        help=(
            "出力形式を指定する JSON ファイルへのパス (デフォルト: %(default)s)。"
            "未指定またはファイルが存在しない場合は CSV のみ出力"
        ),
    )
    args = parser.parse_args(argv)

    _load_env()
    configs = _load_config(Path(args.config))
    swagger_spec = _load_swagger(Path(args.swagger))
    if swagger_spec:
        _apply_schema_columns(configs, swagger_spec)
    else:
        _apply_inherited_ensure_columns(configs)

    try:
        endpoint_index = _gather_endpoints(configs)
    except ValueError as exc:
        print(f"設定ファイルに問題があります: {exc}", file=sys.stderr)
        sys.exit(1)

    api_base = os.getenv("API_BASE")
    hotel_code = os.getenv("HOTEL_CODE")
    api_key = os.getenv("TAP_API_KEY")
    missing = [
        name
        for name, value in {
            "API_BASE": api_base,
            "HOTEL_CODE": hotel_code,
            "TAP_API_KEY": api_key,
        }.items()
        if not value
    ]
    if missing:
        print(f"未設定の環境変数があります: {', '.join(missing)}", file=sys.stderr)
        sys.exit(2)

    reservation_date_from, reservation_date_to = _resolve_reservation_range(
        single_day=args.date,
        from_date=args.from_date,
        to_date=args.to_date,
        file_path=Path(args.date_range_file),
    )

    print(
        "(info) 取得を開始します:",
        f"{reservation_date_from} -> {reservation_date_to}",
    )

    base_context: dict[str, Any] = {
        "hotel_id": hotel_code,
        "reservation_date_from": reservation_date_from,
        "reservation_date_to": reservation_date_to,
    }
    if reservation_date_from == reservation_date_to:
        base_context["reservation_date"] = reservation_date_from

    aggregated: dict[str, list[MutableMapping[str, Any]]] = defaultdict(list)
    errors: list[str] = []

    session = requests.Session()
    headers = _build_headers(api_key)

    for endpoint in configs:
        _process_endpoint(
            endpoint,
            api_base=api_base,
            hotel_code=hotel_code,
            headers=headers,
            session=session,
            context=base_context,
            aggregated=aggregated,
            errors=errors,
        )

    output_formats = _load_output_formats(Path(args.output_config))
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    grouped_datasets: list[tuple[EndpointConfig, list[Mapping[str, Any]]]] = []
    for grouped_name, endpoint_names in GROUPED_EXPORTS.items():
        grouped_endpoint = _build_grouped_endpoint(
            grouped_name,
            endpoint_names,
            endpoint_index,
        )
        grouped_records = _collect_grouped_records(endpoint_names, aggregated)
        grouped_datasets.append((grouped_endpoint, grouped_records))

    output_paths: list[Path] = []
    for fmt in output_formats:
        for grouped_endpoint, grouped_records in grouped_datasets:
            if fmt == "json":
                output_paths.append(
                    _write_grouped_json(
                        grouped_endpoint,
                        grouped_records,
                        timestamp,
                    )
                )
            else:
                output_paths.append(
                    _write_grouped_csv(
                        grouped_endpoint,
                        grouped_records,
                        timestamp,
                    )
                )
    joined_paths = ", ".join(str(path) for path in output_paths)
    if errors:
        joined_errors = "; ".join(errors)
        print(f"(warn) 一部の取得に失敗しました: {joined_errors}", file=sys.stderr)
    print(f"(info) 取得と保存が完了しました。出力: {joined_paths}")


if __name__ == "__main__":
    main()
