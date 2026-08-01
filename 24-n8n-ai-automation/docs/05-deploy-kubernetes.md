# Triển khai Module 24 trên Kubernetes

Stack **ai-automation** gồm:

| Pod | Mô tả |
|-----|--------|
| **n8n** | Workflow automation (PVC lưu data) |
| **agent-bridge** | REST gateway Module 23 (image build local) |
| **ollama** | LLM miễn phí (tùy chọn, `--skip-ollama`) |

---

## Tiên quyết

- Cluster K8s (k3s, minikube, Docker Desktop K8s)
- **Ingress NGINX** (Module 15 đã cài hoặc tương đương)
- Docker (build image `awx-agent-bridge:lab`)
- Module 15 AWX (tùy chọn — demo mode vẫn chạy)

---

## Deploy nhanh

```bash
cd learn-python-ai/24-n8n-ai-automation

bash scripts/03-deploy-k8s.sh
```

Chỉ n8n + bridge (không Ollama trong cluster):

```bash
bash scripts/03-deploy-k8s.sh --skip-ollama
```

---

## Hosts & Ingress

Thêm vào `/etc/hosts`:

```
127.0.0.1 n8n.local
```

Nếu Ingress không trỏ localhost, dùng IP node hoặc `minikube ip`.

**Port-forward thay Ingress (lab nhanh):**

```bash
kubectl port-forward -n ai-automation svc/n8n 5678:5678
open http://localhost:5678
```

---

## Cấu hình AWX thật

Sửa `k8s-ai-automation/secret.yaml`:

```yaml
stringData:
  AWX_TOKEN: "your-awx-token"
```

Sửa `k8s-ai-automation/configmap.yaml`:

```yaml
AWX_URL: "http://awx-service.awx.svc.cluster.local"
AWX_DEMO_MODE: "0"
```

Apply lại:

```bash
kubectl apply -f k8s-ai-automation/configmap.yaml
kubectl apply -f k8s-ai-automation/secret.yaml
kubectl rollout restart deployment/agent-bridge -n ai-automation
```

---

## Kiểm tra

```bash
kubectl get pods -n ai-automation
kubectl logs -n ai-automation deploy/agent-bridge --tail=20
kubectl logs -n ai-automation deploy/n8n --tail=20

# Bridge health (trong cluster)
kubectl run curl-test --rm -it --restart=Never --image=curlimages/curl -- \
  curl -sf http://agent-bridge.ai-automation.svc:8090/health
```

Import workflow trên UI → test:

```bash
N8N_WEBHOOK_URL=http://n8n.local/webhook/awx-run bash scripts/04-test-webhook.sh
```

---

## So sánh Compose vs K8s

| | Docker Compose | Kubernetes |
|---|----------------|------------|
| n8n URL | localhost:5678 | n8n.local (Ingress) |
| Bridge | host :8090 | Service `agent-bridge:8090` |
| Ollama | host hoặc profile | Deployment trong namespace |
| AWX | port-forward | Cluster DNS `awx-service.awx` |

Capstone **15 → 23 → 24** trên K8s: AWX (ns `awx`) + stack `ai-automation` — không cần bridge chạy trên host.

---

## Teardown

```bash
bash scripts/07-teardown-k8s.sh
```

PVC bị xóa cùng namespace (data n8n/ollama mất — lab only).

---

## Manifests

```
k8s-ai-automation/
├── namespace.yaml
├── configmap.yaml
├── secret.yaml
├── n8n-pvc.yaml
├── n8n-deployment.yaml
├── n8n-service.yaml
├── agent-bridge-deployment.yaml
├── agent-bridge-service.yaml
├── ollama-pvc.yaml
├── ollama-deployment.yaml
├── ollama-service.yaml
├── ingress.yaml
└── hosts-entries.txt
```

Image bridge: `23-mcp-ai-agent-awx/agent-bridge/Dockerfile`
