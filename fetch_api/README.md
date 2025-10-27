# fetch_api — TapHub API fetch templates

このパッケージは、**毎回のコマンド入力なしに** API を叩いて結果(JSON)を保存できるよう、
- PowerShell スクリプト (`scripts/fetch.ps1`)
- Bash スクリプト (`scripts/fetch.sh`)
- Python スクリプト (`python/fetch.py`)

の3通りを用意しています。**.env を1回設定**すれば、以降はダブルクリック/1コマンドで実行できます。

## 1) 事前準備 (.env を作成)
ルート直下に `.env` を作って、以下を設定してください（`.env.example` をコピーして編集）:

```
API_BASE=https://taphub-s01.prod.spms.tap-ic.co.jp/prod
HOTEL_CODE=001
TAP_API_KEY=ここにAPIキー
```

> 例のエンドポイントは `GET ${API_BASE}/hotels/${HOTEL_CODE}/provisions` を叩きます。

## 2) 実行方法

### A. Windows (PowerShell)
1. PowerShell を開く（右クリック「PowerShell で開く」等）。
2. プロジェクト直下に移動して実行:
   ```powershell
   scripts\fetch.ps1
   ```
   もしくは
   ```powershell
   pwsh -File scripts/fetch.ps1
   ```
3. 結果は `data/` 配下に `provisions_YYYYMMDDHHmmss.json` として保存されます。

### B. macOS / Linux / WSL (bash/zsh)
```bash
chmod +x scripts/fetch.sh
./scripts/fetch.sh
```
結果は `data/` に保存されます。

### C. Python で実行（クロスプラットフォーム）
```bash
cd python
pip install -r requirements.txt
python fetch.py
```
結果は `../data/` に保存されます。

## 3) うまくいかない時のチェック
- `.env` がルート直下にあり、`TAP_API_KEY` が正しいか。
- プロキシ/社内ネットワーク経由の場合、curl/requests のプロキシ設定が必要なことがあります。
- PowerShell で `curl` が別物のエイリアスになるケースがあるため、本スクリプトでは **`curl.exe` を強制使用**しています。
- Linux/macOS は `curl` コマンドが必要です（ほとんどの環境で標準搭載）。

## 構成
```
fetch_api/
  .env.example
  README.md
  data/                       # 出力先（自動作成）
  python/
    fetch.py
    requirements.txt
  scripts/
    fetch.ps1
    fetch.sh
```
