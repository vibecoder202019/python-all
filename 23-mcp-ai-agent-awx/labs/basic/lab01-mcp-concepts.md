# Lab 01 — Khái niệm MCP

**Thời gian:** 30 phút  
**Tiên quyết:** Module 01–05 (Python)

## Mục tiêu

- Hiểu client / server / tools
- Vẽ được luồng AWX qua MCP

## Bước 1: Đọc

```bash
cat learn-python-ai/23-mcp-ai-agent-awx/docs/01-mcp-overview.md
```

## Bước 2: So sánh 3 lớp automation

| Lớp | Công cụ | Ai trigger |
|-----|---------|------------|
| Ansible | AWX (Module 15) | DevOps / API |
| AI Agent | **Ollama** (Module 23, **miễn phí**) | Chat CLI / HTTP |
| Orchestration | n8n (Module 24) | Webhook / Schedule |

## Bước 3: Vẽ sơ đồ

```
Bạn → Ollama (free) → AWX → MinIO
Bạn → n8n → Bridge/agent/chat → Ollama → AWX
```

(Cursor/MCP — tùy chọn, không bắt buộc)

## Checklist hoàn thành

- [ ] Giải thích được MCP server vs client
- [ ] Biết AWX token lấy ở đâu (Module 15)
- [ ] Biết Module 24 dùng Bridge thay vì MCP trực tiếp

**Tiếp theo:** [lab02-run-mcp-server.md](lab02-run-mcp-server.md)
