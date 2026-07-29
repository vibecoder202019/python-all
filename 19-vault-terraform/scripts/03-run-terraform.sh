#!/usr/bin/env bash
# Chay terraform example: 01-hello | 02-variables | ... | project
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LAB="${1:-01-hello}"
AUTO="${AUTO_APPROVE:-}"

case "$LAB" in
  01-hello)           DIR="$ROOT/terraform/01-hello" ;;
  02-variables)       DIR="$ROOT/terraform/02-variables" ;;
  03-local-resources) DIR="$ROOT/terraform/03-local-resources" ;;
  04-modules)         DIR="$ROOT/terraform/04-modules" ;;
  05-vault-provider)  DIR="$ROOT/terraform/05-vault-provider" ;;
  project)            DIR="$ROOT/terraform/project" ;;
  *)
    echo "Lab khong ton tai: $LAB"
    echo "Usage: $0 [01-hello|02-variables|03-local-resources|04-modules|05-vault-provider|project]"
    exit 1
    ;;
esac

mkdir -p "$DIR/output" 2>/dev/null || true

if [[ "$LAB" == "05-vault-provider" || "$LAB" == "project" ]]; then
  export VAULT_ADDR="${VAULT_ADDR:-http://127.0.0.1:8200}"
  export VAULT_TOKEN="${VAULT_TOKEN:-root}"
  if ! vault status &>/dev/null; then
    echo "Can Vault dang chay. Terminal khac: bash scripts/02-setup-vault-dev.sh"
    exit 1
  fi
  bash "$ROOT/vault/scripts/seed-secrets.sh" 2>/dev/null || true
fi

echo "=== Terraform: $LAB ==="
cd "$DIR"
terraform init -input=false
terraform fmt -check -recursive 2>/dev/null || terraform fmt
terraform validate
terraform plan -input=false

if [[ "$AUTO" == "yes" || "$2" == "--auto" ]]; then
  terraform apply -input=false -auto-approve
  terraform output
else
  echo ""
  echo "Apply thu cong: cd $DIR && terraform apply"
fi
