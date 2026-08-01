# Hướng dẫn chạy Manual — Module 24: n8n + AI Automation

> Lệnh trích từ `setup.sh`, `01-check-prerequisites.sh`, `02-deploy-n8n-compose.sh`, `03-deploy-k8s.sh`, `04-test-webhook.sh`, `06-teardown.sh`, `07-teardown-k8s.sh`.

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
command -v docker
cp -n learn-python-ai/24-n8n-ai-automation/docker-compose/.env.example \
      learn-python-ai/24-n8n-ai-automation/docker-compose/.env
```

**Kiểm tra Docker:**

```bash
docker --version
docker compose version
docker info >/dev/null && echo "Docker daemon OK"
```

---

## Phần B — Kiểm tra stack (`scripts/01-check-prerequisites.sh`)

```bash
docker --version
docker compose version
curl -sf http://localhost:8090/health || echo "Start Module 23 bridge first"
kubectl get pods -n awx 2>/dev/null | head -3 || echo "AWX optional"
```

**Kỳ vọng bridge:** `{"status":"ok",...}`

---

## Phần C — Bridge phải chạy trước (Module 23)

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
source ../.venv/bin/activate
set -a && source config/.env && set +a
uvicorn agent-bridge.main:app --host 0.0.0.0 --port 8090
```

---

---

## Phần D2 — Deploy Kubernetes (`scripts/03-deploy-k8s.sh`)

Full stack namespace `ai-automation` (n8n + agent-bridge + Ollama):

```bash
kubectl cluster-info
cd learn-python-ai/24-n8n-ai-automation
bash scripts/03-deploy-k8s.sh
```

Build image bridge (script tự chạy):

```bash
docker build -t awx-agent-bridge:lab \
  -f learn-python-ai/23-mcp-ai-agent-awx/agent-bridge/Dockerfile \
  learn-python-ai/23-mcp-ai-agent-awx
```

Apply từng manifest (nếu không dùng script):

```bash
K8S=learn-python-ai/24-n8n-ai-automation/k8s-ai-automation
kubectl apply -f $K8S/namespace.yaml
kubectl apply -f $K8S/configmap.yaml
kubectl apply -f $K8S/secret.yaml
kubectl apply -f $K8S/n8n-pvc.yaml
kubectl apply -f $K8S/ollama-pvc.yaml
kubectl apply -f $K8S/ollama-deployment.yaml
kubectl apply -f $K8S/ollama-service.yaml
kubectl apply -f $K8S/agent-bridge-deployment.yaml
kubectl apply -f $K8S/agent-bridge-service.yaml
kubectl apply -f $K8S/n8n-deployment.yaml
kubectl apply -f $K8S/n8n-service.yaml
kubectl apply -f $K8S/ingress.yaml
```

**Kiểm tra:**

```bash
kubectl get pods -n ai-automation
kubectl wait --for=condition=available deployment/n8n -n ai-automation --timeout=180s
kubectl exec -n ai-automation deploy/ollama -- ollama pull llama3.2:1b
kubectl port-forward -n ai-automation svc/n8n 5678:5678
curl -sf -u admin:n8n-lab-pass http://localhost:5678/healthz
```

Thêm hosts: `127.0.0.1 n8n.local` (xem `k8s-ai-automation/hosts-entries.txt`)

Không cần Ollama trong cluster:

```bash
bash scripts/03-deploy-k8s.sh --skip-ollama
```

---

## Phần D — Deploy n8n Compose (`scripts/02-deploy-n8n-compose.sh`)

Chỉ n8n:

```bash
cd learn-python-ai/24-n8n-ai-automation/docker-compose
cp .env.example .env
docker compose up -d n8n
```

Kèm Ollama Docker:

```bash
docker compose --profile ollama up -d
sleep 5
docker exec ollama-lab ollama pull llama3.2:1b
```

**Kiểm tra:**

```bash
docker compose ps
curl -sf -u admin:n8n-lab-pass http://localhost:5678/healthz || curl -sf -o /dev/null -w "%{http_code}\n" http://localhost:5678/
docker exec n8n-lab wget -qO- http://host.docker.internal:8090/health
```

---

## Phần E — Import workflow (UI)

1. Mở http://localhost:5678 — `admin` / `n8n-lab-pass`
2. Import `workflows/02-awx-list-templates.json` → Execute
3. Import `workflows/05-ollama-ai-chat-awx.json` → **Activate**

---

## Phần F — Test webhook (`scripts/04-test-webhook.sh`)

Capstone AWX:

```bash
curl -s -X POST http://localhost:5678/webhook/awx-run \
  -H "Content-Type: application/json" \
  -u admin:n8n-lab-pass \
  -d '{"template_name":"Python Hello World","extra_vars":{"user_name":"capstone"}}'
```

AI Ollama:

```bash
curl -s -X POST http://localhost:5678/webhook/ai-ops \
  -H "Content-Type: application/json" \
  -u admin:n8n-lab-pass \
  -d '{"message":"List AWX job templates"}'
```

---

## Phần G — Capstone guide (`scripts/05-run-capstone-demo.sh`)

```bash
bash learn-python-ai/24-n8n-ai-automation/scripts/05-run-capstone-demo.sh
cat learn-python-ai/24-n8n-ai-automation/labs/capstone/README.md
```

---

## Phần H — Teardown

Compose (`scripts/06-teardown.sh`):

```bash
cd learn-python-ai/24-n8n-ai-automation/docker-compose
docker compose down
docker compose down -v
```

Kubernetes (`scripts/07-teardown-k8s.sh`):

```bash
bash learn-python-ai/24-n8n-ai-automation/scripts/07-teardown-k8s.sh
kubectl get ns ai-automation 2>/dev/null || echo "namespace removed"
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-deploy-n8n-compose.sh` | D |
| `03-deploy-k8s.sh` | D2 |
| `04-test-webhook.sh` | F |
| `05-run-capstone-demo.sh` | G |
| `06-teardown.sh` | H (Compose) |
| `07-teardown-k8s.sh` | H (K8s) |
| `08-pull-ollama-model-k8s.sh` | D2 (Ollama pull) |
