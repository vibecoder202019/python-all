# MCP (Model Context Protocol) — Tổng quan

## MCP là gì?

**MCP** là giao thức chuẩn để **AI client** (Cursor, Claude Desktop) kết nối **MCP server** cung cấp **tools**, **resources**, **prompts**.

```
AI Client ──stdio/SSE──► MCP Server ──► API bên ngoài (AWX, DB, Git...)
```

## Tại sao dùng MCP cho AWX?

| Không MCP | Có MCP |
|-----------|--------|
| Copy token, curl thủ công | Chat: "Deploy app staging" |
| Prompt dài, dễ sai | Agent gọi tool có schema |
| Khó audit | Tool calls có log rõ ràng |

## Thành phần lab Module 23

1. **MCP Server** (`mcp-server/awx_mcp_server.py`) — 3 tools AWX
2. **Agent Bridge** (`agent-bridge/main.py`) — REST cho n8n
3. **Cursor config** — agent cá nhân trên máy bạn

## Bước tiếp theo

→ [lab01-mcp-concepts.md](../labs/basic/lab01-mcp-concepts.md)
