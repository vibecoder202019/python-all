#!/usr/bin/env bash
# Chạy MCP server (stdio) — Cursor/Claude Desktop sẽ spawn process này
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate"
set -a
[ -f "$MODULE_DIR/config/.env" ] && source "$MODULE_DIR/config/.env"
set +a

echo "Starting AWX MCP server (stdio)..." >&2
exec python "$MODULE_DIR/mcp-server/awx_mcp_server.py"
