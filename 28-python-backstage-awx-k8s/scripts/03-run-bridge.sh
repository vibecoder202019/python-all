#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck disable=SC1091
[[ -f "$MODULE_DIR/data/.env" ]] && set -a && source "$MODULE_DIR/data/.env" && set +a
export AWX_DEMO="${AWX_DEMO:-true}"
export BRIDGE_API_KEY="${BRIDGE_API_KEY:-dev-bridge-key-change-me}"
HOST="${BRIDGE_HOST:-127.0.0.1}"
PORT="${BRIDGE_PORT:-8090}"

echo "=== Module 28 Platform Bridge ==="
echo "  demo=$AWX_DEMO  http://$HOST:$PORT"
echo "  Docs: http://$HOST:$PORT/docs"
cd "$MODULE_DIR/project"
exec python3 -m uvicorn bridge_server:app --host "$HOST" --port "$PORT"
