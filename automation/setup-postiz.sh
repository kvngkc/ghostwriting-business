#!/usr/bin/env bash
# Downloads the official Postiz docker-compose setup and fills in your settings from .env.
# Postiz needs Postgres, Redis and Temporal; the official compose file runs all of them.
# Needs: docker with compose, git, and about 4 GB of RAM on the server.
set -euo pipefail
cd "$(dirname "$0")"

[ -f .env ] || { echo "Create .env from .env.example first."; exit 1; }
set -a; . ./.env; set +a
: "${POSTIZ_JWT_SECRET:?Set POSTIZ_JWT_SECRET in .env}"

if [ ! -d postiz ]; then
  git clone --depth 1 https://github.com/gitroomhq/postiz-docker-compose.git postiz
fi

f=postiz/docker-compose.yaml
url="${POSTIZ_URL:-http://localhost:4007}"
# Replace the defaults in the official file with your values.
sed -i.bak \
  -e "s|MAIN_URL: '.*'|MAIN_URL: '${url}'|" \
  -e "s|FRONTEND_URL: '.*'|FRONTEND_URL: '${url}'|" \
  -e "s|NEXT_PUBLIC_BACKEND_URL: '.*'|NEXT_PUBLIC_BACKEND_URL: '${url}/api'|" \
  -e "s|JWT_SECRET: '.*'|JWT_SECRET: '${POSTIZ_JWT_SECRET}'|" \
  -e "s|LINKEDIN_CLIENT_ID: '.*'|LINKEDIN_CLIENT_ID: '${LINKEDIN_CLIENT_ID:-}'|" \
  -e "s|LINKEDIN_CLIENT_SECRET: '.*'|LINKEDIN_CLIENT_SECRET: '${LINKEDIN_CLIENT_SECRET:-}'|" \
  "$f"

echo "Starting Postiz (first start takes a few minutes)..."
(cd postiz && docker compose up -d)
echo "Postiz: ${url}"
echo "After you create your account, set DISABLE_REGISTRATION to 'true' in $f and run: (cd postiz && docker compose up -d)"
