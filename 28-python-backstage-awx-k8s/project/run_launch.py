#!/usr/bin/env python3
"""CLI: list templates / launch AWX job (tạo task)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from awx_client import AwxClient, AwxConfig


def main() -> int:
    p = argparse.ArgumentParser(description="Module 28 — AWX launch CLI")
    p.add_argument("--demo", action="store_true", help="Dùng fixture, không gọi AWX thật")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="Liệt kê job templates")

    launch = sub.add_parser("launch", help="Tạo task (launch job template)")
    launch.add_argument("--template-id", type=int, default=None)
    launch.add_argument("--template-name", default=None)
    launch.add_argument("--extra-vars", default="{}", help='JSON extra_vars, vd: \'{"replicas":3}\'')
    launch.add_argument("--wait", action="store_true")

    deploy = sub.add_parser("deploy", help="Deploy app lên K8s qua AWX")
    deploy.add_argument("--app-name", required=True)
    deploy.add_argument("--namespace", default="platform-apps")
    deploy.add_argument("--image", required=True)
    deploy.add_argument("--replicas", type=int, default=2)
    deploy.add_argument("--template-id", type=int, default=7)
    deploy.add_argument("--wait", action="store_true")

    args = p.parse_args()
    client = AwxClient(AwxConfig.from_env(force_demo=args.demo))

    if args.cmd == "list":
        for t in client.list_job_templates():
            print(f"  [{t['id']}] {t['name']} — {t.get('playbook', '')}")
        return 0

    if args.cmd == "launch":
        tid = args.template_id
        if tid is None and args.template_name:
            tmpl = client.get_template_by_name(args.template_name)
            if not tmpl:
                print(f"Không tìm thấy template: {args.template_name}", file=sys.stderr)
                return 1
            tid = int(tmpl["id"])
        if tid is None:
            tid = client.config.default_template_id or 7
        extra = json.loads(args.extra_vars)
        job = client.launch_job_template(tid, extra_vars=extra or None)
        print(json.dumps(job, indent=2, ensure_ascii=False))
        job_id = job.get("id") or job.get("job")
        if args.wait and job_id:
            print("--- final ---")
            print(json.dumps(client.wait_for_job(int(job_id)), indent=2, ensure_ascii=False))
        return 0

    if args.cmd == "deploy":
        extra = {
            "app_name": args.app_name,
            "namespace": args.namespace,
            "image": args.image,
            "replicas": args.replicas,
        }
        job = client.launch_job_template(args.template_id, extra_vars=extra)
        print(json.dumps(job, indent=2, ensure_ascii=False))
        job_id = job.get("id") or job.get("job")
        if args.wait and job_id:
            print(json.dumps(client.wait_for_job(int(job_id)), indent=2, ensure_ascii=False))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
