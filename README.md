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

スクリプトを実行すると `data/` ディレクトリに、タイムスタンプ付きの 3 つの集約 CSV
(`YYYYMMDDHHMMSS_reservations.csv` / `YYYYMMDDHHMMSS_sales.csv` / `YYYYMMDDHHMMSS_rooms.csv`)
のみが出力されます。`reservations` は予約の基本情報 (`reservations` /
`reservation_meal_reservations`)、`sales` は会計系 (`reservation_slip_reservations` /
`reservation_revenue`)、`rooms` は部屋関連 (`reservation_rooms` /
`reservation_room_check_in`) を統合したものです。レスポンスが空の場合でも、設定した
`context_fields` に基づいたヘッダーのみの CSV が生成されます。

### 認証について
`API/swagger.json` では `securitySchemes` として `AccessToken` が定義されており、
ヘッダー `X-API-Key` を使う API キー認証のみが記載されています。ベーシック認証や
「リバプロID/PW」のような別認証は Swagger には登場しません。そのため、このリポジトリに
含まれるスクリプトでも環境変数 `TAP_API_KEY` を読み込み、`X-API-Key` ヘッダーを
付与して呼び出す実装になっています。

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
- API から一時的な `429`/`503`/`504` が返る場合は自動で最大 3 回リトライします。頻発する場合は
  実行間隔を空けて再実行してください。
- CSV には UTF-8 (BOM 付き) で書き出されるため、Excel でも文字化けせずに開けます。
- `reservations` が 0 件になるときは、次を確認してください。
    - 予約日が意図せずずれていないか: スクリプト起動時に `(info) 取得を開始します: 2025-04-01 -> 2025-04-01` のように解決した日付が表示されます。ここが期待と違う場合は `--date` または `config/reservation_date_range.json` を修正し、`from/to` 両方が埋まっているか確認します。
  - API 側にデータが存在するか: 管理画面や DB で、指定した期間に予約があるかを確認します。期間中に予約がない場合は 200 でも 0 件が返ります。
  - 環境変数が正しいか: `.env` の `API_BASE` と `HOTEL_CODE` が稼働環境の値か確認してください。誤ったホテルコードを指定すると、認証は通っても予約一覧が空になります。
  - クエリを実際に投げているか: 取得開始と完了時に日付範囲と保存先がログに出ます。外形的に実行されていることを確認できます。詳細なリクエスト/レスポンスログは出力しません。
  - `API/generated_service-set-pms-reservation_README-API.md` の定義では `/hotels/{hotel_id}/reservations` に `from_reservation_date` と `to_reservation_date` が必須で、`control_status` は `Reserve`/`Cancel`/`Stay`/`PartialStay`/`NoShow` のみ受け付けられます。意図しないフィルタを付けていないかを確認してください。
  - 同ドキュメントにはページング用の `next_cursor` が返る場合があると記載されています。ダッシュボードなど他ツールでは件数が多いのに CSV が少ない場合、`cursor` パラメーターを使った追跡取得が必要かを検討してください。
