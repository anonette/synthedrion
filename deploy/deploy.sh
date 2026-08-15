#!/usr/bin/env bash
# One-command deploy of the AI Cold War backend on a Debian/Ubuntu server.
# Idempotent: safe to re-run for updates (git pull + pip install + restart).
#
#   sudo bash deploy/deploy.sh
#
# Prereqs on the server:
#   - /opt/aicoldwar/.env must exist (secrets are NOT in the repo — scp it over:
#       scp .env askbot:/opt/aicoldwar/.env )
#   - a reverse proxy terminating TLS for aicoldwar.anonette.net -> 127.0.0.1:8600
#     (Caddy snippet in deploy/Caddyfile.snippet, nginx alternative below)
set -euo pipefail

REPO="https://github.com/anonette/synthedrion.git"
DIR="/opt/aicoldwar"
SVC="aicoldwar"

apt-get update -qq && apt-get install -y -qq git python3-venv python3-pip ffmpeg >/dev/null

id -u aicoldwar &>/dev/null || useradd --system --home "$DIR" --shell /usr/sbin/nologin aicoldwar

if [ ! -d "$DIR/.git" ]; then
  git clone "$REPO" "$DIR"
else
  git -C "$DIR" pull --ff-only
fi

cd "$DIR"
[ -d .venv ] || python3 -m venv .venv
./.venv/bin/pip install --quiet --upgrade pip
./.venv/bin/pip install --quiet -r requirements.txt

if [ ! -f "$DIR/.env" ]; then
  echo "!! $DIR/.env is missing — scp it from the laptop before starting:"
  echo "   scp C:/dev/AIcoldWar2026/.env <this-server>:$DIR/.env"
fi

# optional: bring the existing session archive along
#   scp C:/dev/AIcoldWar2026/sessions.db <this-server>:$DIR/sessions.db

chown -R aicoldwar:aicoldwar "$DIR"
cp deploy/aicoldwar.service /etc/systemd/system/$SVC.service
systemctl daemon-reload
systemctl enable "$SVC"
systemctl restart "$SVC"
sleep 2
systemctl --no-pager -l status "$SVC" | head -8
curl -s -m 5 http://127.0.0.1:8600/health && echo || echo "backend not answering yet — check: journalctl -u $SVC -n 50"

cat <<'EOF'

Reverse proxy (pick one):

  Caddy (auto-TLS) — append to /etc/caddy/Caddyfile and `systemctl reload caddy`:
      aicoldwar.anonette.net {
          reverse_proxy 127.0.0.1:8600
      }

  nginx + certbot:
      server {
          server_name aicoldwar.anonette.net;
          location / { proxy_pass http://127.0.0.1:8600; proxy_set_header Host $host; }
      }
      certbot --nginx -d aicoldwar.anonette.net

DNS is already set: aicoldwar.anonette.net -> this server (DNS-only, so TLS terminates here).
EOF
