#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TF_DIR="$MODULE_DIR/terraform"
AUTO=0
[[ "${1:-}" == "--auto" ]] && AUTO=1

command -v terraform >/dev/null || { echo "Cần terraform"; exit 1; }
cd "$TF_DIR"
[[ -f terraform.tfvars ]] || cp terraform.tfvars.example terraform.tfvars
terraform init -upgrade
terraform plan -out=tfplan
if [[ "$AUTO" -eq 1 ]]; then
  terraform apply tfplan
  terraform output
else
  echo "Plan OK. Apply: bash scripts/04-terraform-plan.sh --auto"
fi
