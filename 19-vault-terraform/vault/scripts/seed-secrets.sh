#!/usr/bin/env bash
# Seed secret mau cho lab Terraform + Vault
set -euo pipefail
export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"

vault kv put secret/myapp/db \
  username=admin \
  password="lab-secret-$(date +%s)" \
  host=localhost \
  port=5432

echo "Secret da luu tai secret/myapp/db"
vault kv get secret/myapp/db
