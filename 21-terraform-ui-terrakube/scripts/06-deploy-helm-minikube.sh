#!/usr/bin/env bash
# Deploy Terrakube Helm chart len minikube (lab 09)
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
NS="${TERRAKUBE_NS:-terrakube}"
RELEASE="${TERRAKUBE_RELEASE:-terrakube}"

command -v minikube >/dev/null || { echo "Can minikube"; exit 1; }
command -v helm >/dev/null || { echo "Can helm"; exit 1; }
command -v kubectl >/dev/null || { echo "Can kubectl"; exit 1; }

echo "=== Helm install Terrakube (minikube) ==="
minikube status || minikube start --cpus=4 --memory=8192

helm repo add terrakube-io https://terrakube-io.github.io/terrakube-helm-chart 2>/dev/null || true
helm repo update

kubectl create namespace "$NS" --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install "$RELEASE" terrakube-io/terrakube \
  -n "$NS" \
  -f "$ROOT/helm/values-minikube.yaml" \
  --wait --timeout 10m

echo ""
echo "=== Helm deploy xong ==="
helm status "$RELEASE" -n "$NS"
echo ""
echo "Truy cap (thu mot trong cac cach):"
echo "  kubectl get ingress -n $NS"
echo "  minikube service -n $NS --all"
echo "  minikube tunnel   # terminal rieng, roi mo https://terrakube.local"
echo ""
echo "Doc: docs/06-helm-minikube.md"
