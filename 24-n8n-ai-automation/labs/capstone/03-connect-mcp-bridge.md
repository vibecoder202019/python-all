# Lab Capstone 03 — Kết nối n8n với Agent Bridge

## Mục tiêu

n8n container gọi Bridge trên máy host (Module 23).

## Bước 1: Bridge env

File `23-mcp-ai-agent-awx/config/.env`:

```
BRIDGE_API_KEY=lab-bridge-key
AWX_DEMO_MODE=1
```

## Bước 2: n8n env

File `24-n8n-ai-automation/docker-compose/.env`:

```
BRIDGE_URL=http://host.docker.internal:8090
BRIDGE_API_KEY=lab-bridge-key
```

## Bước 3: Test từ trong container n8n

```bash
docker exec n8n-lab wget -qO- http://host.docker.internal:8090/health
```

## Bước 4: Import workflow list templates

n8n UI → Import `workflows/02-awx-list-templates.json` → Execute Workflow (manual)

**Kỳ vọng:** JSON templates từ bridge.

## Bước 5: Sửa URL nếu cần (Linux)

Thay `host.docker.internal` bằng IP host hoặc thêm `extra_hosts` trong compose.

**Tiếp:** [04-end-to-end.md](04-end-to-end.md)
