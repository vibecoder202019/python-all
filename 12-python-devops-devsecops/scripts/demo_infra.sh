#!/usr/bin/env bash
# Demo môi trường infra giả lập — chạy 1 lần để test health check
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

echo "=== Demo Infrastructure ==="
echo ""

echo "1. Disk usage:"
python "$MODULE_DIR/project/step06_final.py" disk-usage --path "$MODULE_DIR" 2>/dev/null || \
  python "$MODULE_DIR/examples/02_pathlib_config.py"

echo ""
echo "2. Log analysis:"
python "$MODULE_DIR/project/step06_final.py" parse-log --file "$MODULE_DIR/data/sample.log" 2>/dev/null || \
  python "$MODULE_DIR/examples/03_log_analyzer.py"

echo ""
echo "3. Security scan:"
python "$MODULE_DIR/project/step06_final.py" security-scan --path "$MODULE_DIR/data/" 2>/dev/null || \
  python "$MODULE_DIR/examples/06_security_scan.py"

echo ""
echo "✓ Demo hoàn tất!"
