#!/usr/bin/env bash
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "=== Teardown Module 28 lab resources ==="
if command -v kubectl >/dev/null && kubectl cluster-info >/dev/null 2>&1; then
  kubectl delete -f "$MODULE_DIR/k8s/demo-app.yaml" --ignore-not-found
  kubectl delete ns platform-apps --ignore-not-found --wait=false || true
fi
if [[ -d "$MODULE_DIR/terraform/.terraform" ]]; then
  (cd "$MODULE_DIR/terraform" && terraform destroy -auto-approve) || true
fi
rm -f "$MODULE_DIR/data/generated-catalog.yaml" "$MODULE_DIR/terraform/tfplan"
echo "✓ Done (Bridge process: Ctrl+C nếu đang chạy)"
