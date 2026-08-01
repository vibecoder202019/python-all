# Lab Capstone 04 — End-to-end n8n → AWX

## Bước 1: 3 terminal

**T1 — Bridge**

```bash
export AWX_URL=http://localhost:8052
export AWX_TOKEN=your-token
export AWX_DEMO_MODE=0
export BRIDGE_API_KEY=lab-bridge-key
bash learn-python-ai/23-mcp-ai-agent-awx/scripts/04-run-agent-bridge.sh
```

**T2 — AWX port-forward (nếu K8s)**

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
```

**T3 — n8n**

```bash
bash learn-python-ai/24-n8n-ai-automation/scripts/02-deploy-n8n-compose.sh
```

## Bước 2: Import workflow trên n8n UI

1. Mở http://localhost:5678 (admin / n8n-lab-pass)
2. Workflows → Import from File → `workflows/04-capstone-ai-ops.json`
3. Bật **Active**

## Bước 3: Trigger webhook

```bash
bash learn-python-ai/24-n8n-ai-automation/scripts/04-test-webhook.sh
```

**Kỳ vọng:** JSON có `job` hoặc `status: successful` (demo mode).

## Bước 4: Xem execution trên n8n

Executions → workflow capstone → node "Call Agent Bridge" → output.

## Bước 5: Verify AWX (nếu không demo)

AWX UI → Jobs → job mới nhất → Successful.

## Troubleshooting

| Triệu chứng | Fix |
|-------------|-----|
| Connection refused bridge | Bridge chưa chạy T1 |
| 401 bridge | Sai `X-API-Key` |
| n8n không reach host | `host.docker.internal` — kiểm tra Docker Desktop |
| AWX 401 | Token hết hạn |

## Hoàn thành capstone 🎉

Bạn đã nối **orchestration (n8n) + AI agent layer (bridge/MCP) + automation (AWX)**.
