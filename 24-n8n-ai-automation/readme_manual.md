# Hướng dẫn chạy Manual — Module 24: n8n + AI Automation

> Lệnh trích từ `setup.sh`, `01-check-prerequisites.sh`, `02-deploy-n8n-compose.sh`, `04-test-webhook.sh`, `06-teardown.sh`.

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

## Phần D — Deploy n8n (`scripts/02-deploy-n8n-compose.sh`)

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

## Phần H — Teardown (`scripts/06-teardown.sh`)

```bash
cd learn-python-ai/24-n8n-ai-automation/docker-compose
docker compose down
docker compose down -v
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-deploy-n8n-compose.sh` | D |
| `04-test-webhook.sh` | F |
| `05-run-capstone-demo.sh` | G |
| `06-teardown.sh` | H |
