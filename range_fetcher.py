#!/usr/bin/env python3
"""Range-based fetcher for history/onhand reservations, sales, and rooms."""
from __future__ import annotations

import argparse
import csv
import json
import os
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, MutableMapping, Sequence

import boto3
import requests
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
DEFAULT_CONFIG_PATH = ROOT / "range_fetch_config.yaml"
DEFAULT_OUTPUT_DIR = ROOT / "data" / "range_exports"
DEFAULT_TIMEOUT = 30
DEFAULT_COLUMNS: dict[str, tuple[str, ...]] = {
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
    "sales": (
        "reservation_number",
        "date",
        "item",
        "total_price",
        "tax_include",
        "quantity",
        "number_of_use",
        "sales_amount",
        "meal_amount",
        "total",
        "request_url",
    ),
    "rooms": (
        "reservation_number",
        "date",
        "room_number",
        "room_type_code",
        "request_url",
    ),
}


@dataclass
class RangeSettings:
    enabled: bool
    use_manual_dates: bool
    manual_from: date | None
    manual_to: date | None


@dataclass
class DefaultsSettings:
    history_days_ago: int = 2
    onhand_start_offset_days: int = -1
    onhand_end_offset_days: int = 178


@dataclass
class ChunkingSettings:
    enabled: bool
    days_per_request: int
    resume_after_timeout: bool
    retry_days_per_request: int


@dataclass
class FetchingSettings:
    timeout_seconds: int
    chunking: ChunkingSettings
    cursor_loop_guard: bool


@dataclass
class OutputSettings:
    formats: Sequence[str]
    destination: str
    local_directory: Path
    s3_bucket: str | None
    s3_prefix: str | None
    filename_prefix: str


@dataclass
class ColumnSettings:
    reservations: Sequence[str] = field(default_factory=tuple)
    sales: Sequence[str] = field(default_factory=tuple)
    rooms: Sequence[str] = field(default_factory=tuple)


@dataclass
class Settings:
    ranges: Dict[str, RangeSettings]
    defaults: DefaultsSettings
    output: OutputSettings
    fetching: FetchingSettings
    columns: ColumnSettings


class ApiClient:
    def __init__(self, api_base: str, hotel_code: str, api_key: str, timeout: int) -> None:
        self.api_base = api_base.rstrip("/")
        self.hotel_code = hotel_code
        self.session = requests.Session()
        self.session.headers.update({"X-API-Key": api_key})
        self.timeout = timeout

    def _build_url(self, path: str) -> str:
        return f"{self.api_base}{path}"

    def fetch(
        self,
        path: str,
        params: MutableMapping[str, Any],
        data_key: str,
        cursor_guard: bool = True,
    ) -> list[dict[str, Any]]:
        url = self._build_url(path)
        collected: list[dict[str, Any]] = []
        cursor = params.get("cursor")
        seen_cursors: set[str] = set()
        if cursor:
            seen_cursors.add(cursor)

        while True:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            payload = response.json()
            body = payload.get(data_key, [])
            if isinstance(body, list):
                collected.extend(body)
            next_cursor = payload.get("next_cursor")
            if not next_cursor:
                break
            if cursor_guard and next_cursor in seen_cursors:
                break
            seen_cursors.add(next_cursor)
            params = dict(params)
            params["cursor"] = next_cursor
        return collected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG_PATH, help="Path to YAML config.")
    return parser.parse_args()


def _as_date(value: Any) -> date | None:
    if value is None:
        return None
    if isinstance(value, date):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        return date.fromisoformat(value)
    return None


def _parse_range_settings(data: Dict[str, Any]) -> Dict[str, RangeSettings]:
    parsed: Dict[str, RangeSettings] = {}
    for key, payload in data.items():
        parsed[key] = RangeSettings(
            enabled=bool(payload.get("enabled", True)),
            use_manual_dates=bool(payload.get("use_manual_dates", False)),
            manual_from=_as_date(payload.get("manual_from")),
            manual_to=_as_date(payload.get("manual_to")),
        )
    return parsed


def load_settings(path: Path) -> Settings:
    with path.open("r", encoding="utf-8") as handle:
        raw = yaml.safe_load(handle)

    ranges = _parse_range_settings(raw.get("ranges", {}))
    defaults = raw.get("defaults", {})
    output_raw = raw.get("output", {})
    fetching_raw = raw.get("fetching", {})
    chunking_raw = fetching_raw.get("chunking", {})
    columns_raw = raw.get("columns", {})

    settings = Settings(
        ranges=ranges,
        defaults=DefaultsSettings(
            history_days_ago=int(defaults.get("history_days_ago", 2)),
            onhand_start_offset_days=int(defaults.get("onhand_start_offset_days", -1)),
            onhand_end_offset_days=int(defaults.get("onhand_end_offset_days", 178)),
        ),
        output=OutputSettings(
            formats=tuple(output_raw.get("formats", ["csv"])),
            destination=str(output_raw.get("destination", "local")),
            local_directory=ROOT / output_raw.get("local_directory", DEFAULT_OUTPUT_DIR),
            s3_bucket=output_raw.get("s3", {}).get("bucket"),
            s3_prefix=output_raw.get("s3", {}).get("prefix"),
            filename_prefix=str(output_raw.get("filename_prefix", "tap_range")),
        ),
        fetching=FetchingSettings(
            timeout_seconds=int(fetching_raw.get("timeout_seconds", DEFAULT_TIMEOUT)),
            cursor_loop_guard=bool(fetching_raw.get("cursor_loop_guard", True)),
            chunking=ChunkingSettings(
                enabled=bool(chunking_raw.get("enabled", True)),
                days_per_request=int(chunking_raw.get("days_per_request", 30)),
                resume_after_timeout=bool(chunking_raw.get("resume_after_timeout", True)),
                retry_days_per_request=int(chunking_raw.get("retry_days_per_request", 7)),
            ),
        ),
        columns=ColumnSettings(
            reservations=tuple(columns_raw.get("reservations") or DEFAULT_COLUMNS["reservations"]),
            sales=tuple(columns_raw.get("sales") or DEFAULT_COLUMNS["sales"]),
            rooms=tuple(columns_raw.get("rooms") or DEFAULT_COLUMNS["rooms"]),
        ),
    )
    return settings


def resolve_date_range(name: str, settings: Settings, today: date) -> tuple[date, date] | None:
    config = settings.ranges.get(name)
    if not config or not config.enabled:
        return None
    if config.use_manual_dates:
        if not config.manual_from or not config.manual_to:
            raise ValueError(f"Manual dates for {name} must be provided when use_manual_dates is true.")
        return (config.manual_from, config.manual_to)
    if name == "history":
        target_day = today - timedelta(days=settings.defaults.history_days_ago)
        return (target_day, target_day)
    if name == "onhand":
        start = today + timedelta(days=settings.defaults.onhand_start_offset_days)
        end = today + timedelta(days=settings.defaults.onhand_end_offset_days)
        return (start, end)
    raise ValueError(f"Unknown range name: {name}")


def ensure_output_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def select_columns(row: Dict[str, Any], columns: Sequence[str]) -> Dict[str, Any]:
    if not columns:
        return dict(row)
    return {key: row.get(key) for key in columns}


def record_fingerprint(row: Dict[str, Any]) -> str:
    return json.dumps(row, ensure_ascii=False, sort_keys=True)


def extract_reservation_id(entry: Dict[str, Any]) -> str | None:
    for key in ("reservation_id", "reservationId", "reservation_number", "id", "id "):
        if key in entry and entry.get(key):
            return str(entry[key]).strip()
    return None


def normalize_date_value(value: Any) -> str | None:
    """Convert datetime-like values to YYYY-MM-DD for query parameters."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, str):
        try:
            parsed = datetime.fromisoformat(value)
        except ValueError:
            return None
        return parsed.date().isoformat()
    return None


def fetch_primary_records(
    api: ApiClient,
    range_name: str,
    date_from: date,
    date_to: date,
    settings: Settings,
) -> list[dict[str, Any]]:
    path = f"/hotels/{api.hotel_code}/{'stays' if range_name == 'history' else 'reservations'}"
    data_key = "stays" if range_name == "history" else "reservations"
    chunk_settings = settings.fetching.chunking
    chunk_size = max(1, chunk_settings.days_per_request if chunk_settings.enabled else (date_to - date_from).days + 1)
    retry_size = max(1, chunk_settings.retry_days_per_request)
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    window = chunk_size
    cursor_start = date_from
    last_completed = date_from - timedelta(days=1)

    while cursor_start <= date_to:
        cursor_end = min(cursor_start + timedelta(days=window - 1), date_to)
        params: MutableMapping[str, Any] = {
            "from_reservation_date": cursor_start.isoformat(),
            "to_reservation_date": cursor_end.isoformat(),
        }
        try:
            rows = api.fetch(path, params, data_key=data_key, cursor_guard=settings.fetching.cursor_loop_guard)
        except requests.Timeout:
            if not (chunk_settings.enabled and chunk_settings.resume_after_timeout):
                raise
            cursor_start = last_completed + timedelta(days=1)
            window = retry_size
            continue
        for row in rows:
            if "date_range_type" not in row:
                row["date_range_type"] = range_name
            fp = record_fingerprint(row)
            if fp in seen:
                continue
            seen.add(fp)
            results.append(row)
        last_completed = cursor_end
        cursor_start = cursor_end + timedelta(days=1)
        window = chunk_size
    return results


def fetch_child_records(
    api: ApiClient,
    parent_records: Iterable[dict[str, Any]],
    settings: Settings,
    data_key: str,
    path_template: str,
    default_from: date,
    default_to: date,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    for entry in parent_records:
        reservation_id = extract_reservation_id(entry)
        if not reservation_id:
            continue
        params: MutableMapping[str, Any] = {}
        date_from = normalize_date_value(
            entry.get("check_in_date")
            or entry.get("from_reservation_date")
            or default_from
        )
        date_to = normalize_date_value(
            entry.get("check_out_date")
            or entry.get("to_reservation_date")
            or default_to
        )
        if date_from:
            params["from_reservation_date"] = date_from
        if date_to:
            params["to_reservation_date"] = date_to
        path = path_template.format(hotel_id=api.hotel_code, reservation_id=reservation_id)
        try:
            payload = api.fetch(path, params, data_key=data_key, cursor_guard=settings.fetching.cursor_loop_guard)
        except requests.Timeout:
            if not settings.fetching.chunking.resume_after_timeout:
                raise
            payload = api.fetch(path, params, data_key=data_key, cursor_guard=settings.fetching.cursor_loop_guard)
        except requests.HTTPError as exc:
            print(f"[warn] skip child endpoint due to HTTP error ({exc.response.status_code}): {path} params={params}")
            continue
        for item in payload:
            item.setdefault("reservation_id", reservation_id)
            fp = record_fingerprint(item)
            if fp in seen:
                continue
            seen.add(fp)
            rows.append(item)
    return rows


def merge_records(*collections: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    merged: list[dict[str, Any]] = []
    seen: set[str] = set()
    for collection in collections:
        for row in collection:
            fp = record_fingerprint(row)
            if fp in seen:
                continue
            seen.add(fp)
            merged.append(row)
    return merged


def export_records(
    name: str,
    records: list[dict[str, Any]],
    columns: Sequence[str],
    output: OutputSettings,
) -> list[Path]:
    ensure_output_dir(output.local_directory)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    base_name = f"{output.filename_prefix}_{timestamp}_{name}"
    produced: list[Path] = []
    fieldnames: list[str]
    if columns:
        fieldnames = list(columns)
    else:
        fieldnames = sorted({key for row in records for key in row})

    if "csv" in output.formats:
        csv_path = output.local_directory / f"{base_name}.csv"
        with csv_path.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            for row in records:
                writer.writerow(select_columns(row, fieldnames))
        produced.append(csv_path)
    if "json" in output.formats:
        json_path = output.local_directory / f"{base_name}.json"
        with json_path.open("w", encoding="utf-8") as handle:
            json.dump([select_columns(row, fieldnames) for row in records], handle, ensure_ascii=False, indent=2)
        produced.append(json_path)

    if output.destination.lower() == "s3":
        upload_to_s3(produced, output)
    return produced


def upload_to_s3(files: list[Path], output: OutputSettings) -> None:
    if not output.s3_bucket:
        raise ValueError("S3 bucket must be configured when destination is 's3'.")
    client = boto3.client("s3")
    prefix = (output.s3_prefix or "").rstrip("/")
    for path in files:
        key = f"{prefix}/{path.name}" if prefix else path.name
        client.upload_file(str(path), output.s3_bucket, key)


def main() -> None:
    args = parse_args()
    load_dotenv()
    settings = load_settings(args.config)

    api_base = os.environ.get("API_BASE")
    hotel_code = os.environ.get("HOTEL_CODE")
    api_key = os.environ.get("TAP_API_KEY")
    if not api_base or not hotel_code or not api_key:
        raise EnvironmentError("API_BASE, HOTEL_CODE, and TAP_API_KEY environment variables are required.")

    api_client = ApiClient(api_base, hotel_code, api_key, timeout=settings.fetching.timeout_seconds)
    today = date.today()
    ranges = {"history": resolve_date_range("history", settings, today), "onhand": resolve_date_range("onhand", settings, today)}

    datasets: dict[str, list[dict[str, Any]]] = {}

    for range_name, resolved in ranges.items():
        if not resolved:
            continue
        start, end = resolved
        print(f"[info] fetching {range_name}: {start.isoformat()} -> {end.isoformat()}")
        base_records = fetch_primary_records(api_client, range_name, start, end, settings)
        sales = fetch_child_records(
            api_client,
            base_records,
            settings,
            data_key="slip_reservations",
            path_template="/hotels/{hotel_id}/reservations/{reservation_id}/slip-reservations",
            default_from=start,
            default_to=end,
        )
        revenue = fetch_child_records(
            api_client,
            base_records,
            settings,
            data_key="revenue_info",
            path_template="/hotels/{hotel_id}/reservations/{reservation_id}/revenue",
            default_from=start,
            default_to=end,
        )
        meal_reservations = fetch_child_records(
            api_client,
            base_records,
            settings,
            data_key="meal_reservation",
            path_template="/hotels/{hotel_id}/reservations/{reservation_id}/meal-reservations",
            default_from=start,
            default_to=end,
        )
        rooms = fetch_child_records(
            api_client,
            base_records,
            settings,
            data_key="room_reservation",
            path_template="/hotels/{hotel_id}/reservations/{reservation_id}/rooms",
            default_from=start,
            default_to=end,
        )
        reservations_merged = merge_records(base_records, meal_reservations)
        sales_merged = merge_records(sales, revenue)
        rooms_merged = merge_records(rooms)
        datasets[f"{range_name}_reservations"] = [select_columns(row, settings.columns.reservations) for row in reservations_merged]
        datasets[f"{range_name}_sales"] = [select_columns(row, settings.columns.sales) for row in sales_merged]
        datasets[f"{range_name}_rooms"] = [select_columns(row, settings.columns.rooms) for row in rooms_merged]

    for name, records in datasets.items():
        if not records:
            continue
        column_selection: Sequence[str] = ()
        if name.endswith("reservations"):
            column_selection = settings.columns.reservations
        elif name.endswith("sales"):
            column_selection = settings.columns.sales
        elif name.endswith("rooms"):
            column_selection = settings.columns.rooms
        produced = export_records(name, records, columns=column_selection, output=settings.output)
        for path in produced:
            print(f"[info] wrote {path}")


if __name__ == "__main__":
    main()
