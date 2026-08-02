#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
EX="$MODULE_DIR/examples"

cd "$ROOT_DIR"
# shellcheck disable=SC1091
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo "=== Run all Module 25 examples ==="
for f in 01_phishing_url_analyzer.py 02_email_header_red_flags.py 03_security_headers_check.py \
         04_owasp_input_sanitizer.py 05_seo_integrity_audit.py 06_search_penalty_triage.py; do
  echo ""
  python3 "$EX/$f"
done
echo ""
echo "✓ All examples done"
