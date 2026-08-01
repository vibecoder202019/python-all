# Tích hợp n8n với Agent Bridge (Module 23)

## Luồng HTTP

```
n8n HTTP Request node
  POST http://host.docker.internal:8090/agent/run
  Header: X-API-Key: lab-bridge-key
  Body: {"intent":"launch_job","template_name":"...","wait":true}
```

## Env trong docker-compose

```
BRIDGE_URL=http://host.docker.internal:8090
BRIDGE_API_KEY=lab-bridge-key
```

## Workflow import

1. `workflows/02-awx-list-templates.json` — test kết nối
2. `workflows/04-capstone-ai-ops.json` — webhook production-like

## MCP vs n8n

| | MCP (Cursor) | n8n |
|---|--------------|-----|
| Trigger | Chat | Webhook, Cron, Email |
| Giao thức | stdio MCP | HTTP REST |
| Người dùng | Developer | Ops / no-code |

Cả hai dùng chung **Agent Bridge** hoặc AWX API.

## Capstone

→ [labs/capstone/README.md](../labs/capstone/README.md)
