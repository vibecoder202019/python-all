#!/usr/bin/env bash
# Setup cluster lab CKA/CKS
set -euo pipefail
echo "=== Module 18: Setup CKA/CKS Lab ==="

if command -v minikube &>/dev/null; then
  echo "Khởi động minikube..."
  minikube start --memory=8192 --cpus=4 2>/dev/null || minikube status
  minikube addons enable ingress 2>/dev/null || true
  minikube addons enable metrics-server 2>/dev/null || true
elif kubectl get nodes &>/dev/null; then
  echo "✅ Cluster sẵn sàng (Docker Desktop / kind)"
else
  echo "❌ Cần minikube hoặc Docker Desktop K8s"
  exit 1
fi

# Alias gợi ý
mkdir -p "$(dirname "$0")/../.lab"
cat > "$(dirname "$0")/../.lab/bashrc-snippet" << 'EOF'
alias k=kubectl
export do="--dry-run=client -o yaml"
complete -F __start_kubectl k 2>/dev/null || true
EOF

echo "✅ Lab ready"
echo "  source 18-cka-cks-kubernetes/.lab/bashrc-snippet"
echo "  bash 18-cka-cks-kubernetes/scripts/02-run-lab.sh basic 01"
