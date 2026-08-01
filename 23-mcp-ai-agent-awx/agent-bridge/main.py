#!/usr/bin/env python3
"""
Agent Bridge API — REST gateway để n8n / webhook gọi AWX (không cần MCP client).

Chạy:
  uvicorn agent-bridge.main:app --host 0.0.0.0 --port 8090

Env: AWX_URL, AWX_TOKEN, BRIDGE_API_KEY (tùy chọn)
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from lib.awx_tools import job_status_json, launch_job_json, list_templates_json
from lib.agent_executor import execute_intent
from lib.ollama_client import OLLAMA_MODEL, ollama_available, parse_intent

DEMO = os.environ.get("AWX_DEMO_MODE", "").lower() in ("1", "true", "yes")
USE_OLLAMA = os.environ.get("USE_OLLAMA", "1").lower() not in ("0", "false", "no")
API_KEY = os.environ.get("BRIDGE_API_KEY", "")

app = FastAPI(
    title="AWX Agent Bridge",
    description="REST API cho n8n tích hợp AWX — Module 23/24 capstone",
    version="1.0.0",
)


def _check_key(x_api_key: str | None) -> None:
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid X-API-Key")


class LaunchBody(BaseModel):
    template_name: str | None = None
    template_id: int | None = None
    extra_vars: dict[str, Any] = Field(default_factory=dict)
    wait: bool = False


class AgentRunBody(BaseModel):
    """Payload thân thiện cho n8n — AI ops tự nhiên."""
    intent: str = Field(
        ...,
        description="list_templates | launch_job | job_status",
    )
    template_name: str | None = None
    template_id: int | None = None
    job_id: int | None = None
    extra_vars: dict[str, Any] = Field(default_factory=dict)
    wait: bool = False


class AgentChatBody(BaseModel):
    """Chat tự nhiên — Ollama (free) parse intent rồi thực thi AWX."""
    message: str = Field(..., min_length=1)
    use_ollama: bool = True


@app.get("/health")
def health():
    return {
        "status": "ok",
        "demo_mode": DEMO,
        "ollama": ollama_available() if USE_OLLAMA else False,
        "ollama_model": OLLAMA_MODEL,
    }


@app.get("/templates")
def templates(x_api_key: str | None = Header(default=None)):
    _check_key(x_api_key)
    return json.loads(list_templates_json(demo=DEMO))


@app.post("/jobs/launch")
def launch(body: LaunchBody, x_api_key: str | None = Header(default=None)):
    _check_key(x_api_key)
    raw = launch_job_json(
        template_name=body.template_name,
        template_id=body.template_id,
        extra_vars=body.extra_vars or None,
        demo=DEMO,
    )
    data = json.loads(raw)
    job_id = data.get("job")
    if body.wait and job_id and not DEMO:
        status_raw = job_status_json(int(job_id), wait=True, demo=False)
        data["final"] = json.loads(status_raw)
    return data


@app.get("/jobs/{job_id}")
def job(job_id: int, wait: bool = False, x_api_key: str | None = Header(default=None)):
    _check_key(x_api_key)
    return json.loads(job_status_json(job_id, wait=wait, demo=DEMO))


@app.post("/agent/run")
def agent_run(body: AgentRunBody, x_api_key: str | None = Header(default=None)):
    """
    Endpoint capstone: n8n gửi intent → bridge xử lý như AI agent đơn giản.
    """
    _check_key(x_api_key)
    intent = body.intent.lower().strip()

    if intent == "list_templates":
        return json.loads(list_templates_json(demo=DEMO))

    if intent == "launch_job":
        raw = launch_job_json(
            template_name=body.template_name,
            template_id=body.template_id,
            extra_vars=body.extra_vars or None,
            demo=DEMO,
        )
        data = json.loads(raw)
        if body.wait and data.get("job") and not DEMO:
            data["final"] = json.loads(
                job_status_json(int(data["job"]), wait=True, demo=False)
            )
        return data

    if intent == "job_status":
        if not body.job_id:
            raise HTTPException(400, "job_id required for job_status")
        return json.loads(job_status_json(body.job_id, wait=body.wait, demo=DEMO))

    raise HTTPException(400, f"Unknown intent: {body.intent}")


@app.post("/agent/chat")
def agent_chat(body: AgentChatBody, x_api_key: str | None = Header(default=None)):
    """
    AI miễn phí (Ollama): câu chat tự nhiên → parse intent → AWX.
    n8n có thể POST message thay vì intent cứng.
    """
    _check_key(x_api_key)

    if body.use_ollama and USE_OLLAMA:
        if not ollama_available():
            raise HTTPException(
                503,
                "Ollama chưa chạy. Chạy: ollama serve && ollama pull llama3.2:1b",
            )
        try:
            intent = parse_intent(body.message)
        except (ValueError, json.JSONDecodeError) as e:
            raise HTTPException(422, f"Ollama parse lỗi: {e}") from e
    else:
        # Fallback rule-based khi không có Ollama
        lower = body.message.lower()
        if "list" in lower or "liệt kê" in lower:
            intent = {"intent": "list_templates"}
        elif "launch" in lower or "chạy" in lower:
            intent = {
                "intent": "launch_job",
                "template_name": "Python Hello World",
                "extra_vars": {"user_name": "bridge"},
            }
        else:
            intent = {"intent": "explain", "message": "Thử: list templates hoặc launch job"}

    result = execute_intent(intent)
    return {
        "user_message": body.message,
        "parsed_intent": intent,
        "result": result,
    }
