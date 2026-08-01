#!/usr/bin/env bash
# Terraform AWX client — plan | apply | destroy
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TF_DIR="$SCRIPT_DIR/../terraform/awx-client"
ACTION="${1:-plan}"

[[ -d "$TF_DIR" ]] || { echo "Missing $TF_DIR"; exit 1; }

if [[ ! -f "$TF_DIR/terraform.tfvars" ]]; then
  echo "Tao terraform.tfvars tu example:"
  echo "  cp $TF_DIR/terraform.tfvars.example $TF_DIR/terraform.tfvars"
  exit 1
fi

cd "$TF_DIR"
terraform init -input=false

case "$ACTION" in
  plan)
    terraform plan -input=false
    ;;
  apply)
    terraform apply -input=false
    echo ""
    echo "Launch job (vi du):"
    echo "  awx job_templates launch \"python-script-demo-tf\" --monitor"
    ;;
  destroy)
    terraform destroy -input=false
    ;;
  *)
    echo "Usage: $0 [plan|apply|destroy]"
    exit 1
    ;;
esac
