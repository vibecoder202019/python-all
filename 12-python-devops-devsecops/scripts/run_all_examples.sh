#!/usr/bin/env bash
# Chạy TẤT CẢ ví dụ DevOps tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

EXAMPLES=(
  "01_subprocess_bash.py"
  "02_pathlib_config.py"
  "03_log_analyzer.py"
  "04_health_check.py"
  "05_docker_script.py"
  "06_security_scan.py"
)

echo "=== Chạy tất cả ví dụ DevOps (Module 12) ==="
echo ""

for ex in "${EXAMPLES[@]}"; do
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "▶ $ex"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$MODULE_DIR/examples/$ex"
  echo ""
done

echo "✓ Hoàn thành! Tiếp: bash scripts/run_project.sh"
