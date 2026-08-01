#!/usr/bin/env bash
set -euo pipefail
# Test capstone webhook — cần workflow 04 active trên n8n
WEBHOOK="${N8N_WEBHOOK_URL:-http://localhost:5678/webhook/awx-run}"

echo "POST $WEBHOOK"
curl -s -X POST "$WEBHOOK" \
  -H "Content-Type: application/json" \
  -u admin:n8n-lab-pass \
  -d '{"template_name":"Python Hello World","extra_vars":{"user_name":"capstone"}}' | jq . 2>/dev/null || cat

echo ""
echo "Nếu 404: import workflows/04-capstone-ai-ops.json và Activate workflow trên n8n UI"
