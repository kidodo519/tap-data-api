#!/usr/bin/env python3
"""Fetch TapHub provisions API response and export it as CSV."""
from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path
import re
from collections.abc import Mapping, MutableMapping, Sequence
from typing import List

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

_RESOURCE_ALIASES = {
    "provision": "provisions",
    "reservation": "reservations",
}


def _normalise_resource(resource: str) -> str:
    """Resolve resource aliases to actual endpoint names."""

    plain = resource.strip("/")
    if not plain:
        return "provisions"

    # Only substitute when the entire segment matches to avoid altering nested paths.
    replacement = _RESOURCE_ALIASES.get(plain.lower())
    if replacement:
        if resource != replacement:
            print(f"(info) '{resource}' を '{replacement}' に置き換えてアクセスします。")
        return replacement
    return plain


def _determine_resource(argv: Sequence[str]) -> str:
    if len(argv) > 1 and argv[1]:
        return _normalise_resource(argv[1])

    env_resource = os.getenv("TAP_RESOURCE")
    if env_resource:
        return _normalise_resource(env_resource)

    return "provisions"


def _build_request(resource: str) -> tuple[str, Mapping[str, str]]:
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

    url = f"{api_base.rstrip('/')}/hotels/{hotel_code}/{resource}"
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


def _flatten_value(value: object, prefix: str, flattened: MutableMapping[str, str]) -> None:
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
            for index, item in enumerate(value):
                base = prefix or "value"
                next_prefix = f"{base}[{index}]"
                _flatten_value(item, next_prefix, flattened)
        return

    target = _next_available_column(_simplify_column_name(prefix), flattened)
    flattened[target] = _serialise_value(value)


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


def _normalise_records(
    records: Sequence[Mapping[str, object]]
) -> List[dict[str, str]]:
    normalised: List[dict[str, str]] = []
    for record in records:
        flattened: dict[str, str] = {}
        for key, value in record.items():
            _flatten_value(value, str(key), flattened)
        if not flattened:
            flattened["value"] = ""
        normalised.append(flattened)
    return normalised


def _collect_columns(records: Sequence[Mapping[str, str]]) -> List[str]:
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


def _write_csv(
    resource: str,
    records: Sequence[Mapping[str, object]],
) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    resource_slug = resource.replace("/", "_") or "resource"
    csv_path = DATA_DIR / f"{resource_slug}_{stamp}.csv"

    normalised = _normalise_records(records)
    columns = _collect_columns(normalised)
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for record in normalised:
            writer.writerow({column: record.get(column, "") for column in columns})
    print(f"Saved CSV  : {csv_path} ({csv_path.stat().st_size} bytes)")


def main() -> None:
    _load_env()
    resource = _determine_resource(sys.argv)
    url, headers = _build_request(resource)
    response = _request_json(url, headers)

    try:
        payload = response.json()
    except ValueError as exc:
        print(f"JSON 解析に失敗しました: {exc}", file=sys.stderr)
        sys.exit(6)

    records = _ensure_records(payload)
    _write_csv(resource, records)


if __name__ == "__main__":
    main()
