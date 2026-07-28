#!/usr/bin/env bash
# Setup toàn bộ repo learn-python-ai (chạy 1 lần)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "╔══════════════════════════════════════════╗"
echo "║  Learn Python AI — Full Setup            ║"
echo "╚══════════════════════════════════════════╝"

python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt

chmod +x scripts/*.sh
chmod +x 11-python-game-tre-em/scripts/*.sh
chmod +x 12-python-devops-devsecops/scripts/*.sh

bash 12-python-devops-devsecops/scripts/setup.sh

echo ""
echo "✅ Setup hoàn tất!"
echo ""
echo "Chạy module Game:"
echo "  bash 11-python-game-tre-em/scripts/run_all_examples.sh"
echo "  bash 11-python-game-tre-em/scripts/run_project.sh"
echo ""
echo "Chạy module DevOps:"
echo "  bash 12-python-devops-devsecops/scripts/run_all_examples.sh"
echo "  bash 12-python-devops-devsecops/scripts/run_project.sh"
