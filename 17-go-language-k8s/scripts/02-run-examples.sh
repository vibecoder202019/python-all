#!/usr/bin/env bash
# Module 17 — Chạy tất cả examples Go
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE="$(dirname "$SCRIPT_DIR")"
EXAMPLES="$MODULE/examples"

echo "=== Module 17: Go Examples ==="
cd "$MODULE"
for dir in "$EXAMPLES"/0*/; do
  name=$(basename "$dir")
  echo "────────────────────────────────────────"
  echo "▶ $name"
  echo "────────────────────────────────────────"
  if [ "$name" = "06_http_json" ] && [ "${1:-}" != "--with-server" ]; then
    echo "  (bỏ qua — chạy riêng: go run ./examples/06_http_json/)"
    continue
  fi
  if [ "$name" = "06_http_json" ]; then
    timeout 2 go run "./examples/$name/" || true
  else
    go run "./examples/$name/"
  fi
  echo ""
done
echo "✅ Hoàn tất examples"
