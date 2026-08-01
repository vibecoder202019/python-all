"""Thực thi intent AWX — dùng chung cho Ollama agent và Bridge API."""
from __future__ import annotations

import json
import os
from typing import Any

from lib import awx_tools


def is_demo() -> bool:
    return os.environ.get("AWX_DEMO_MODE", "").lower() in ("1", "true", "yes")


def execute_intent(data: dict[str, Any]) -> dict[str, Any]:
    intent = (data.get("intent") or "").lower().strip()
    demo = is_demo()

    if intent == "explain":
        return {"intent": "explain", "message": data.get("message", "")}

    if intent == "list_templates":
        return json.loads(awx_tools.list_templates_json(demo=demo))

    if intent == "launch_job":
        raw = awx_tools.launch_job_json(
            template_name=data.get("template_name"),
            template_id=data.get("template_id"),
            extra_vars=data.get("extra_vars"),
            demo=demo,
        )
        result = json.loads(raw)
        if data.get("wait") and result.get("job") and not demo:
            final = json.loads(
                awx_tools.job_status_json(int(result["job"]), wait=True, demo=False)
            )
            result["final"] = final
        return result

    if intent == "job_status":
        job_id = data.get("job_id")
        if not job_id:
            return {"error": "Thiếu job_id"}
        return json.loads(
            awx_tools.job_status_json(
                int(job_id),
                wait=bool(data.get("wait")),
                demo=demo,
            )
        )

    return {"error": f"Intent không hỗ trợ: {intent}"}
