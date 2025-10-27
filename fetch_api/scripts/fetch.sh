#!/usr/bin/env bash
# scripts/fetch.sh
# TapHub API から provisions を取得し data/ に保存
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f ".env" ]]; then
  echo ".env が見つかりません（.env.example をコピーして作成してください）" >&2
  exit 1
fi

# .env を読み込む（export 付き）
set -a
# shellcheck disable=SC1091
. ./.env
set +a

: "${API_BASE:?API_BASE が未設定}"
: "${HOTEL_CODE:?HOTEL_CODE が未設定}"
: "${TAP_API_KEY:?TAP_API_KEY が未設定}"

mkdir -p "data"
STAMP="$(date +%Y%m%d%H%M%S)"
OUT="data/provisions_${STAMP}.json"
URL="${API_BASE}/hotels/${HOTEL_CODE}/provisions"

echo "Request: $URL"
echo "Saving to: $OUT"

curl --location "$URL" \
  --header "Accept: application/json" \
  --header "X-API-Key: ${TAP_API_KEY}" \
  -sS -o "$OUT" -w "\nHTTP %{http_code}\n"

if [[ ! -s "$OUT" ]]; then
  echo "出力が空の可能性があります: $OUT" >&2
  exit 2
fi

# jq があれば整形表示
if command -v jq >/dev/null 2>&1; then
  jq . "$OUT" || true
else
  echo "(ヒント) jq を入れると整形表示できます: sudo apt-get install jq"
fi

echo "Done."
