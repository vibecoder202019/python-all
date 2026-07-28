#!/usr/bin/env bash
# Chạy dự án DevOps Toolkit — 6 bước tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

STEPS=(
  "step01_cli_skeleton.py"
  "step02_file_ops.py"
  "step03_log_parser.py"
  "step04_health_monitor.py"
  "step05_security_audit.py"
  "step06_final.py"
)

echo "=== Dự án DevOps Toolkit — 6 bước ==="
echo ""

for i in "${!STEPS[@]}"; do
  step="${STEPS[$i]}"
  num=$((i + 1))
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  Bước $num/6: $step"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$MODULE_DIR/project/$step" --demo 2>/dev/null || python "$MODULE_DIR/project/$step"
  echo ""
done

echo "🎉 DevOps Toolkit hoàn chỉnh!"
echo ""
echo "Dùng CLI:"
echo "  python project/step06_final.py --help"
echo "  python project/step06_final.py disk-usage --path ."
echo "  python project/step06_final.py parse-log --file data/sample.log"
echo "  python project/step06_final.py security-scan --path data/"
