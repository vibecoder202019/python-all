# Lab 04 — Agent Bridge API

**Thời gian:** 45 phút  
**Tiên quyết:** Lab 02, Module 15 (hoặc demo mode)

## Mục tiêu

Chạy REST API để n8n (Module 24) gọi AWX.

## Bước 1: Cấu hình env

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
cp config/.env.example config/.env
# Sửa BRIDGE_API_KEY, AWX_TOKEN nếu có AWX
```

## Bước 2: Chạy bridge (terminal 1)

```bash
bash scripts/04-run-agent-bridge.sh
```

## Bước 3: Test (terminal 2)

```bash
curl http://localhost:8090/health
curl -H "X-API-Key: lab-bridge-key" http://localhost:8090/templates
curl -X POST http://localhost:8090/agent/run \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{"intent":"list_templates"}'
```

## Bước 4: Launch job (AWX thật)

```bash
curl -X POST http://localhost:8090/agent/run \
  -H "Content-Type: application/json" \
  -H "X-API-Key: lab-bridge-key" \
  -d '{
    "intent": "launch_job",
    "template_name": "Python Hello World",
    "extra_vars": {"user_name": "n8n-bridge"},
    "wait": true
  }'
```

## Checklist

- [ ] `/docs` mở được Swagger
- [ ] `list_templates` trả JSON
- [ ] Hiểu header `X-API-Key`

**Tiếp theo:** Module 24 — [lab03-connect-mcp-bridge.md](../../24-n8n-ai-automation/labs/capstone/03-connect-mcp-bridge.md)
