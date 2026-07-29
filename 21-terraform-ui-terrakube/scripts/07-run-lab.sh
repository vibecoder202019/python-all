#!/usr/bin/env bash
# Mo huong dan lab 01-10
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01}"
FILE=$(find "$ROOT/labs" -name "lab${LAB}-*.md" 2>/dev/null | head -1)
if [[ -z "$FILE" ]]; then
  echo "Lab $LAB khong tim thay (01-10)"
  exit 1
fi
echo "=== Lab $LAB ==="
cat "$FILE"
