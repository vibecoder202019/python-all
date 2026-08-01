#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"

echo "=== Kiểm tra prerequisites Module 23 ==="
python3 --version
command -v uvicorn >/dev/null || pip install -q uvicorn 2>/dev/null || true

echo -n "mcp package: "
python3 -c "import mcp; print('OK')" 2>/dev/null || echo "MISSING — bash scripts/setup.sh"

echo ""
echo "AWX (Module 15 — khuyến nghị đã deploy):"
if kubectl get pods -n awx &>/dev/null; then
  kubectl get pods -n awx 2>/dev/null | head -5 || true
else
  echo "  (chưa có namespace awx — dùng AWX_DEMO_MODE=1 để học không cần cluster)"
fi

echo ""
echo "Env gợi ý:"
echo "  export AWX_URL=http://localhost:8052"
echo "  export AWX_TOKEN=your-token"
echo "  export BRIDGE_API_KEY=lab-bridge-key"
echo "  export AWX_DEMO_MODE=1   # học không cần AWX"
