#!/usr/bin/env bash
# Chạy dự án Catch the Stars — 6 bước tuần tự
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

STEPS=(
  "step01_window.py"
  "step02_player.py"
  "step03_stars.py"
  "step04_collision.py"
  "step05_score_lives.py"
  "step06_final.py"
)

echo "=== Dự án Catch the Stars — 6 bước ==="
echo ""

for i in "${!STEPS[@]}"; do
  step="${STEPS[$i]}"
  num=$((i + 1))
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "  Bước $num/6: $step"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  python "$MODULE_DIR/project/$step"
  echo ""
done

echo "🎉 Chúc mừng! Bạn đã hoàn thành game Catch the Stars!"
echo "   Game cuối cùng: project/step06_final.py"
