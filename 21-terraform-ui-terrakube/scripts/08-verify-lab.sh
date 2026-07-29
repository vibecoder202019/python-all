#!/usr/bin/env bash
# Verify lab Module 21
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01}"
URL="${TERRAKUBE_UI_URL:-https://terrakube.platform.local}"

pass() { echo "  PASS $1"; }
fail() { echo "  FAIL $1"; exit 1; }

case "$LAB" in
  01|02)
    code=$(curl -sk -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null || echo 000)
    [[ "$code" =~ ^(200|301|302)$ ]] && pass "UI $URL ($code)" || fail "UI chua san sang"
    ;;
  04|05)
    echo "Verify tay tren UI: workspace co run Apply thanh cong + tab States"
    pass "(manual) xem lab 04 checklist"
    ;;
  *)
    echo "Auto verify: lab 01, 02. Lab khac: verify tay theo file lab."
    exit 0
    ;;
esac
echo "Lab $LAB OK"
