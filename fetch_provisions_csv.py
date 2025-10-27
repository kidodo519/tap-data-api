#!/usr/bin/env python3
"""Fetch TapHub provisions API response and export it as CSV."""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Mapping, MutableMapping, Sequence

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT / ".env"
DATA_DIR = ROOT / "data"


def _load_env() -> None:
    if not ENV_PATH.exists():
        print(f".env が見つかりません: {ENV_PATH}", file=sys.stderr)
        sys.exit(1)

    load_dotenv(ENV_PATH)


def _build_request() -> tuple[str, Mapping[str, str]]:
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
        print(
            f"未設定の環境変数があります: {', '.join(missing)}",
            file=sys.stderr,
        )
        sys.exit(2)

    url = f"{api_base.rstrip('/')}/hotels/{hotel_code}/provisions"
    headers = {
        "Accept": "application/json",
        "X-API-Key": api_key,
    }
    return url, headers


def _request_json(url: str, headers: Mapping[str, str]) -> requests.Response:
    print(f"Request: {url}")
    try:
        response = requests.get(url, headers=headers, timeout=30)
    except requests.RequestException as exc:
        print(f"HTTP リクエストに失敗: {exc}", file=sys.stderr)
        sys.exit(3)

    print(f"HTTP {response.status_code}")
    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        print(f"HTTP エラー: {exc}", file=sys.stderr)
        sys.exit(4)
    return response


def _ensure_records(payload: object) -> List[MutableMapping[str, object]]:
    if isinstance(payload, list):
        candidates = payload
    elif isinstance(payload, dict):
        for key in ("data", "items", "results", "rows"):
            value = payload.get(key) if isinstance(payload, dict) else None
            if isinstance(value, list):
                candidates = value
                break
        else:
            candidates = [payload]
    else:
        candidates = [payload]

    records: List[MutableMapping[str, object]] = []
    for index, item in enumerate(candidates):
        if isinstance(item, MutableMapping):
            records.append(item)
        else:
            records.append({"value": item})
            print(
                f"(注) {index} 番目の要素がオブジェクトではなかったため 'value' 列に変換しました。",
                file=sys.stderr,
            )
    if not records:
        print("レスポンスに出力対象のデータが見つかりませんでした。", file=sys.stderr)
        sys.exit(5)
    return records


def _collect_columns(records: Sequence[Mapping[str, object]]) -> List[str]:
    columns: set[str] = set()
    for record in records:
        columns.update(record.keys())
    ordered = sorted(columns)
    if not ordered:
        ordered = ["value"]
    return ordered


def _serialise_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False)


def _write_files(response: requests.Response, records: Sequence[Mapping[str, object]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    json_path = DATA_DIR / f"provisions_{stamp}.json"
    csv_path = DATA_DIR / f"provisions_{stamp}.csv"

    json_path.write_text(response.text, encoding=response.encoding or "utf-8")
    print(f"Saved JSON : {json_path} ({json_path.stat().st_size} bytes)")

    columns = _collect_columns(records)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({column: _serialise_value(record.get(column)) for column in columns})
    print(f"Saved CSV  : {csv_path} ({csv_path.stat().st_size} bytes)")


def main() -> None:
    _load_env()
    url, headers = _build_request()
    response = _request_json(url, headers)

    try:
        payload = response.json()
    except ValueError as exc:
        print(f"JSON 解析に失敗しました: {exc}", file=sys.stderr)
        sys.exit(6)

    records = _ensure_records(payload)
    _write_files(response, records)

    preview = json.dumps(payload, ensure_ascii=False, indent=2)
    print(preview[:10000])


if __name__ == "__main__":
    main()
