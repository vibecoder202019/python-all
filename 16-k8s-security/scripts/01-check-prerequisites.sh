#!/usr/bin/env bash
# Kiểm tra môi trường K8s cho module security
set -euo pipefail
echo "=== Module 16: Prerequisites ==="
kubectl get nodes &>/dev/null && echo "✅ K8s cluster" || echo "❌ K8s chưa sẵn sàng"
kubectl get pods -n ingress-nginx &>/dev/null && echo "✅ Ingress controller" || echo "⚠️  Cần cài NGINX Ingress"
python3 -c "import fastapi" 2>/dev/null && echo "✅ fastapi" || echo "⚠️  bash scripts/setup.sh"
