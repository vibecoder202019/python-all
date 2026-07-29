#!/usr/bin/env bash
# Goi y dap an — chi xem sau khi tu lam
set -euo pipefail

# 1. cd terraform/01-hello && terraform init && terraform apply
# 2. terraform apply -var="region=ap-southeast-1"  # them variable trong main.tf truoc
# 6. vault kv put secret/demo/api-key value=abc123
# 7. vault policy write demo-read - <<EOF
# path "secret/data/demo/*" { capabilities = ["read"] }
# EOF
# 11.
export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
export VAULT_TOKEN="${VAULT_TOKEN:-root}"
# vault kv put secret/myapp/db username=u password=p
# AUTO_APPROVE=yes bash scripts/03-run-terraform.sh 05-vault-provider --auto
echo "Xem lab 01-12 va docs/ cho dap an chi tiet"
