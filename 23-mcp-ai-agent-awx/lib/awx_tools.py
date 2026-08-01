"""AWX helpers dùng chung cho MCP server và Agent Bridge (Module 23)."""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests

MODULE15 = Path(__file__).resolve().parents[2] / "15-ansible-awx-minio-k8s" / "project"
_USE_MODULE15 = False
if MODULE15.exists():
    sys.path.insert(0, str(MODULE15))
    try:
        from common import AWXClient as _AWXClient15
        from common import get_awx_client as _get_awx_client15
        from common import handle_awx_error

        _USE_MODULE15 = True
    except ImportError:
        handle_awx_error = lambda e: str(e)  # noqa: E731

DEFAULT_AWX_URL = os.environ.get("AWX_URL", "http://localhost:8052")
DEFAULT_AWX_TOKEN = os.environ.get("AWX_TOKEN", "")


class AWXClient:
    """Fallback client nếu không import được Module 15."""

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            }
        )

    def _url(self, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{self.base_url}/api/v2{path}"

    def get(self, path: str, params: dict | None = None) -> dict[str, Any]:
        resp = self.session.get(self._url(path), params=params, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def post(self, path: str, data: dict | None = None) -> dict[str, Any]:
        resp = self.session.post(self._url(path), json=data or {}, timeout=30)
        resp.raise_for_status()
        return resp.json()

    def list_job_templates(self) -> list[dict[str, Any]]:
        return self.get("/job_templates/").get("results", [])

    def get_template_by_name(self, name: str) -> dict[str, Any] | None:
        for tmpl in self.list_job_templates():
            if tmpl.get("name") == name:
                return tmpl
        return None

    def launch_job(self, template_id: int, extra_vars: dict | None = None) -> dict[str, Any]:
        payload: dict[str, Any] = {}
        if extra_vars:
            payload["extra_vars"] = extra_vars
        return self.post(f"/job_templates/{template_id}/launch/", payload)

    def get_job(self, job_id: int) -> dict[str, Any]:
        return self.get(f"/jobs/{job_id}/")

    def get_job_stdout(self, job_id: int) -> str:
        resp = self.session.get(
            self._url(f"/jobs/{job_id}/stdout/"),
            params={"format": "txt"},
            timeout=30,
        )
        resp.raise_for_status()
        return resp.text

    def wait_for_job(self, job_id: int, poll_interval: int = 5, timeout: int = 600) -> dict[str, Any]:
        terminal = {"successful", "failed", "error", "canceled"}
        elapsed = 0
        while elapsed < timeout:
            job = self.get_job(job_id)
            if job.get("status") in terminal:
                return job
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"Job {job_id} timeout sau {timeout}s")


def client_from_env():
    if _USE_MODULE15:
        return _get_awx_client15()
    if not DEFAULT_AWX_TOKEN:
        raise ValueError("Thiếu AWX_TOKEN — tạo token trên AWX UI")
    client = AWXClient(DEFAULT_AWX_URL, DEFAULT_AWX_TOKEN)
    return type("Ctx", (), {"client": client, "base_url": DEFAULT_AWX_URL, "token": DEFAULT_AWX_TOKEN})()


def demo_templates() -> list[dict[str, Any]]:
    return [
        {"id": 7, "name": "Python Hello World", "status": "demo"},
        {"id": 8, "name": "MinIO Upload Demo", "status": "demo"},
    ]


def list_templates_json(demo: bool = False) -> str:
    if demo:
        return json.dumps({"mode": "demo", "templates": demo_templates()}, indent=2)
    ctx = client_from_env()
    templates = ctx.client.list_job_templates()
    slim = [{"id": t["id"], "name": t["name"]} for t in templates]
    return json.dumps({"templates": slim}, indent=2)


def launch_job_json(
    template_name: str | None = None,
    template_id: int | None = None,
    extra_vars: dict | None = None,
    demo: bool = False,
) -> str:
    if demo:
        return json.dumps(
            {
                "mode": "demo",
                "job": 42,
                "template": template_name or template_id,
                "status": "successful",
            },
            indent=2,
        )
    ctx = client_from_env()
    tid = template_id
    if template_name:
        tmpl = ctx.client.get_template_by_name(template_name)
        if not tmpl:
            raise ValueError(f"Không tìm thấy template: {template_name}")
        tid = tmpl["id"]
    if not tid:
        raise ValueError("Cần template_name hoặc template_id")
    result = ctx.client.launch_job(tid, extra_vars=extra_vars)
    return json.dumps(result, indent=2)


def job_status_json(job_id: int, wait: bool = False, demo: bool = False) -> str:
    if demo:
        return json.dumps({"mode": "demo", "job_id": job_id, "status": "successful"}, indent=2)
    ctx = client_from_env()
    job = ctx.client.wait_for_job(job_id) if wait else ctx.client.get_job(job_id)
    out = {"id": job.get("id"), "status": job.get("status"), "name": job.get("name")}
    if job.get("status") == "successful":
        out["stdout_preview"] = ctx.client.get_job_stdout(job_id)[:2000]
    return json.dumps(out, indent=2)
