# python/fetch.py
# TapHub API を叩いて ../data/ に保存
import os
import sys
import json
from pathlib import Path
from datetime import datetime

from dotenv import load_dotenv
import requests

ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = ROOT / ".env"
DATA_DIR = ROOT / "data"

if not ENV_PATH.exists():
    print(f".env が見つかりません: {ENV_PATH}", file=sys.stderr)
    sys.exit(1)

load_dotenv(ENV_PATH)

API_BASE = os.getenv("API_BASE")
HOTEL_CODE = os.getenv("HOTEL_CODE")
TAP_API_KEY = os.getenv("TAP_API_KEY")

missing = [k for k,v in {"API_BASE":API_BASE,"HOTEL_CODE":HOTEL_CODE,"TAP_API_KEY":TAP_API_KEY}.items() if not v]
if missing:
    print(f"未設定の環境変数があります: {', '.join(missing)}", file=sys.stderr)
    sys.exit(2)

url = f"{API_BASE}/hotels/{HOTEL_CODE}/provisions"
headers = {
    "Accept": "application/json",
    "X-API-Key": TAP_API_KEY,
}

DATA_DIR.mkdir(parents=True, exist_ok=True)
stamp = datetime.now().strftime("%Y%m%d%H%M%S")
out_path = DATA_DIR / f"provisions_{stamp}.json"

print(f"Request: {url}")
try:
    resp = requests.get(url, headers=headers, timeout=30)
except requests.RequestException as e:
    print(f"HTTP リクエストに失敗: {e}", file=sys.stderr)
    sys.exit(3)

print(f"HTTP {resp.status_code}")
resp.raise_for_status()

# 保存（バイナリではなくテキスト。エンコーディングはHTTPヘッダー準拠）
out_path.write_text(resp.text, encoding=resp.encoding or "utf-8")
print(f"Saved: {out_path} ({out_path.stat().st_size} bytes)")

# 整形表示（JSON の場合のみ）
try:
    parsed = resp.json()
    print(json.dumps(parsed, ensure_ascii=False, indent=2)[:10000])  # 標準出力は最大1万文字まで
except Exception:
    print("(注) レスポンスは JSON ではない可能性があります（ファイルには保存済み）。")
