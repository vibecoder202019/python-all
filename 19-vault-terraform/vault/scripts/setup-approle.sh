#!/usr/bin/env bash
# Enable AppRole + role myapp (can chay sau 02-setup-vault-dev.sh)
set -euo pipefail
export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
POLICY_DIR="$(dirname "$SCRIPT_DIR")/policies"

vault auth enable approle 2>/dev/null || true
vault policy write approle-app "$POLICY_DIR/approle-app.hcl"
vault write auth/approle/role/myapp \
  token_policies="approle-app" \
  token_ttl=1h \
  secret_id_ttl=10m

ROLE_ID=$(vault read -field=role_id auth/approle/role/myapp/role-id)
SECRET_ID=$(vault write -field=secret_id -f auth/approle/role/myapp/secret-id)

echo "Role ID:  $ROLE_ID"
echo "Secret ID: $SECRET_ID"
echo ""
echo "Login:"
echo "  vault write auth/approle/login role_id=$ROLE_ID secret_id=$SECRET_ID"
