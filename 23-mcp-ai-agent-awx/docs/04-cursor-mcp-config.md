# Cấu hình MCP trong Cursor

## Bước 1: Lấy đường dẫn tuyệt đối server

```bash
cd learn-python-ai/23-mcp-ai-agent-awx
python -c "from pathlib import Path; print(Path('mcp-server/awx_mcp_server.py').resolve())"
```

## Bước 2: AWX token (Module 15)

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
# AWX UI → User → Tokens → Create
export AWX_TOKEN=...
```

## Bước 3: Thêm MCP server

Sửa `config/cursor-mcp.example.json` — thay `/ABSOLUTE/PATH/` và token.

**Cursor:** Settings → Features → MCP → Edit config

Hoặc merge vào `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "awx-devops-agent": {
      "command": "python",
      "args": ["/Users/you/learn-python-ai/23-mcp-ai-agent-awx/mcp-server/awx_mcp_server.py"],
      "env": {
        "AWX_URL": "http://localhost:8052",
        "AWX_TOKEN": "xxx",
        "AWX_DEMO_MODE": "0"
      }
    }
  }
}
```

Dùng venv Python:

```json
"command": "/Users/you/learn-python-ai/.venv/bin/python"
```

## Bước 4: Test trong chat

Prompt gợi ý:

- *Liệt kê job template trên AWX*
- *Launch job template "Python Hello World" với user_name=Capstone*
- *Kiểm tra status job 42*

Agent sẽ gọi tools `awx_list_job_templates`, `awx_launch_job`, `awx_job_status`.

## Demo không AWX

```json
"AWX_DEMO_MODE": "1"
```

## Troubleshooting

| Lỗi | Cách xử lý |
|-----|------------|
| MCP server không start | `pip install 'mcp[cli]>=1.2.0'` |
| 401 AWX | Token sai — tạo lại |
| Tool không hiện | Restart Cursor sau khi sửa mcp.json |
