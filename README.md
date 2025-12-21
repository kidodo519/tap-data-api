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
`main.py` を使用します。設定はリポジトリルートの `config.yaml` にまとめます。
呼び出すエンドポイントと付随するパラメーターを `reservations_endpoints` 配列として列挙しておくと、
スクリプトが順番にリクエストを実行し CSV として保存します。予約日の範囲は
`reservation_date_range` で指定できます (`from`/`to` が未設定の場合は JST の「昨日」が共通日付として利用されます)。
出力形式は `reservations_output.formats` に `csv`/`json` を配列で列挙してください。設定例:

```yaml
reservation_date_range:
  from: "2025-01-01"
  to: "2025-01-01"

reservations_endpoints:
  - name: reservations
    path: reservations
    params:
      from_reservation_date: "{reservation_date_from}"
      to_reservation_date: "{reservation_date_to}"
    context_fields:
      - reservation_date_from
      - reservation_date_to
    column_types:
      reservation_id: integer
      check_in_date: date
    children:
      - name: reservation_rooms
        path: reservations/{reservation_id}/rooms
        context_fields:
          - reservation_id
          - reservation_number
          - reservation_date_from
          - reservation_date_to
        inherit_ensure_columns: true
reservations_output:
  formats: ["csv"]
```

取得した予約の `reservation_id` を使って子エンドポイントも呼び出します。

```bash
python main.py
```

オプション:

- `--date`: `YYYY-MM-DD` 形式で単一日を指定できます。`from`/`to` の両方に同じ日付が適用されます。
- `--from-date`, `--to-date`: `YYYY-MM-DD` 形式で予約日の開始・終了を指定します。セットで使用します。
- `--config`: デフォルト以外の YAML 設定ファイルを使用する場合に指定します。
- `--swagger`: `API/swagger.json` 以外の OpenAPI/Swagger JSON を参照したい場合に指定します。
- 対話的に実行するときは `--date` を省略して Enter キーを押すと、プロンプトが表示され手動で
  予約日を入力できます (未入力の場合は昨日の日付が利用されます)。

エンドポイントごとの全カラムを出力するため、デフォルトで `API/swagger.json` から取得したレスポンス
スキーマを走査し、200 応答に含まれるプロパティ名を `ensure_columns` に自動設定します。Swagger を
変更した場合は、スクリプト実行時に `--swagger` で更新後のファイルを指すようにしてください。
特定の列を必ず含めたい場合は `config.yaml` の該当エントリに `ensure_columns`
を明示的に書き換えれば上書きできます。

スクリプトを実行すると `data/` ディレクトリに、タイムスタンプ付きの 3 つの集約ファイル
(`YYYYMMDDHHMMSS_reservations.*` / `YYYYMMDDHHMMSS_sales.*` / `YYYYMMDDHHMMSS_rooms.*`)
が出力されます。`config.yaml` の `reservations_output.formats` に `"csv"`/`"json"` を
列挙すると、指定した拡張子ごとに同名ファイルが生成されます。設定ファイルが存在しない場合は
従来通り CSV のみを出力します。`reservations` は予約の基本情報 (`reservations` /
`reservation_meal_reservations`)、`sales` は会計系 (`reservation_slip_reservations` /
`reservation_revenue`)、`rooms` は部屋関連 (`reservation_rooms` /
`reservation_room_check_in`) を統合したものです。レスポンスが空の場合でも、設定した
`context_fields` に基づいたヘッダーのみの CSV が生成されます。

`column_types` をエンドポイントごとに指定すると、`integer`/`date`/`datetime`/`boolean`/`string`
といった型ラベルに応じて取得データを軽量な共通関数で整形します。カラム単位での変換処理を
`config.yaml` 側へ寄せられるため、`main.py` の変更を抑えつつ型整形を行えます。

### 滞在履歴 (history) / 予約オンハンド (onhand) をまとめて取得する
`range_fetcher.py` は `main.py` を残したまま新規作成した最小構成のスクリプトで、`stays` (履歴) と
`reservations` (オンハンド) をそれぞれ別日付範囲で取得し、ID を元に `sales` と `rooms` を
引き続き取得して 6 種類のファイル (history/onhand × reservations/sales/rooms) を生成します。

- 出力形式は `csv` / `json` を `range_fetch_config.yaml` の `output.formats` で選択できます。
- `columns` セクションでデータセットごとの出力カラムを絞り込めます (デフォルトは `main.py`/`config.yaml` と同等の列)。
- `ranges.history/onhand` で日付範囲の ON/OFF と手動入力の有無を指定できます。
  - 自動取得時は history: 「今日から 2 日前の単日」、onhand: 「昨日から 178 日後」になります。
  - 日付が広い場合は `fetching.chunking` の設定に従って範囲を分割し、タイムアウト時は直前までの
    日付から自動で再開します (`retry_days_per_request` で再リクエスト幅を指定)。
  - 同一カーソルが再登場した場合はループを検出して処理を終了します。
- 取得したファイルはローカル (`data/range_exports` がデフォルト) か S3 への転送を選択できます。
  - `destination: s3` にして `output.s3.bucket`/`prefix` を設定すると自動でアップロードします。
- `reservations` には予約本体に加え食事予約 (`meal-reservations`) の結果を結合し、`sales` は売上 (`slip-reservations`) と収益 (`revenue`) をまとめて 1 ファイルにします。`rooms` は部屋関連 (`rooms`) をマージします。
- 子エンドポイントが 4xx/5xx を返した場合は警告を出してスキップし、他の予約の処理は継続します。

設定例 (抜粋):
```yaml
ranges:
  history:
    enabled: true
    use_manual_dates: false
  onhand:
    enabled: true
    use_manual_dates: true
    manual_from: "2025-02-01"
    manual_to: "2025-02-15"
output:
  formats: ["csv", "json"]
  destination: local
columns:
  reservations: ["reservation_number", "check_in_date", "control_status"]
  sales: ["reservation_id", "date", "total_price"]
  rooms: ["reservation_id", "room_number", "room_type_code"]
fetching:
  chunking:
    enabled: true
    days_per_request: 14
    resume_after_timeout: true
    retry_days_per_request: 7
```

実行:
```bash
python range_fetcher.py --config range_fetch_config.yaml
```

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
    - 予約日が意図せずずれていないか: スクリプト起動時に `(info) 取得を開始します: 2025-04-01 -> 2025-04-01` のように解決した日付が表示されます。ここが期待と違う場合は `--date` または `config.yaml` の `reservation_date_range` を修正し、`from`/`to` 両方が埋まっているか確認します。
  - API 側にデータが存在するか: 管理画面や DB で、指定した期間に予約があるかを確認します。期間中に予約がない場合は 200 でも 0 件が返ります。
  - 環境変数が正しいか: `.env` の `API_BASE` と `HOTEL_CODE` が稼働環境の値か確認してください。誤ったホテルコードを指定すると、認証は通っても予約一覧が空になります。
    - クエリを実際に投げているか: 取得開始と完了時に日付範囲と保存先がログに出ます。外形的に実行されていることを確認できます。詳細なリクエスト/レスポンスログは出力しません。HTTP エラーが発生した場合は完了前に 1 行の警告としてまとめて表示されます。
  - `API/generated_service-set-pms-reservation_README-API.md` の定義では `/hotels/{hotel_id}/reservations` に `from_reservation_date` と `to_reservation_date` が必須で、`control_status` は `Reserve`/`Cancel`/`Stay`/`PartialStay`/`NoShow` のみ受け付けられます。意図しないフィルタを付けていないかを確認してください。
  - 同ドキュメントにはページング用の `next_cursor` が返る場合があると記載されています。ダッシュボードなど他ツールでは件数が多いのに CSV が少ない場合、`cursor` パラメーターを使った追跡取得が必要かを検討してください。
