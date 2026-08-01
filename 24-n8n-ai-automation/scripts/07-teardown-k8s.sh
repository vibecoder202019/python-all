#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
K8S_DIR="$MODULE_DIR/k8s-ai-automation"

echo "=== Teardown Module 24 — Kubernetes ==="
kubectl delete -f "$K8S_DIR/ingress.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/n8n-service.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/n8n-deployment.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/agent-bridge-service.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/agent-bridge-deployment.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/ollama-service.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/ollama-deployment.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/ollama-pvc.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/n8n-pvc.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/secret.yaml" --ignore-not-found
kubectl delete -f "$K8S_DIR/configmap.yaml" --ignore-not-found
kubectl delete namespace ai-automation --ignore-not-found
echo "✓ Đã gỡ stack ai-automation"
