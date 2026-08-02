#!/usr/bin/env bash
# Deploy demo app thẳng lên cluster (bỏ qua AWX) — để verify K8s manifests.
set -euo pipefail
MODULE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
command -v kubectl >/dev/null || { echo "Cần kubectl + cluster"; exit 1; }
kubectl cluster-info >/dev/null
kubectl apply -f "$MODULE_DIR/k8s/demo-app.yaml"
kubectl rollout status deploy/demo-api -n platform-apps --timeout=120s
kubectl get deploy,svc,pods -n platform-apps
echo "✓ K8s demo-app deployed"
echo "  Port-forward: kubectl -n platform-apps port-forward svc/demo-api 8088:80"
