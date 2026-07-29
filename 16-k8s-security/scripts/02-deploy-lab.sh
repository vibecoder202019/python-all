#!/usr/bin/env bash
# Module 16 — Deploy security lab lên K8s
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
K8S_DIR="$(dirname "$SCRIPT_DIR")/k8s"

echo "=== Deploy Security Lab ==="
for f in namespace.yaml configmap-app.yaml deployment.yaml service.yaml \
         networkpolicy.yaml ingress-secure.yaml hpa.yaml; do
  echo "▶ Applying $f..."
  kubectl apply -f "$K8S_DIR/$f"
done

echo "Chờ pod Ready..."
kubectl wait --for=condition=ready pod -l app=secure-api \
  -n security-lab --timeout=180s || true

echo ""
echo "✅ Deploy xong!"
echo "  Thêm /etc/hosts: 127.0.0.1 secure-api.local"
echo "  Test: bash scripts/03-test-attacks.sh"
