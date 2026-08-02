#!/usr/bin/env python3
"""Ví dụ 03 — Gọi Bridge API tạo deploy task (giả lập HTTP client nội bộ)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from awx_client import AwxClient, AwxConfig


def main() -> None:
    print("=== 03: Bridge-style deploy payload → AWX ===\n")
    # Trong lab thật: curl POST http://127.0.0.1:8090/api/v1/deploy
    # Ở đây gọi thẳng client — cùng semantics với bridge.
    client = AwxClient(AwxConfig.from_env(force_demo=True))
    payload = {
        "app_name": "payments-api",
        "namespace": "platform-apps",
        "image": "ghcr.io/example/payments-api:1.4.2",
        "replicas": 3,
        "terraform_workspace": "labs-us-east-1",
    }
    print("Request body:")
    for k, v in payload.items():
        print(f"  {k}: {v}")

    job = client.launch_job_template(7, extra_vars=payload)
    print(f"\n✓ AWX job {job.get('id')} → {job.get('status')}")
    print("  (Ansible playbook sẽ apply Deployment/Service lên K8s)")


if __name__ == "__main__":
    main()
