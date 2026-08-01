#!/usr/bin/env bash
# Demo AWX CLI — launch job template (can AWX_HOST + AWX_TOKEN)
set -euo pipefail

TEMPLATE_NAME="${1:-python-script-demo-tf}"

: "${AWX_HOST:?export AWX_HOST=http://localhost:8052}"
: "${AWX_TOKEN:?export AWX_TOKEN=...}"

export AWX_VERIFY_SSL="${AWX_VERIFY_SSL:-false}"

echo "=== AWX CLI demo: launch $TEMPLATE_NAME ==="
awx ping
echo ""
awx job_templates list -f json | jq -r '.results[] | "\(.id)\t\(.name)"' | head -20
echo ""
echo "Launching..."
awx job_templates launch "$TEMPLATE_NAME" --extra_vars '{"demo_mode": true}' --monitor
