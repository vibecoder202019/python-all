#!/usr/bin/env bash
set -euo pipefail
echo "=== Prerequisites Module 24 ==="
docker --version
docker compose version
echo ""
echo "Module 23 Agent Bridge (khuyến nghị đang chạy :8090):"
curl -sf http://localhost:8090/health && echo " OK" || echo "  (chưa chạy — bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh)"
echo ""
echo "Module 15 AWX (tùy chọn):"
kubectl get pods -n awx 2>/dev/null | head -3 || echo "  (chưa deploy AWX — dùng AWX_DEMO_MODE=1 trên bridge)"
