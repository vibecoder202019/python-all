"""Ollama client — AI miễn phí, chạy local (không cần Cursor/API key)."""
from __future__ import annotations

import json
import os
import re
from typing import Any

import httpx

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")

SYSTEM_PROMPT = """Bạn là DevOps agent. Người dùng muốn điều khiển Ansible AWX.
Trả lời CHỈ bằng một JSON object (không markdown), một trong các intent:

1. list_templates — liệt kê job template
   {"intent":"list_templates"}

2. launch_job — chạy job
   {"intent":"launch_job","template_name":"Tên template","extra_vars":{"user_name":"ai"}}

3. job_status — xem trạng thái job
   {"intent":"job_status","job_id":42,"wait":false}

4. explain — giải thích, không gọi AWX
   {"intent":"explain","message":"..."}

Nếu không chắc template_name, dùng list_templates trước.
"""


def ollama_available() -> bool:
    try:
        r = httpx.get(f"{OLLAMA_URL}/api/tags", timeout=3)
        return r.status_code == 200
    except httpx.HTTPError:
        return False


def pull_model(model: str | None = None) -> None:
    model = model or OLLAMA_MODEL
    with httpx.stream(
        "POST",
        f"{OLLAMA_URL}/api/pull",
        json={"name": model},
        timeout=None,
    ) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines():
            if line:
                data = json.loads(line)
                if "status" in data:
                    print(data["status"])


def chat_raw(prompt: str, model: str | None = None) -> str:
    model = model or OLLAMA_MODEL
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        "stream": False,
        "options": {"temperature": 0.1},
    }
    r = httpx.post(f"{OLLAMA_URL}/api/chat", json=payload, timeout=120)
    r.raise_for_status()
    return r.json()["message"]["content"]


def _extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{[\s\S]*\}", text)
    if match:
        return json.loads(match.group())
    raise ValueError(f"Ollama không trả JSON hợp lệ: {text[:200]}")


def parse_intent(user_message: str, model: str | None = None) -> dict[str, Any]:
    """Gửi câu hỏi tự nhiên → JSON intent cho AWX bridge."""
    raw = chat_raw(user_message, model=model)
    return _extract_json(raw)
