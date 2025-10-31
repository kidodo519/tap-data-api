# Tap Data API Tools

TapHub の provisions API を叩いて JSON/CSV を保存するワンショットツールです。

## セットアップ
1. ルート直下にある [`.env.example`](./.env.example) をコピーして `.env` を作成します。
2. `.env` に API のエンドポイントやホテルコード、API キーを入力します。
3. Python の依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```

## 使い方
### Python から直接実行
```bash
python fetch_provisions_csv.py [resource]
```

引数 `resource` を省略すると `provisions` エンドポイントを利用します。`reservations`
など別のリソースを取得したい場合は `python fetch_provisions_csv.py reservations` のように
指定してください。環境変数 `TAP_RESOURCE` でも同様に切り替えられます。

実行すると `data/` ディレクトリが自動で作成され、`{resource}_YYYYMMDDHHMMSS.json` と
`{resource}_YYYYMMDDHHMMSS.csv` の 2 つのファイルが出力されます (`resource` は使用した
エンドポイント名)。CSV にはレスポンス内の全てのキーがドット (`.`) やインデックス
(`[0]` など) を使ったフラットな列名として展開されるため、ネストされたオブジェクトや
配列の内容もセルごとに確認できます。

### シェルスクリプト / PowerShell を利用
- macOS / Linux / WSL:
  ```bash
  chmod +x scripts/fetch.sh
  ./scripts/fetch.sh
  ```
- Windows (PowerShell):
  ```powershell
  scripts\fetch.ps1
  ```
  もしくは
  ```powershell
  pwsh -File scripts/fetch.ps1
  ```

環境変数 `PYTHON_BIN` を設定すると使用する Python 実行ファイルを変更できます。

## トラブルシューティング
- `.env` が正しく配置されているか確認してください。
- プロキシ環境では `requests` に対応する環境変数 (`HTTP_PROXY` など) を設定してください。
- CSV には UTF-8 (BOM 付き) で書き出されるため、Excel でも文字化けせずに開けます。
