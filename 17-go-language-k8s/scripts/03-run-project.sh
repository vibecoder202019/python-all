#!/usr/bin/env bash
# Module 17 — Build, test, chạy Task API
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT="$(dirname "$SCRIPT_DIR")/project"
cd "$PROJECT"

echo "=== Module 17: Go Task API ==="
echo "[1/3] go test ./..."
go test ./...

echo "[2/3] go build..."
go build -o bin/server ./cmd/server
echo "  Binary: project/bin/server"

echo "[3/3] Chạy server (Ctrl+C để dừng)..."
echo "  curl http://localhost:8080/health"
echo "  curl -X POST http://localhost:8080/tasks -d '{\"title\":\"Học Go\"}' -H 'Content-Type: application/json'"
if [ "${1:-}" = "--run" ]; then
  ./bin/server
fi
