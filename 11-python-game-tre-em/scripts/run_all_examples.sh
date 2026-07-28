#!/usr/bin/env bash
# Chạy TẤT CẢ ví dụ module 11 lần lượt (mỗi game tự đóng sau vài giây hoặc ESC)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

source "$ROOT_DIR/.venv/bin/activate" 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

EXAMPLES=(
  "01_cua_so_va_mau.py"
  "02_hinh_va_text.py"
  "03_ban_phim_chuot.py"
  "04_sprite_va_anh.py"
  "05_va_cham_diem.py"
  "06_game_snake.py"
)

echo "=== Chạy tất cả ví dụ Game (Module 11) ==="
echo "Nhấn ESC hoặc đóng cửa sổ để chuyển ví dụ tiếp theo."
echo ""

for ex in "${EXAMPLES[@]}"; do
  echo "▶ Running: $ex"
  python "$MODULE_DIR/examples/$ex" || true
  sleep 1
done

echo ""
echo "✓ Hoàn thành tất cả ví dụ!"
echo "Tiếp theo: bash scripts/run_project.sh"
