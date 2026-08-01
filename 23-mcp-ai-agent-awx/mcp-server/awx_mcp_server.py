#!/usr/bin/env python3
"""
MCP Server — cung cấp tools AWX cho AI agent (Cursor, Claude Desktop, ...).

Chạy (stdio — Cursor gọi tự động):
  python mcp-server/awx_mcp_server.py

Test local:
  AWX_DEMO_MODE=1 python mcp-server/awx_mcp_server.py
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from lib.awx_tools import job_status_json, launch_job_json, list_templates_json

try:
    from mcp.server import MCPServer
except ImportError as exc:
    raise SystemExit(
        "Thiếu package mcp. Chạy: pip install 'mcp[cli]>=1.2.0'"
    ) from exc

DEMO = os.environ.get("AWX_DEMO_MODE", "").lower() in ("1", "true", "yes")

server = MCPServer(
    "awx-devops-agent",
    instructions=(
        "Agent hỗ trợ DevOps qua Ansible AWX. "
        "Dùng awx_list_job_templates trước khi launch. "
        "Sau launch dùng awx_job_status để theo dõi."
    ),
)


@server.tool()
async def awx_list_job_templates() -> str:
    """Liệt kê Job Template trên AWX (id + name)."""
    return list_templates_json(demo=DEMO)


@server.tool()
async def awx_launch_job(
    template_name: str = "",
    template_id: int = 0,
    extra_vars_json: str = "{}",
) -> str:
    """
    Launch job trên AWX.
    template_name: tên template (ưu tiên).
    template_id: id số nếu không có tên.
    extra_vars_json: JSON string extra vars, ví dụ {"user_name":"Lab"}.
    """
    extra = json.loads(extra_vars_json or "{}")
    tid = template_id if template_id else None
    tname = template_name or None
    return launch_job_json(
        template_name=tname,
        template_id=tid,
        extra_vars=extra or None,
        demo=DEMO,
    )


@server.tool()
async def awx_job_status(job_id: int, wait: bool = False) -> str:
    """Lấy trạng thái job AWX. wait=true chờ đến khi successful/failed."""
    return job_status_json(job_id, wait=wait, demo=DEMO)


async def main() -> None:
    await server.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
