#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
cd "$ROOT_DIR" && source .venv/bin/activate 2>/dev/null || true

echo "=== Module 16: Examples ==="
for f in 01_detect_sql_injection 02_rate_limiter 03_phishing_url_checker \
         04_port_scan_detector 06_k8s_security_scanner; do
  echo "▶ $f"
  python "$MODULE_DIR/examples/${f}.py" $([ "$1" = "--demo" ] && echo --demo)
  echo ""
done
echo "▶ 05_waf_middleware (info only — chạy riêng: uvicorn ...)"
python -c "print('  uvicorn 16-k8s-security.examples.05_waf_middleware:app --port 8080')"
