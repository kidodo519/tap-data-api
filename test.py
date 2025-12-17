from __future__ import annotations

import csv
import json
import os
from pathlib import Path
import sys
from typing import Iterable

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
load_dotenv(ROOT / ".env")


def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        sys.exit(f"環境変数 {name} が設定されていません")
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


def main() -> None:
    api_base = _require_env("API_BASE").rstrip("/")
    hotel_code = _require_env("HOTEL_CODE")
    api_key = _require_env("TAP_API_KEY")
    reservation_date_from = _require_env("FROM_RESERVATION_DATE")
    reservation_date_to = _require_env("TO_RESERVATION_DATE")
    initial_cursor = os.getenv("INITIAL_CURSOR")

    url = f"{api_base}/hotels/{hotel_code}/reservations"
    cursor: str | None = initial_cursor
    headers = {"X-API-Key": api_key}
    jsonl_path = ROOT / "reservations.jsonl"
    csv_path = ROOT / "reservations.csv"

    with jsonl_path.open("w", encoding="utf-8") as jsonl_file, csv_path.open(
        "w", encoding="utf-8", newline=""
    ) as csv_file:
        csv_writer: csv.DictWriter[str] | None = None
        fieldnames: list[str] | None = None

        while True:
            params = {
                "from_reservation_date": reservation_date_from,
                "to_reservation_date": reservation_date_to,
            }
            if cursor:
                params["cursor"] = cursor

            response = requests.get(url, headers=headers, params=params, timeout=30)
            response.raise_for_status()
            payload = response.json()

            for item in _extract_items(payload, preferred_key="reservations"):
                jsonl_file.write(json.dumps(item, ensure_ascii=False) + "\n")

                if isinstance(item, dict):
                    if csv_writer is None:
                        fieldnames = sorted(item.keys())
                        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        csv_writer.writeheader()
                    csv_writer.writerow({key: item.get(key, "") for key in fieldnames})

            if isinstance(payload, dict):
                cursor = payload.get("next_cursor") or payload.get("cursor")
            else:
                cursor = None
            if not cursor:
                break


if __name__ == "__main__":
    main()
