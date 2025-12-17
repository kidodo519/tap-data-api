from __future__ import annotations

import csv
import os
from copy import deepcopy
from pathlib import Path
from typing import Iterable, Mapping

import requests
import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config.yaml"
CSV_PATH = ROOT / "reservations.csv"
TIMEOUT = 30


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise SystemExit(f"環境変数 {name} が設定されていません")
    return value


def _extract_items(payload: object, preferred_key: str) -> Iterable[object]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return []

    if isinstance(payload.get(preferred_key), list):
        return payload[preferred_key]

    for key in ("items", "data", "reservations"):
        items = payload.get(key)
        if isinstance(items, list):
            return items
    return []


def _resolve_params(params: Mapping[str, str], context: Mapping[str, str]) -> dict[str, str]:
    resolved: dict[str, str] = {}
    for key, value in params.items():
        resolved[key] = value.format(**context) if isinstance(value, str) else str(value)
    return resolved


def _load_reservations_config() -> Mapping[str, object]:
    if not CONFIG_PATH.exists():
        raise SystemExit("config.yaml が見つかりません")
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    endpoints = config.get("reservations_endpoints") or []
    reservation_entry = next((e for e in endpoints if e.get("name") == "reservations"), None)
    if not reservation_entry:
        raise SystemExit("config.yaml に reservations の設定がありません")
    return deepcopy(reservation_entry)


def _prepare_fieldnames(items: Iterable[object], ensure_columns: list[str]) -> list[str]:
    for item in items:
        if isinstance(item, dict):
            extra_keys = [key for key in item.keys() if key not in ensure_columns]
            return ensure_columns + sorted(extra_keys)
    return ensure_columns


def main() -> None:
    load_dotenv(ROOT / ".env")

    api_base = _require_env("API_BASE").rstrip("/")
    hotel_code = _require_env("HOTEL_CODE")
    api_key = _require_env("TAP_API_KEY")

    config_entry = _load_reservations_config()

    date_range = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")).get("reservation_date_range") or {}
    reservation_date_from = date_range.get("from") or ""
    reservation_date_to = date_range.get("to") or ""
    context = {
        "reservation_date_from": reservation_date_from,
        "reservation_date_to": reservation_date_to,
    }

    params = _resolve_params(config_entry.get("params", {}), context)
    path = config_entry.get("path", "reservations").lstrip("/")
    url = f"{api_base}/hotels/{hotel_code}/{path}"

    ensure_columns = list(config_entry.get("ensure_columns") or [])
    cursor: str | None = None
    headers = {"X-API-Key": api_key}

    with CSV_PATH.open("w", encoding="utf-8-sig", newline="") as csv_file:
        writer: csv.DictWriter[str] | None = None
        fieldnames: list[str] = ensure_columns

        while True:
            page_params = dict(params)
            if cursor:
                page_params["cursor"] = cursor

            response = requests.get(url, headers=headers, params=page_params, timeout=TIMEOUT)
            response.raise_for_status()
            payload = response.json()

            items = list(_extract_items(payload, preferred_key="reservations"))

            if writer is None:
                fieldnames = _prepare_fieldnames(items, ensure_columns)
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

            if writer and fieldnames:
                for item in items:
                    if isinstance(item, dict):
                        writer.writerow({key: item.get(key, "") for key in fieldnames})

            cursor = payload.get("next_cursor") if isinstance(payload, dict) else None
            if not cursor:
                break

    print(f"予約データを {CSV_PATH.name} に出力しました")


if __name__ == "__main__":
    main()
