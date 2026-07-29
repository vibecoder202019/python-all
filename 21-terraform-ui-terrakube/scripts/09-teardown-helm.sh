#!/usr/bin/env bash
# Go bo Helm release Terrakube tren minikube
set -euo pipefail
NS="${TERRAKUBE_NS:-terrakube}"
RELEASE="${TERRAKUBE_RELEASE:-terrakube}"
helm uninstall "$RELEASE" -n "$NS" 2>/dev/null || true
kubectl delete namespace "$NS" --ignore-not-found
echo "Da go Terrakube helm khoi minikube"
