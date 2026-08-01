# Hướng dẫn chạy Manual — Module 24: n8n + AI Automation

> Capstone liên kết với Module **15** và **23**.

## Phần A — Kiểm tra

```bash
bash 24-n8n-ai-automation/scripts/01-check-prerequisites.sh
```

## Phần B — Bridge phải chạy trước (Module 23)

```bash
cd learn-python-ai
bash 23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh
```

## Phần C — Deploy n8n

```bash
cd learn-python-ai/24-n8n-ai-automation/docker-compose
cp .env.example .env
docker compose up -d
docker compose ps
```

```bash
open http://localhost:5678
```

Login: `admin` / `n8n-lab-pass`

## Phần D — Test bridge từ container n8n

```bash
docker exec n8n-lab wget -qO- http://host.docker.internal:8090/health
```

## Phần E — Import workflow

1. n8n UI → **Workflows** → **Import from File**
2. Chọn `24-n8n-ai-automation/workflows/02-awx-list-templates.json`
3. **Execute Workflow** (nút play)

## Phần F — Capstone webhook

1. Import `workflows/04-capstone-ai-ops.json`
2. **Activate** workflow
3. Test:

```bash
bash 24-n8n-ai-automation/scripts/04-test-webhook.sh
```

Hoặc:

```bash
curl -X POST http://localhost:5678/webhook/awx-run \
  -u admin:n8n-lab-pass \
  -H "Content-Type: application/json" \
  -d '{"template_name":"Python Hello World","extra_vars":{"user_name":"manual-capstone"}}'
```

## Phần G — AWX thật (tùy chọn)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
export AWX_URL=http://localhost:8052
export AWX_TOKEN=PASTE_TOKEN
export AWX_DEMO_MODE=0
# Restart bridge với env trên
```

## Teardown

```bash
bash 24-n8n-ai-automation/scripts/06-teardown.sh
```

## Lab capstone đầy đủ

```bash
cat 24-n8n-ai-automation/labs/capstone/README.md
```
