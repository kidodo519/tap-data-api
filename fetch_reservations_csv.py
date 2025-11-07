#!/usr/bin/env python3
"""Fetch reservations-related endpoints and export them as CSV files."""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Mapping, MutableMapping, Sequence

import requests
from dotenv import load_dotenv

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover - Python < 3.9 is unsupported but guard for clarity
    ZoneInfo = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT / ".env"
CONFIG_PATH = ROOT / "config" / "reservations_endpoints.json"
DATA_DIR = ROOT / "data"
TIMEZONE = ZoneInfo("Asia/Tokyo") if ZoneInfo is not None else None
REQUEST_TIMEOUT = 30


@dataclass
class EndpointConfig:
    name: str
    path: str
    method: str = "GET"
    params: Mapping[str, str] = field(default_factory=dict)
    context_fields: Sequence[str] = field(default_factory=list)
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


def _determine_reservation_date(arg_value: str | None) -> str:
    if arg_value:
        try:
            parsed = datetime.strptime(arg_value, "%Y-%m-%d").date()
        except ValueError as exc:
            print(f"--date の形式が不正です (YYYY-MM-DD): {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        if TIMEZONE is not None:
            now = datetime.now(TIMEZONE)
        else:
            now = datetime.now()
        parsed = (now - timedelta(days=1)).date()
    return parsed.isoformat()


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
    if isinstance(payload, list):
        candidates = payload
    elif isinstance(payload, Mapping):
        for key in ("data", "items", "results", "rows"):
            value = payload.get(key)  # type: ignore[index]
            if isinstance(value, list):
                candidates = value
                break
        else:
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


def _flatten_value(value: Any, prefix: str, flattened: MutableMapping[str, str]) -> None:
    if isinstance(value, Mapping):
        if not value:
            target = prefix or "value"
            flattened[target] = ""
        else:
            for key, nested in value.items():
                next_prefix = f"{prefix}.{key}" if prefix else str(key)
                _flatten_value(nested, next_prefix, flattened)
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        if not value:
            target = prefix or "value"
            flattened[target] = ""
        else:
            for index, item in enumerate(value):
                base = prefix or "value"
                next_prefix = f"{base}[{index}]"
                _flatten_value(item, next_prefix, flattened)
        return
    target = prefix or "value"
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


def _write_csv(
    name: str,
    records: Sequence[Mapping[str, Any]],
    context_fields: Sequence[str],
    timestamp: str,
) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = DATA_DIR / f"{timestamp}_{name}.csv"

    if records:
        normalised = _normalise_records(records)
        columns = _collect_columns(normalised)
    else:
        normalised = []
        columns = sorted(set(context_fields)) or ["value"]

    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in normalised:
            writer.writerow({column: record.get(column, "") for column in columns})
    print(f"Saved CSV  : {csv_path} ({csv_path.stat().st_size} bytes)")


def _request_json(
    session: requests.Session,
    method: str,
    url: str,
    *,
    headers: Mapping[str, str],
    params: Mapping[str, Any] | None,
) -> requests.Response | None:
    print(f"Request: {method} {url}")
    if params:
        print(f"         params={params}")
    try:
        response = session.request(
            method,
            url,
            headers=headers,
            params=params,
            timeout=REQUEST_TIMEOUT,
        )
    except requests.RequestException as exc:
        print(f"HTTP リクエストに失敗しました: {exc}", file=sys.stderr)
        return None

    print(f"HTTP {response.status_code}")
    if response.status_code == 204:
        print("(info) 応答が 204 No Content のためデータは出力されません。")
        return None

    if not response.ok:
        print(
            f"HTTP エラー: {response.status_code} {response.text[:200]}",
            file=sys.stderr,
        )
        return None
    return response


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
) -> None:
    formatted_path = _format_template(endpoint.path, context, name=endpoint.name)
    if not formatted_path:
        return
    url = _build_url(api_base, hotel_code, formatted_path)

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

    response = _request_json(session, endpoint.method, url, headers=headers, params=params)
    if response is None:
        return

    try:
        payload = response.json()
    except ValueError as exc:
        print(f"JSON 解析に失敗しました ({endpoint.name}): {exc}", file=sys.stderr)
        return

    records = _coerce_records(payload)
    augmented: list[MutableMapping[str, Any]] = []
    for record in records:
        augmented.append(_augment_record(record, endpoint.context_fields, context))

    aggregated[endpoint.name].extend(augmented)
    print(f"(info) {endpoint.name}: {len(augmented)} record(s)")

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
        help="予約日 (YYYY-MM-DD)。省略時は JST の昨日の日付を使用",
    )
    args = parser.parse_args(argv)

    _load_env()
    configs = _load_config(Path(args.config))

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

    reservation_date = _determine_reservation_date(args.date)

    base_context: dict[str, Any] = {
        "hotel_id": hotel_code,
        "reservation_date": reservation_date,
    }

    aggregated: dict[str, list[MutableMapping[str, Any]]] = defaultdict(list)

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
        )

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    for name, endpoint in endpoint_index.items():
        records = aggregated.get(name, [])
        _write_csv(name, records, endpoint.context_fields, timestamp)


if __name__ == "__main__":
    main()
