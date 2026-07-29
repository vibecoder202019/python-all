#!/usr/bin/env bash
# Module 16 — Setup
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
ROOT_DIR="$(dirname "$MODULE_DIR")"
cd "$ROOT_DIR"
[ ! -d ".venv" ] && python3 -m venv .venv
source .venv/bin/activate
pip install -q --upgrade pip
pip install -q fastapi uvicorn pyyaml httpx
mkdir -p "$MODULE_DIR/data"
cat > "$MODULE_DIR/data/phishing_urls.txt" << 'EOF'
https://github.com/login
https://paypal-secure-update.xyz/confirm-password
http://192.168.1.1/login-verify
https://google.com@evil.tk/steal
EOF
cat > "$MODULE_DIR/data/sqli_payloads.txt" << 'EOF'
admin
' OR '1'='1
'; DROP TABLE users; --
1 UNION SELECT password FROM users
normal search query
EOF
echo "✓ Module 16 setup done"
echo "  bash 16-k8s-security/scripts/run_all_examples.sh"
