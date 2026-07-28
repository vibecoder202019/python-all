#!/usr/bin/env bash
# Chạy tất cả ví dụ AWS tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

EXAMPLES=(
  "01_boto3_basics.py"
  "02_s3_operations.py"
  "03_ec2_basics.py"
  "04_iam_security.py"
  "05_cloudwatch.py"
  "06_generate_template.py"
)

echo "=== Chạy ví dụ AWS (Module 13) ==="
echo ""

for ex in "${EXAMPLES[@]}"; do
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "▶ $ex"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$MODULE_DIR/examples/$ex" || true
  echo ""
done

echo "✓ Hoàn thành! Tiếp: bash scripts/run_project.sh"
