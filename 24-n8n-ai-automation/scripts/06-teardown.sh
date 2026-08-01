#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

cd "$MODULE_DIR/docker-compose"
docker compose down
echo "✓ n8n stopped (volume giữ data — xóa: docker compose down -v)"
