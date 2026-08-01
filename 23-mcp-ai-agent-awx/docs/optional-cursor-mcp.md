# (Tùy chọn) MCP + Cursor

> **Không bắt buộc.** Luồng chính module dùng **Ollama miễn phí** — xem [02-ollama-free-ai-agent.md](02-ollama-free-ai-agent.md).

MCP (Model Context Protocol) cho phép IDE như **Cursor** gọi tools AWX qua stdio.

## Khi nào dùng?

- Bạn đã dùng Cursor và muốn chat trong IDE
- Học thêm về chuẩn MCP (không liên quan n8n capstone)

## Cấu hình Cursor

1. `pip install 'mcp[cli]>=1.2.0'`
2. Sửa `config/cursor-mcp.example.json` — đường dẫn Python + AWX_TOKEN
3. Cursor → Settings → MCP → merge config
4. Chat: *"Liệt kê job template AWX"*

## Chạy MCP server thủ công

```bash
bash scripts/03-run-mcp-server.sh
```

## So sánh

| Ollama (mặc định) | Cursor MCP |
|-------------------|------------|
| Miễn phí, local | Cần Cursor |
| CLI + n8n `/agent/chat` | Chỉ trong IDE |
| Khuyến nghị capstone | Tùy chọn |

Chi tiết Cursor cũ: nội dung tương tự file `docs/04-cursor-mcp-config.md`.
