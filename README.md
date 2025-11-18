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

実行すると `data/` ディレクトリが自動で作成され、`{resource}_YYYYMMDDHHMMSS.csv`
(`resource` は使用したエンドポイント名) が出力されます。CSV にはレスポンス内の全てのキーが
ドット (`.`) で区切られた末尾のキー名を基にしたシンプルな列名として展開されます。
配列要素が複数ある場合は同じ列名が重複しないよう `name`, `name_2`, `name_3` のように
連番が付与されます。ネストされたオブジェクトや配列の内容も簡潔なヘッダーで確認できます。

### 予約関連 API を日次で収集する
予約一覧と、その予約 ID を使う関連エンドポイントをまとめて取得したい場合は
`fetch_reservations_csv.py` を使用します。設定ファイル `config/reservations_endpoints.json`
に呼び出すエンドポイントと付随するパラメーターを列挙しておくと、スクリプトが順番に
リクエストを実行し CSV として保存します。予約日の範囲は `config/reservation_date_range.json`
に JSON 形式で保存しておくと読み込まれます (`{"from": "2025-01-01", "to": "2025-01-07"}` のように
指定)。雛形として `config/reservation_date_range.json.example` を用意しているのでコピーして使用して
ください。ファイルが存在しない場合は JST の「昨日」が `from`/`to` 共通の日付として利用されます。
取得した予約の `reservation_id` を使って子エンドポイントも呼び出します。

```bash
python fetch_reservations_csv.py
```

オプション:

- `--date`: `YYYY-MM-DD` 形式で単一日を指定できます。`from`/`to` の両方に同じ日付が適用されます。
- `--from-date`, `--to-date`: `YYYY-MM-DD` 形式で予約日の開始・終了を指定します。セットで使用します。
- `--date-range-file`: `from`/`to` を保持した JSON ファイルのパスを指定します。省略時は
  `config/reservation_date_range.json` を読み込みます。
- `--config`: デフォルト以外のエンドポイント設定ファイルを使用する場合に指定します。
- `--swagger`: `API/swagger.json` 以外の OpenAPI/Swagger JSON を参照したい場合に指定します。
- 対話的に実行するときは `--date` を省略して Enter キーを押すと、プロンプトが表示され手動で
  予約日を入力できます (未入力の場合は昨日の日付が利用されます)。

エンドポイントごとの全カラムを出力するため、デフォルトで `API/swagger.json` から取得したレスポンス
スキーマを走査し、200 応答に含まれるプロパティ名を `ensure_columns` に自動設定します。Swagger を
変更した場合は、スクリプト実行時に `--swagger` で更新後のファイルを指すようにしてください。
特定の列を必ず含めたい場合は `config/reservations_endpoints.json` の該当エントリに `ensure_columns`
を明示的に書き換えれば上書きできます。

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
