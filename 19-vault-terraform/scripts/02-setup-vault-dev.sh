#!/usr/bin/env bash
# Khoi dong Vault dev mode + enable KV v2 + seed secret mau
# Chay terminal rieng — process chay foreground
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"

if vault status &>/dev/null; then
  echo "Vault da chay tai $VAULT_ADDR"
  bash "$ROOT/vault/scripts/seed-secrets.sh" 2>/dev/null || true
  exit 0
fi

echo "=== Vault Dev Mode (CHI lab) ==="
echo "VAULT_ADDR=$VAULT_ADDR"
echo "Root token: root"
echo ""
echo "Sau khi server khoi dong, mo terminal khac:"
echo "  export VAULT_ADDR='$VAULT_ADDR'"
echo "  export VAULT_TOKEN='root'"
echo "  bash $ROOT/vault/scripts/seed-secrets.sh"
echo ""

# Enable KV + seed trong background sau 3s
(
  sleep 3
  export VAULT_ADDR VAULT_TOKEN
  vault secrets enable -path=secret kv-v2 2>/dev/null || true
  bash "$ROOT/vault/scripts/seed-secrets.sh" 2>/dev/null || true
) &

exec vault server -dev -dev-root-token-id=root -dev-listen-address=127.0.0.1:8200
