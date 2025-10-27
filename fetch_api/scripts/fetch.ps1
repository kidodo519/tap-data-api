# scripts/fetch.ps1
# TapHub API から provisions を取得し data/ に保存
# 必要: ルート直下の .env に API_BASE, HOTEL_CODE, TAP_API_KEY を設定

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# ルートに移動（このスクリプトの親フォルダの親）
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir
Set-Location $RootDir

# .env を読み込む（#始まりの行は無視）
$envPath = Join-Path $RootDir ".env"
if (-not (Test-Path $envPath)) {
  throw ".env が見つかりません: $envPath （.env.example をコピーして作成してください）"
}

Get-Content $envPath | ForEach-Object {
  if (-not ($_ -match '^\s*#') -and $_ -match '^\s*([^=]+)=(.*)\s*$') {
    $key = $Matches[1].Trim()
    $val = $Matches[2].Trim()
    [System.Environment]::SetEnvironmentVariable($key, $val, "Process")
  }
}

# 変数確認
$API_BASE = $env:API_BASE
$HOTEL_CODE = $env:HOTEL_CODE
$TAP_API_KEY = $env:TAP_API_KEY

if (-not $API_BASE -or -not $HOTEL_CODE -or -not $TAP_API_KEY) {
  throw "API_BASE / HOTEL_CODE / TAP_API_KEY のいずれかが未設定です（.env を確認してください）"
}

# 出力先
$dataDir = Join-Path $RootDir "data"
New-Item -ItemType Directory -Force -Path $dataDir | Out-Null
$stamp = Get-Date -Format "yyyyMMddHHmmss"
$outFile = Join-Path $dataDir ("provisions_{0}.json" -f $stamp)

# URL 構築
$Url = "$API_BASE/hotels/$HOTEL_CODE/provisions"

Write-Host "Request: $Url"
Write-Host "Saving to: $outFile"

# curl.exe を使う（PowerShellのcurlエイリアスではない明示）
$cmd = @(
  "curl.exe",
  "--location", $Url,
  "--header", "Accept: application/json",
  "--header", "X-API-Key: $TAP_API_KEY",
  "-o", $outFile,
  "-sS", "-w", "`nHTTP %{http_code}`n"
)

$process = Start-Process -FilePath $cmd[0] -ArgumentList $cmd[1..($cmd.Length-1)] -NoNewWindow -PassThru -Wait
if ($LASTEXITCODE -ne 0) {
  throw "curl 実行に失敗しました（exit code=$LASTEXITCODE）"
}

# ざっくり検査
if (-not (Test-Path $outFile) -or (Get-Item $outFile).Length -lt 2) {
  throw "出力が空の可能性があります: $outFile"
}

Write-Host "Done."
try {
  # JSON 整形表示（確認用）
  (Get-Content $outFile -Raw) | ConvertFrom-Json | ConvertTo-Json -Depth 10
} catch {
  Write-Warning "JSON の整形表示に失敗しました（生データは $outFile に保存済み）"
}
