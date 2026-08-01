#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate"
set -a
[ -f "$MODULE_DIR/config/.env" ] && source "$MODULE_DIR/config/.env"
set +a

PORT="${BRIDGE_PORT:-8090}"
echo "=== Agent Bridge API on :$PORT ==="
echo "Docs: http://localhost:$PORT/docs"
cd "$MODULE_DIR"
exec uvicorn agent-bridge.main:app --host 0.0.0.0 --port "$PORT" --reload
