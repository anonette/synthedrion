# Publish the satire bundle to the public GitHub Pages repo (anonette/synthedrion-satire),
# which serves it at https://www.anonette.net/synthedrion-satire/ for Lovable.
#
# Usage (from the project root, with the backend running):
#   powershell -File scripts/publish-satire.ps1
#   $env:ROUNDTABLE_BASE_URL="https://aicoldwar.ngrok.app"; powershell -File scripts/publish-satire.ps1
$ErrorActionPreference = "Stop"
$root  = Split-Path -Parent $PSScriptRoot
$clone = "C:\dev\synthedrion-satire"
if (-not (Test-Path (Join-Path $clone ".git"))) {
    throw "Pages repo clone not found at $clone. Re-clone it: git clone https://github.com/anonette/synthedrion-satire $clone"
}
Push-Location $root
try {
    Write-Host "[publish] regenerating bundle..." -ForegroundColor Cyan
    node scripts/snapshot-satire.mjs
    if ($LASTEXITCODE -ne 0) { throw "snapshot-satire.mjs failed (is the backend running?)" }
    $src = Join-Path $root "public\satire-archive"
    if (-not (Test-Path (Join-Path $src "index.json"))) { throw "no bundle at $src" }

    # Sync bundle into the clone, preserving repo plumbing.
    Get-ChildItem $clone -Force | Where-Object { $_.Name -notin @('.git', '.nojekyll', 'README.md') } | Remove-Item -Recurse -Force
    Copy-Item -Path (Join-Path $src '*') -Destination $clone -Recurse -Force

    Push-Location $clone
    try {
        git add -A
        if (-not (git status --porcelain)) { Write-Host "[publish] no changes to publish." -ForegroundColor Yellow; return }
        git -c user.name="dk" -c user.email="denisa.kera@gmail.com" commit -q -m "update satire archive"
        git push -q origin main
        Write-Host "[publish] pushed. Live in ~30s: https://www.anonette.net/synthedrion-satire/" -ForegroundColor Green
    }
    finally { Pop-Location }
}
finally { Pop-Location }
