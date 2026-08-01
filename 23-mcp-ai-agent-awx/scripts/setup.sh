#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 23: Setup MCP + Agent Bridge ==="
cd "$ROOT_DIR"
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r "$MODULE_DIR/mcp-server/requirements.txt"
pip install -q -r "$MODULE_DIR/agent-bridge/requirements.txt"
pip install -q httpx

cp -n "$MODULE_DIR/config/.env.example" "$MODULE_DIR/config/.env" 2>/dev/null || true

echo "✓ Dependencies installed"
echo ""
echo "Tiếp theo:"
echo "  bash 23-mcp-ai-agent-awx/scripts/01-check-prerequisites.sh"
echo "  AWX_DEMO_MODE=1 python 23-mcp-ai-agent-awx/examples/01_test_awx_tools.py --demo"
