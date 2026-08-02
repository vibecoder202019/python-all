#!/usr/bin/env bash
# Smoke-test Bridge API (demo) — chạy khi bridge đang listen :8090
set -euo pipefail
BASE="${BRIDGE_URL:-http://127.0.0.1:8090}"
KEY="${BRIDGE_API_KEY:-dev-bridge-key-change-me}"
HDR=(-H "Content-Type: application/json" -H "X-API-Key: $KEY")

echo "health:"; curl -sf "$BASE/health" | python3 -m json.tool
echo "templates:"; curl -sf "${HDR[@]}" "$BASE/api/v1/templates" | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d["count"], "templates")'
echo "create job:"; curl -sf "${HDR[@]}" -X POST "$BASE/api/v1/jobs" \
  -d '{"template_id":7,"extra_vars":{"app_name":"api-from-curl","replicas":2}}' | python3 -m json.tool
echo "deploy:"; curl -sf "${HDR[@]}" -X POST "$BASE/api/v1/deploy" \
  -d '{"app_name":"checkout","namespace":"platform-apps","image":"nginx:1.27-alpine","replicas":2}' \
  | python3 -m json.tool
echo "✓ Bridge API OK"
