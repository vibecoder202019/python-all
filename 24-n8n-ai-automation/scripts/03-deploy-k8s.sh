#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODULE_DIR="$(dirname "$SCRIPT_DIR")"
K8S_DIR="$MODULE_DIR/k8s-ai-automation"
M23_DIR="$(dirname "$MODULE_DIR")/23-mcp-ai-agent-awx"
SKIP_OLLAMA=0
SKIP_BUILD=0

for arg in "$@"; do
  case "$arg" in
    --skip-ollama) SKIP_OLLAMA=1 ;;
    --skip-build) SKIP_BUILD=1 ;;
  esac
done

echo "=== Deploy Module 24 — Kubernetes (ai-automation) ==="
command -v kubectl >/dev/null || { echo "Cần kubectl + cluster (k3s/minikube/Docker Desktop K8s)"; exit 1; }
kubectl cluster-info >/dev/null

if [[ "$SKIP_BUILD" -eq 0 ]]; then
  echo "Build Agent Bridge image (Module 23)..."
  docker build -t awx-agent-bridge:lab -f "$M23_DIR/agent-bridge/Dockerfile" "$M23_DIR"

  # Load image vào cluster local nếu cần
  if command -v minikube >/dev/null && minikube status >/dev/null 2>&1; then
    echo "Load image vào minikube..."
    minikube image load awx-agent-bridge:lab
  elif command -v kind >/dev/null && kind get clusters 2>/dev/null | grep -q .; then
    CLUSTER="$(kind get clusters | head -1)"
    echo "Load image vào kind ($CLUSTER)..."
    kind load docker-image awx-agent-bridge:lab --name "$CLUSTER"
  fi
fi

echo "Apply manifests..."
kubectl apply -f "$K8S_DIR/namespace.yaml"
kubectl apply -f "$K8S_DIR/configmap.yaml"
kubectl apply -f "$K8S_DIR/secret.yaml"
kubectl apply -f "$K8S_DIR/n8n-pvc.yaml"

if [[ "$SKIP_OLLAMA" -eq 0 ]]; then
  kubectl apply -f "$K8S_DIR/ollama-pvc.yaml"
  kubectl apply -f "$K8S_DIR/ollama-deployment.yaml"
  kubectl apply -f "$K8S_DIR/ollama-service.yaml"
fi

kubectl apply -f "$K8S_DIR/agent-bridge-deployment.yaml"
kubectl apply -f "$K8S_DIR/agent-bridge-service.yaml"
kubectl apply -f "$K8S_DIR/n8n-deployment.yaml"
kubectl apply -f "$K8S_DIR/n8n-service.yaml"
kubectl apply -f "$K8S_DIR/ingress.yaml"

echo "Chờ pods ready..."
kubectl wait --for=condition=available deployment/agent-bridge -n ai-automation --timeout=120s
kubectl wait --for=condition=available deployment/n8n -n ai-automation --timeout=180s
if [[ "$SKIP_OLLAMA" -eq 0 ]]; then
  kubectl wait --for=condition=available deployment/ollama -n ai-automation --timeout=120s || true
fi

if [[ "$SKIP_OLLAMA" -eq 0 ]]; then
  echo "Pull Ollama model (có thể mất vài phút)..."
  kubectl exec -n ai-automation deploy/ollama -- ollama pull "${OLLAMA_MODEL:-llama3.2:1b}" || \
    echo "  (bỏ qua pull — chạy lại: bash scripts/08-pull-ollama-model-k8s.sh)"
fi

echo ""
echo "✓ Namespace: ai-automation"
echo "  n8n UI:      http://n8n.local:5678  (hoặc port-forward, xem docs/05-deploy-kubernetes.md)"
echo "  Bridge:      http://agent-bridge.ai-automation.svc.cluster.local:8090"
echo "  Credentials: admin / n8n-lab-pass"
echo ""
echo "Thêm hosts (nếu chưa có):"
cat "$K8S_DIR/hosts-entries.txt"
echo ""
echo "Test bridge trong cluster:"
echo "  kubectl run curl-test --rm -it --restart=Never --image=curlimages/curl -- \\"
echo "    curl -sf http://agent-bridge.ai-automation.svc:8090/health"
echo ""
echo "Test webhook (sau khi import workflow):"
echo "  N8N_WEBHOOK_URL=http://n8n.local/webhook/awx-run bash scripts/04-test-webhook.sh"
