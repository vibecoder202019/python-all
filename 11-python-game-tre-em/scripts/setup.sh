#!/usr/bin/env bash
# Module 11 — Cài môi trường game (chạy 1 lần)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"

echo "=== Module 11: Setup Game Environment ==="

cd "$ROOT_DIR"
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install -q --upgrade pip
pip install -q pygame

echo "✓ Pygame installed: $(python -c 'import pygame; print(pygame.ver)')"
echo ""
echo "Chạy tiếp:"
echo "  bash 11-python-game-tre-em/scripts/run_all_examples.sh"
echo "  bash 11-python-game-tre-em/scripts/run_project.sh"
