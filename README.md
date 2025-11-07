# Tap Data API Tools

TapHub の API を叩いて CSV を保存するワンショットツールです。

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
指定してください。単数形 (`reservation` など) で指定した場合も自動的に正しい
エンドポイントへ置き換えます。環境変数 `TAP_RESOURCE` でも同様に切り替えられます。

実行すると `data/` ディレクトリが自動で作成され、`{resource}_YYYYMMDDHHMMSS.json` と
`{resource}_YYYYMMDDHHMMSS.csv` の 2 つのファイルが出力されます (`resource` は使用した
エンドポイント名)。CSV にはレスポンス内の全てのキーがドット (`.`) やインデックス
(`[0]` など) を使ったフラットな列名として展開されるため、ネストされたオブジェクトや
配列の内容もセルごとに確認できます。

### 予約関連 API を日次で収集する
予約一覧と、その予約 ID を使う関連エンドポイントをまとめて取得したい場合は
`fetch_reservations_csv.py` を使用します。設定ファイル `config/reservations_endpoints.json`
に呼び出すエンドポイントと付随するパラメーターを列挙しておくと、スクリプトが順番に
リクエストを実行し CSV として保存します。既定では JST の「昨日」を予約日として
`GET /hotels/{hotel_id}/reservations?from_reservation_date=...&to_reservation_date=...` を呼び出し、
取得した予約の `reservation_id` を使って子エンドポイントも呼び出します。

```bash
python fetch_reservations_csv.py
```

オプション:

- `--date`: `YYYY-MM-DD` 形式で予約日を指定できます。省略時は JST の昨日になります。
- `--config`: デフォルト以外のエンドポイント設定ファイルを使用する場合に指定します。

スクリプトを実行すると `data/` ディレクトリに `YYYYMMDDHHMMSS_{endpoint_name}.csv` が
出力されます。JSON は保存されません。レスポンスが空の場合でも、設定した
`context_fields` に基づいたヘッダーのみの CSV が生成されます。

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
