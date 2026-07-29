#!/usr/bin/env bash
set -euo pipefail
ENV="${1:-management}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="$ROOT/terraform/environments/$ENV"
[[ -d "$DIR" ]] || { echo "Unknown env: $ENV"; exit 1; }
cd "$DIR"
terraform init -input=false
terraform fmt -check -recursive 2>/dev/null || terraform fmt
terraform validate
terraform plan -input=false
echo "Apply: cd $DIR && terraform apply"
