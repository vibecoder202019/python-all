"""AWX REST client — list templates, launch job (tạo task), poll status.

Demo mode: đọc data/awx_fixture.json khi chưa có AWX_URL/AWX_TOKEN.
"""
from __future__ import annotations

import json
import os
import time
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None  # type: ignore

MODULE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = MODULE_DIR / "data" / "awx_fixture.json"


@dataclass
class AwxConfig:
    base_url: str = ""
    token: str = ""
    username: str = ""
    password: str = ""
    verify_ssl: bool = True
    demo: bool = False
    fixture_path: Path = DEFAULT_FIXTURE
    default_template_id: int | None = None

    @classmethod
    def from_env(cls, force_demo: bool = False) -> "AwxConfig":
        url = os.environ.get("AWX_URL", "").rstrip("/")
        token = os.environ.get("AWX_TOKEN", "")
        demo_flag = os.environ.get("AWX_DEMO", "").lower() in ("1", "true", "yes")
        demo = force_demo or demo_flag or not url
        tid = os.environ.get("AWX_DEFAULT_JOB_TEMPLATE_ID")
        return cls(
            base_url=url,
            token=token,
            username=os.environ.get("AWX_USERNAME", ""),
            password=os.environ.get("AWX_PASSWORD", ""),
            verify_ssl=os.environ.get("AWX_VERIFY_SSL", "true").lower()
            not in ("0", "false", "no"),
            demo=demo,
            default_template_id=int(tid) if tid else None,
        )


class AwxClient:
    """Client gọi Ansible AWX / AAP API v2."""

    def __init__(self, config: AwxConfig | None = None) -> None:
        self.config = config or AwxConfig.from_env()
        self._fixture: dict[str, Any] | None = None
        self._session = None
        if not self.config.demo:
            if requests is None:
                raise ImportError("pip install requests")
            self._session = requests.Session()
            self._session.verify = self.config.verify_ssl
            if self.config.token:
                self._session.headers["Authorization"] = f"Bearer {self.config.token}"
            elif self.config.username:
                self._session.auth = (self.config.username, self.config.password)
            else:
                raise ValueError("Cần AWX_TOKEN hoặc AWX_USERNAME/PASSWORD (hoặc AWX_DEMO=true)")
            self._session.headers["Content-Type"] = "application/json"

    def _load_fixture(self) -> dict[str, Any]:
        if self._fixture is None:
            self._fixture = json.loads(self.config.fixture_path.read_text(encoding="utf-8"))
        return self._fixture

    def _url(self, path: str) -> str:
        path = path if path.startswith("/") else f"/{path}"
        return f"{self.config.base_url}/api/v2{path}"

    def list_job_templates(self) -> list[dict[str, Any]]:
        if self.config.demo:
            return list(self._load_fixture().get("job_templates", []))
        assert self._session is not None
        resp = self._session.get(self._url("/job_templates/"), params={"page_size": 100}, timeout=30)
        resp.raise_for_status()
        return resp.json().get("results", [])

    def get_template(self, template_id: int) -> dict[str, Any] | None:
        for t in self.list_job_templates():
            if int(t["id"]) == int(template_id):
                return t
        return None

    def get_template_by_name(self, name: str) -> dict[str, Any] | None:
        for t in self.list_job_templates():
            if t.get("name") == name:
                return t
        return None

    def launch_job_template(
        self,
        template_id: int,
        extra_vars: dict[str, Any] | None = None,
        *,
        limit: str | None = None,
        inventory: int | None = None,
    ) -> dict[str, Any]:
        """Tạo task (job) trên AWX từ Job Template — tương đương 'Launch' trên UI."""
        payload: dict[str, Any] = {}
        if extra_vars:
            payload["extra_vars"] = extra_vars
        if limit:
            payload["limit"] = limit
        if inventory is not None:
            payload["inventory"] = inventory

        if self.config.demo:
            templates = {int(t["id"]): t for t in self.list_job_templates()}
            tmpl = templates.get(int(template_id))
            if not tmpl:
                raise ValueError(f"Demo fixture không có template id={template_id}")
            job_id = 9000 + (uuid.uuid4().int % 1000)
            job = {
                "id": job_id,
                "job": job_id,
                "type": "job",
                "job_template": template_id,
                "name": tmpl["name"],
                "status": "successful",
                "started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "finished": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "extra_vars": extra_vars or {},
                "url": f"/api/v2/jobs/{job_id}/",
                "demo": True,
            }
            self._load_fixture().setdefault("jobs", []).append(job)
            return job

        assert self._session is not None
        resp = self._session.post(
            self._url(f"/job_templates/{template_id}/launch/"),
            json=payload,
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()

    def get_job(self, job_id: int) -> dict[str, Any]:
        if self.config.demo:
            for j in self._load_fixture().get("jobs", []):
                if int(j["id"]) == int(job_id):
                    return j
            raise ValueError(f"Demo: không tìm thấy job {job_id}")
        assert self._session is not None
        resp = self._session.get(self._url(f"/jobs/{job_id}/"), timeout=30)
        resp.raise_for_status()
        return resp.json()

    def wait_for_job(
        self,
        job_id: int,
        *,
        poll_interval: float = 3.0,
        timeout: float = 600.0,
    ) -> dict[str, Any]:
        if self.config.demo:
            return self.get_job(job_id)
        terminal = {"successful", "failed", "error", "canceled"}
        elapsed = 0.0
        while elapsed < timeout:
            job = self.get_job(job_id)
            if job.get("status") in terminal:
                return job
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"Job {job_id} chưa xong sau {timeout}s")
