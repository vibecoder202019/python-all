#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate"
set -a
[ -f "$MODULE_DIR/config/.env" ] && source "$MODULE_DIR/config/.env"
set +a

export AWX_DEMO_MODE="${AWX_DEMO_MODE:-1}"
export BRIDGE_URL="${BRIDGE_URL:-http://localhost:8090}"

echo "=== Test AWX tools (demo) ==="
python "$MODULE_DIR/examples/01_test_awx_tools.py" --demo

echo ""
echo "=== Test bridge (cần bridge đang chạy) ==="
python "$MODULE_DIR/examples/02_call_bridge_api.py" --intent list_templates 2>/dev/null || \
  echo "(Bỏ qua nếu bridge chưa chạy — bash scripts/04-run-agent-bridge.sh)"
