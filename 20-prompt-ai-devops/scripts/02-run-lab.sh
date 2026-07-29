#!/usr/bin/env bash
# Mở lab theo số 01-12
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01}"

find_lab() {
  find "$ROOT/labs" -name "lab${LAB}-*.md" 2>/dev/null | head -1
}

FILE=$(find_lab)
if [[ -z "$FILE" ]]; then
  echo "Lab $LAB không tìm thấy. Dùng 01-12."
  exit 1
fi
echo "=== Lab $LAB ==="
echo "File: $FILE"
echo ""
cat "$FILE"
