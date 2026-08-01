#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
echo "=== Module 24 setup ==="
command -v docker >/dev/null
cp -n "$MODULE_DIR/docker-compose/.env.example" "$MODULE_DIR/docker-compose/.env" 2>/dev/null || true
echo "✓ Ready — bash scripts/02-deploy-n8n-compose.sh"
