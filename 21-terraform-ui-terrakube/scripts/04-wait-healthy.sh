#!/usr/bin/env bash
# Doi Terrakube UI tra loi HTTPS
set -euo pipefail

URL="${TERRAKUBE_UI_URL:-https://terrakube.platform.local}"
MAX="${MAX_WAIT:-120}"
INTERVAL=5
elapsed=0

echo "Doi Terrakube tai $URL (max ${MAX}s)..."

while [[ $elapsed -lt $MAX ]]; do
  code=$(curl -sk -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null || echo "000")
  if [[ "$code" =~ ^(200|301|302|303)$ ]]; then
    echo "Terrakube UI san sang (HTTP $code)"
    exit 0
  fi
  echo "  ... chua san sang ($code) — ${elapsed}s"
  sleep "$INTERVAL"
  elapsed=$((elapsed + INTERVAL))
done

echo "Timeout — kiem tra: docker ps | grep -i terra"
echo "Logs: cd .cache/terrakube-upstream/docker-compose && docker compose logs --tail=50"
exit 1
