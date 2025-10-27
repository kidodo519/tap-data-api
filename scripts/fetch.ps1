#!/usr/bin/env pwsh
# Export TapHub provisions as CSV via Python helper
$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Resolve-Path (Join-Path $ScriptDir '..')
$PythonBin = if ($env:PYTHON_BIN) { $env:PYTHON_BIN } else { 'python' }

Set-Location $RootDir

if (-Not (Test-Path (Join-Path $RootDir '.env'))) {
    Write-Error '.env が見つかりません（.env.example をコピーして作成してください）'
}

& $PythonBin (Join-Path $RootDir 'fetch_provisions_csv.py')
