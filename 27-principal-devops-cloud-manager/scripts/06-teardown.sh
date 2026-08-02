#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
# Giữ templates; xóa output lab nếu user muốn reset
rm -f "$MODULE_DIR/portfolio/governance-scorecard.json" \
      "$MODULE_DIR/portfolio/finops-summary.json"
echo "✓ Cleared generated JSON in portfolio/ (Markdown giữ nguyên — tự xóa nếu cần)"
