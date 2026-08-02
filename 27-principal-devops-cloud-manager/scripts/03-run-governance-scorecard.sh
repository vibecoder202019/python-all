#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
OUT="$MODULE_DIR/portfolio/governance-scorecard.json"
mkdir -p "$MODULE_DIR/portfolio"
python3 "$MODULE_DIR/project/governance_scorecard.py" \
  -i "$MODULE_DIR/data/governance_fixture.json" \
  -o "$OUT"
