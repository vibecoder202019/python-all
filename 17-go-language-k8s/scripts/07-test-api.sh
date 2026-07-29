#!/usr/bin/env bash
# Module 17 — Test API endpoints
set -euo pipefail
BASE="${BASE_URL:-http://localhost:8080}"

echo "=== Test Go Task API @ $BASE ==="
curl -sf "$BASE/health" | python3 -m json.tool && echo "✅ health" || echo "❌ health"
curl -sf -X POST "$BASE/tasks" -H "Content-Type: application/json" \
  -d '{"title":"Task từ script test"}' | python3 -m json.tool && echo "✅ create" || echo "❌ create"
curl -sf "$BASE/tasks" | python3 -m json.tool && echo "✅ list" || echo "❌ list"
