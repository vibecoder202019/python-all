"""
Module 15 — Tiện ích dùng chung: AWX API client & MinIO helper

Dùng lại ở examples/, project/step01→step06.

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU:
  1. AWXClient — gọi REST API AWX (list template, launch job, poll status).
  2. get_awx_client() — đọc AWX_URL, AWX_TOKEN từ biến môi trường.
  3. MinIO helper — upload file bằng boto3 (S3-compatible).
  4. handle_awx_error() — thông báo lỗi tiếng Việt.
═══════════════════════════════════════════════════════════════════════════
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from typing import Any

try:
    import requests
except ImportError:
    requests = None

try:
    import boto3
    from botocore.client import Config
except ImportError:
    boto3 = None

# ── Cấu hình mặc định — override bằng biến môi trường ──
DEFAULT_AWX_URL = os.environ.get("AWX_URL", "http://localhost:8052")
DEFAULT_AWX_TOKEN = os.environ.get("AWX_TOKEN", "")
DEFAULT_MINIO_ENDPOINT = os.environ.get("MINIO_ENDPOINT", "http://localhost:9000")
DEFAULT_MINIO_ACCESS_KEY = os.environ.get("MINIO_ACCESS_KEY", "minioadmin")
DEFAULT_MINIO_SECRET_KEY = os.environ.get("MINIO_SECRET_KEY", "minioadmin123")


@dataclass
class AWXContext:
    """Thông tin kết nối AWX sau khi xác thực."""
    base_url: str
    token: str
    client: "AWXClient"


class AWXClient:
    """Client gọi AWX REST API v2 — dùng Bearer token."""

    def __init__(self, base_url: str, token: str) -> None:
        if requests is None:
            raise ImportError("pip install requests")
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

    def wait_for_job(
        self,
        job_id: int,
        poll_interval: int = 5,
        timeout: int = 600,
    ) -> dict[str, Any]:
        terminal = {"successful", "failed", "error", "canceled"}
        elapsed = 0
        while elapsed < timeout:
            job = self.get_job(job_id)
            status = job.get("status", "unknown")
            if status in terminal:
                return job
            time.sleep(poll_interval)
            elapsed += poll_interval
        raise TimeoutError(f"Job {job_id} chưa hoàn thành sau {timeout}s")


def get_awx_client(url: str | None = None, token: str | None = None) -> AWXContext:
    """Tạo AWXClient từ env hoặc tham số truyền vào."""
    base_url = url or DEFAULT_AWX_URL
    api_token = token or DEFAULT_AWX_TOKEN
    if not api_token:
        raise ValueError(
            "Thiếu AWX_TOKEN. Tạo token: AWX UI → User → Tokens → Create\n"
            "export AWX_TOKEN='your-token'"
        )
    client = AWXClient(base_url, api_token)
    return AWXContext(base_url=base_url, token=api_token, client=client)


def upload_to_minio(
    file_path: str,
    bucket: str,
    object_key: str,
    endpoint: str | None = None,
    access_key: str | None = None,
    secret_key: str | None = None,
) -> str:
    """Upload file lên MinIO (S3 API) — trả về s3:// URI."""
    if boto3 is None:
        raise ImportError("pip install boto3")

    client = boto3.client(
        "s3",
        endpoint_url=endpoint or DEFAULT_MINIO_ENDPOINT,
        aws_access_key_id=access_key or DEFAULT_MINIO_ACCESS_KEY,
        aws_secret_access_key=secret_key or DEFAULT_MINIO_SECRET_KEY,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
    client.upload_file(file_path, bucket, object_key)
    return f"s3://{bucket}/{object_key}"


def handle_awx_error(exc: Exception) -> str:
    """Chuyển exception sang thông báo tiếng Việt."""
    if requests and isinstance(exc, requests.HTTPError):
        if exc.response is not None and exc.response.status_code == 401:
            return "❌ AWX 401 Unauthorized — token sai hoặc hết hạn"
        return f"❌ AWX HTTP Error: {exc}"
    if isinstance(exc, ValueError):
        return f"❌ {exc}"
    if isinstance(exc, TimeoutError):
        return f"❌ {exc}"
    return f"❌ {exc}"


def save_json_report(data: dict, path: str) -> str:
    """Ghi dict ra file JSON — dùng cho pipeline report → MinIO."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return path
