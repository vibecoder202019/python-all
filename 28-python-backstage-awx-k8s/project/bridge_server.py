#!/usr/bin/env python3
"""
Platform Bridge API — Backstage / curl gọi để tạo task AWX (deploy K8s).

Chạy (demo):
  AWX_DEMO=true uvicorn bridge_server:app --app-dir project --reload --port 8090

Endpoints chính:
  POST /api/v1/jobs          — tạo task AWX (launch job template)
  POST /api/v1/deploy        — shortcut deploy app → K8s qua AWX
  POST /api/scaffolder/run   — payload Backstage Software Template
"""
from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from awx_client import AwxClient, AwxConfig  # noqa: E402
from backstage_catalog import (  # noqa: E402
    build_catalog_documents,
    render_catalog_yaml,
)

API_KEY = os.environ.get("BRIDGE_API_KEY", "")
ORG = os.environ.get("BACKSTAGE_ORG", "default")
SYSTEM = os.environ.get("BACKSTAGE_SYSTEM", "platform")
DEFAULT_DEPLOY_TEMPLATE = int(
    os.environ.get("AWX_DEPLOY_TEMPLATE_ID", os.environ.get("AWX_DEFAULT_JOB_TEMPLATE_ID", "7"))
)

app = FastAPI(
    title="Platform Bridge — Backstage ↔ AWX ↔ K8s",
    description="Module 28: tạo task AWX từ API / Backstage Scaffolder để deploy Kubernetes",
    version="1.0.0",
)


def _client() -> AwxClient:
    return AwxClient(AwxConfig.from_env())


def _auth(x_api_key: str | None) -> None:
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid X-API-Key")


class LaunchJobRequest(BaseModel):
    template_id: int | None = None
    template_name: str | None = None
    extra_vars: dict[str, Any] = Field(default_factory=dict)
    wait: bool = False
    limit: str | None = None


class DeployRequest(BaseModel):
    """Deploy microservice lên K8s qua AWX job template."""

    app_name: str = Field(..., min_length=1, examples=["demo-api"])
    namespace: str = Field(default="platform-apps", examples=["platform-apps"])
    image: str = Field(..., examples=["ghcr.io/example/demo-api:1.0.0"])
    replicas: int = Field(default=2, ge=1, le=20)
    template_id: int | None = None
    wait: bool = False
    # Terraform outputs (optional) — truyền tiếp vào Ansible extra_vars
    terraform_workspace: str | None = None
    cluster_context: str | None = None


class ScaffolderRunRequest(BaseModel):
    """Payload tối giản từ Backstage template action (http:backstage:request)."""

    values: dict[str, Any] = Field(default_factory=dict)
    wait: bool = False


@app.get("/health")
def health() -> dict[str, Any]:
    cfg = AwxConfig.from_env()
    return {
        "status": "ok",
        "demo_mode": cfg.demo,
        "awx_url": cfg.base_url or None,
        "default_deploy_template_id": DEFAULT_DEPLOY_TEMPLATE,
    }


@app.get("/api/v1/templates")
def list_templates(x_api_key: str | None = Header(default=None)) -> dict[str, Any]:
    _auth(x_api_key)
    templates = _client().list_job_templates()
    return {"count": len(templates), "results": templates}


@app.post("/api/v1/jobs")
def create_job(
    body: LaunchJobRequest,
    x_api_key: str | None = Header(default=None),
) -> dict[str, Any]:
    """Tạo task trên Ansible AWX (POST job_templates/{id}/launch)."""
    _auth(x_api_key)
    client = _client()
    template_id = body.template_id
    if template_id is None and body.template_name:
        tmpl = client.get_template_by_name(body.template_name)
        if not tmpl:
            raise HTTPException(404, f"Template not found: {body.template_name}")
        template_id = int(tmpl["id"])
    if template_id is None:
        template_id = client.config.default_template_id or DEFAULT_DEPLOY_TEMPLATE
    try:
        job = client.launch_job_template(
            template_id,
            extra_vars=body.extra_vars or None,
            limit=body.limit,
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    job_id = job.get("id") or job.get("job")
    result: dict[str, Any] = {"job": job, "job_id": job_id, "template_id": template_id}
    if body.wait and job_id:
        result["final"] = client.wait_for_job(int(job_id))
    return result


@app.get("/api/v1/jobs/{job_id}")
def get_job(job_id: int, x_api_key: str | None = Header(default=None)) -> dict[str, Any]:
    _auth(x_api_key)
    try:
        return _client().get_job(job_id)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@app.post("/api/v1/deploy")
def deploy_to_k8s(
    body: DeployRequest,
    x_api_key: str | None = Header(default=None),
) -> dict[str, Any]:
    """Shortcut: tạo AWX task deploy app vào Kubernetes."""
    _auth(x_api_key)
    extra = {
        "app_name": body.app_name,
        "namespace": body.namespace,
        "image": body.image,
        "replicas": body.replicas,
    }
    if body.terraform_workspace:
        extra["terraform_workspace"] = body.terraform_workspace
    if body.cluster_context:
        extra["cluster_context"] = body.cluster_context

    req = LaunchJobRequest(
        template_id=body.template_id or DEFAULT_DEPLOY_TEMPLATE,
        extra_vars=extra,
        wait=body.wait,
    )
    result = create_job(req, x_api_key=x_api_key)
    result["deploy"] = extra
    return result


@app.post("/api/scaffolder/run")
def scaffolder_run(
    body: ScaffolderRunRequest,
    x_api_key: str | None = Header(default=None),
) -> dict[str, Any]:
    """Backstage Software Template → map values → /api/v1/deploy."""
    _auth(x_api_key)
    v = body.values
    deploy = DeployRequest(
        app_name=str(v.get("app_name") or v.get("name") or "demo-app"),
        namespace=str(v.get("namespace") or "platform-apps"),
        image=str(v.get("image") or "nginx:1.27-alpine"),
        replicas=int(v.get("replicas") or 2),
        template_id=int(v["template_id"]) if v.get("template_id") else None,
        wait=body.wait,
        terraform_workspace=v.get("terraform_workspace"),
        cluster_context=v.get("cluster_context"),
    )
    return deploy_to_k8s(deploy, x_api_key=x_api_key)


@app.get("/api/backstage/catalog.yaml", response_class=PlainTextResponse)
def catalog_yaml(x_api_key: str | None = Header(default=None)) -> str:
    _auth(x_api_key)
    docs = build_catalog_documents(_client().list_job_templates(), org=ORG, system=SYSTEM)
    return render_catalog_yaml(docs)
