#!/usr/bin/env python3
"""Ví dụ 02 — Launch job template (tạo task trên AWX)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from awx_client import AwxClient, AwxConfig


def main() -> None:
    print("=== 02: Launch AWX job (create task) ===\n")
    client = AwxClient(AwxConfig.from_env(force_demo=True))
    template_id = 7
    extra_vars = {"app_name": "demo-api", "namespace": "platform-apps", "replicas": 2}
    job = client.launch_job_template(template_id, extra_vars=extra_vars)
    print(json.dumps(job, indent=2, ensure_ascii=False))
    print(f"\n✓ Task tạo xong — job_id={job.get('id') or job.get('job')} status={job.get('status')}")


if __name__ == "__main__":
    main()
