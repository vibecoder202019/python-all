#!/usr/bin/env bash
# Verify lab hoan thanh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01}"

export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"

pass() { echo "  PASS $1"; }
fail() { echo "  FAIL $1"; exit 1; }

case "$LAB" in
  01)
    [[ -f "$ROOT/terraform/01-hello/output/hello.txt" ]] && pass "hello.txt ton tai" || fail "chua apply 01-hello"
    ;;
  02)
    ls "$ROOT/terraform/02-variables/output/"*.json &>/dev/null && pass "config json ton tai" || fail "chua apply 02-variables"
    ;;
  07|08)
    vault kv get secret/myapp/db &>/dev/null && pass "secret myapp/db" || fail "chua seed secret"
    ;;
  11)
    [[ -f "$ROOT/terraform/05-vault-provider/output/.env.generated" ]] && pass ".env.generated" || fail "chua apply 05-vault-provider"
    ;;
  12)
    [[ -f "$ROOT/terraform/project/output/deployment-dev.yaml" ]] && pass "capstone manifest" || fail "chua apply project"
    ;;
  *)
    echo "Verify co san lab: 01, 02, 07, 08, 11, 12"
    echo "Usage: $0 <lab-number>"
    exit 1
    ;;
esac
echo "Lab $LAB OK"
