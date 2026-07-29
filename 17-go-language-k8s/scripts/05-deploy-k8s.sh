#!/usr/bin/env bash
# Module 17 — Deploy bằng manifest K8s thuần
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
K8S="$(dirname "$SCRIPT_DIR")/k8s"

echo "=== Deploy K8s (raw manifests) ==="
kubectl apply -f "$K8S/namespace.yaml"
kubectl apply -f "$K8S/deployment.yaml"
kubectl apply -f "$K8S/service.yaml"
kubectl apply -f "$K8S/ingress.yaml"

kubectl wait --for=condition=ready pod -l app=go-task-api \
  -n go-api-lab --timeout=120s || true

echo "✅ http://go-api.local (thêm /etc/hosts: 127.0.0.1 go-api.local)"
