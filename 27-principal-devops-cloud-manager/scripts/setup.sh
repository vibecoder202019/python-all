#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
echo "=== Module 27 setup ==="
mkdir -p "$MODULE_DIR/portfolio" "$MODULE_DIR/reports"
python3 -c "import json; print('stdlib OK')"
echo "✓ Ready"
echo "  bash 27-principal-devops-cloud-manager/scripts/02-init-portfolio.sh"
echo "  bash 27-principal-devops-cloud-manager/scripts/03-run-governance-scorecard.sh"
