#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

cd "$MODULE_DIR"
echo "Dừng PostgreSQL container..."
docker compose down
echo "✓ Done. Data volume giữ lại — xóa hẳn: docker compose down -v"
