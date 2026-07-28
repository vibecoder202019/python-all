#!/usr/bin/env bash
# Chạy demo nhanh cả 2 module mới (Game + DevOps)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

source .venv/bin/activate 2>/dev/null || {
  echo "Chưa setup. Chạy: bash scripts/setup.sh"
  exit 1
}

echo "╔══════════════════════════════════════════╗"
echo "║  Demo Module 11 + 12                     ║"
echo "╚══════════════════════════════════════════╝"

echo ""
echo "▶ Module 11: Game (chạy project cuối cùng)..."
python 11-python-game-tre-em/project/step06_final.py &
GAME_PID=$!
sleep 3
kill $GAME_PID 2>/dev/null || true

echo ""
echo "▶ Module 12: DevOps Toolkit..."
python 12-python-devops-devsecops/project/step06_final.py --demo

echo ""
echo "✅ Demo hoàn tất!"
