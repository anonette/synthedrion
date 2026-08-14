# Deploying the backend to a persistent server

Target: the anonette.net server (`95.216.199.241`, the machine behind `ssh askbot`),
subdomain **aicoldwar.anonette.net** (DNS A record already created, DNS-only).

## For whoever has SSH access (three steps)

```bash
ssh askbot
sudo git clone https://github.com/anonette/synthedrion.git /opt/aicoldwar   # first time only
sudo bash /opt/aicoldwar/deploy/deploy.sh
```

Then two one-time items:

1. **Secrets** — the repo has no `.env` (by design). Copy it from Denisa's laptop:
   `scp C:/dev/AIcoldWar2026/.env askbot:/opt/aicoldwar/.env` and re-run the deploy
   script (or `sudo systemctl restart aicoldwar`).
2. **TLS/proxy** — add the Caddy or nginx snippet the script prints, pointing
   `aicoldwar.anonette.net` at `127.0.0.1:8600`.

Optionally migrate the existing session archive:
`scp C:/dev/AIcoldWar2026/sessions.db askbot:/opt/aicoldwar/sessions.db` (then restart).

## Updating later

`sudo bash /opt/aicoldwar/deploy/deploy.sh` — pulls main, reinstalls deps, restarts.

## After it is live

- Verify: `https://aicoldwar.anonette.net/health` returns JSON with `openrouter_enabled: true`.
- Tell Lovable to switch its API base URL from `https://aicoldwar.ngrok.app` to
  `https://aicoldwar.anonette.net` (no `ngrok-skip-browser-warning` header needed anymore).
- The laptop + ngrok setup keeps working independently; the server copy is the
  persistent one. Do not run both against the same expectations of "the live session" —
  each has its own database unless sessions.db was migrated.
