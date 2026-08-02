#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
rm -f "$MODULE_DIR/data/last_audit_report.json"
echo "✓ Removed generated report (fixtures giữ nguyên)"
