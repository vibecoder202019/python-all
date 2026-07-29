#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01}"
F=$(find "$ROOT/labs" -name "lab${LAB}-*.md" | head -1)
[[ -n "$F" ]] && cat "$F" || { echo "Lab $LAB not found"; exit 1; }
