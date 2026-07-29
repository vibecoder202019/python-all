#!/usr/bin/env bash
# Module 17 — Deploy bằng Helm chart
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHART="$(dirname "$SCRIPT_DIR")/helm/go-task-api"
RELEASE="${RELEASE:-go-task-api}"
NS="${NS:-go-api-lab}"

echo "=== Deploy Helm chart ==="

# Tạo namespace nếu chưa có
kubectl create namespace "$NS" --dry-run=client -o yaml | kubectl apply -f -

# helm upgrade --install — cài mới hoặc upgrade nếu đã tồn tại
helm upgrade --install "$RELEASE" "$CHART" \
  --namespace "$NS" \
  --set image.repository="${IMAGE_REPO:-go-task-api}" \
  --set image.tag="${IMAGE_TAG:-latest}" \
  --set image.pullPolicy=IfNotPresent \
  --wait --timeout 120s

echo ""
echo "✅ Helm release: $RELEASE"
helm status "$RELEASE" -n "$NS"
echo ""
echo "Kiểm tra:"
echo "  kubectl get pods -n $NS"
echo "  curl http://go-api.local/health"
