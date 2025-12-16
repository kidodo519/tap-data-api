from __future__ import annotations

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
    resource = os.getenv("TAP_RESOURCE", "provisions").strip("/") or "provisions"

    url = f"{api_base}/hotels/{hotel_code}/{resource}"
    cursor: str | None = None
    headers = {"X-API-Key": api_key}

    while True:
        params = {"cursor": cursor} if cursor else None
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()

        for item in _extract_items(payload, preferred_key=resource):
            print(json.dumps(item, ensure_ascii=False))

        if isinstance(payload, dict):
            cursor = payload.get("next_cursor") or payload.get("cursor")
        else:
            cursor = None
        if not cursor:
            break


if __name__ == "__main__":
    main()
