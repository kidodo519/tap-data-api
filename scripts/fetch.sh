#!/usr/bin/env bash
# Export TapHub provisions as CSV via Python helper
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PYTHON_BIN=${PYTHON_BIN:-python3}

cd "$ROOT_DIR"

if [[ ! -f "$ROOT_DIR/.env" ]]; then
  echo ".env が見つかりません（.env.example をコピーして作成してください）" >&2
  exit 1
fi

exec "$PYTHON_BIN" "$ROOT_DIR/fetch_provisions_csv.py"
