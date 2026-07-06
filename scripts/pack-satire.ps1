# One command: regenerate the satirical bundle AND zip it for uploading into Lovable.
#
# Usage (from the project root):
#   powershell -File scripts/pack-satire.ps1                 # from a local backend
#   $env:ROUNDTABLE_BASE_URL="https://aicoldwar.ngrok.app"; powershell -File scripts/pack-satire.ps1
#
# Produces:  public/satire-archive/   (the self-contained bundle, git-ignored)
#            exports/satire-archive.zip   <- drop its contents into Lovable's public/satire-archive/
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    $base = if ($env:ROUNDTABLE_BASE_URL) { $env:ROUNDTABLE_BASE_URL } else { "http://127.0.0.1:8000" }
    Write-Host "[pack-satire] generating bundle from $base..." -ForegroundColor Cyan
    node scripts/snapshot-satire.mjs
    if ($LASTEXITCODE -ne 0) { throw "snapshot-satire.mjs failed (is the backend running?)" }

    $src = Join-Path $root "public\satire-archive"
    if (-not (Test-Path (Join-Path $src "index.json"))) { throw "no bundle produced at $src" }

    New-Item -ItemType Directory -Force -Path (Join-Path $root "exports") | Out-Null
    $dst = Join-Path $root "exports\satire-archive.zip"
    if (Test-Path $dst) { Remove-Item $dst -Force }

    # Build the zip with FORWARD-SLASH entry names. PowerShell 5.1 Compress-Archive
    # stores backslashes, which Linux hosts (Lovable) extract as literal filenames
    # like "heads\us.webm" instead of a heads/ folder — breaking the bundle.
    Add-Type -AssemblyName System.IO.Compression | Out-Null
    Add-Type -AssemblyName System.IO.Compression.FileSystem | Out-Null
    $zip = [System.IO.Compression.ZipFile]::Open($dst, [System.IO.Compression.ZipArchiveMode]::Create)
    try {
        Get-ChildItem -Path $src -Recurse -File | ForEach-Object {
            $rel = $_.FullName.Substring($src.Length + 1).Replace('\', '/')
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip, $_.FullName, $rel, [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
        }
    }
    finally { $zip.Dispose() }

    $mb = [math]::Round((Get-Item $dst).Length / 1MB, 1)
    $takes = ((Get-Content (Join-Path $src "index.json") -Raw | ConvertFrom-Json).total)
    Write-Host "[pack-satire] done: $takes take(s) -> $dst ($mb MB)" -ForegroundColor Green
    Write-Host "Next: unzip into your Lovable project's public/satire-archive/ folder." -ForegroundColor Green
}
finally { Pop-Location }
