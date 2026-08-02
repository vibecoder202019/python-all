#!/usr/bin/env python3
"""Ví dụ 05 — Full flow demo: Terraform values → AWX task → (mô phỏng) K8s deploy."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "project"))

from awx_client import AwxClient, AwxConfig


def main() -> None:
    print("=== 05: Full platform flow (demo) ===\n")
    print("1) Terraform (đã plan/apply) → outputs: namespace, kube_context")
    tf_outputs = {
        "namespace": "platform-apps",
        "kube_context": "kind-lab-desktop",
        "workspace": "labs",
    }
    print(json.dumps(tf_outputs, indent=2))

    print("\n2) Backstage / API → Bridge → AWX launch")
    client = AwxClient(AwxConfig.from_env(force_demo=True))
    extra = {
        "app_name": "checkout-svc",
        "namespace": tf_outputs["namespace"],
        "image": "nginx:1.27-alpine",
        "replicas": 2,
        "cluster_context": tf_outputs["kube_context"],
        "terraform_workspace": tf_outputs["workspace"],
    }
    job = client.launch_job_template(7, extra_vars=extra)
    print(json.dumps({"job_id": job.get("id"), "status": job.get("status")}, indent=2))

    print("\n3) Ansible (trong AWX) apply k8s/ manifests với extra_vars trên")
    print("   → kubectl get deploy,svc -n platform-apps")
    print("\n✓ Flow demo hoàn tất — lab thật: scripts/03-run-bridge.sh + 05-deploy-k8s-demo.sh")


if __name__ == "__main__":
    main()
