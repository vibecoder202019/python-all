#!/usr/bin/env python3
"""Test Agent Bridge API — không cần n8n."""
import argparse
import json
import os
import sys

import httpx

BASE = os.environ.get("BRIDGE_URL", "http://localhost:8090")
API_KEY = os.environ.get("BRIDGE_API_KEY", "")


def headers():
    h = {"Content-Type": "application/json"}
    if API_KEY:
        h["X-API-Key"] = API_KEY
    return h


def demo():
    print("=== DEMO — mô phỏng gọi bridge (không cần server) ===")
    print("POST /agent/run intent=list_templates")
    print('POST /agent/run intent=launch_job template_name="Python Hello World"')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    parser.add_argument("--intent", default="list_templates")
    parser.add_argument("--template-name")
    parser.add_argument("--job-id", type=int)
    args = parser.parse_args()

    if args.demo:
        demo()
        return

    payload = {"intent": args.intent}
    if args.template_name:
        payload["template_name"] = args.template_name
    if args.job_id:
        payload["job_id"] = args.job_id

    try:
        r = httpx.get(f"{BASE}/health", timeout=10)
        r.raise_for_status()
        print(f"Health: {r.json()}\n")

        r = httpx.post(f"{BASE}/agent/run", json=payload, headers=headers(), timeout=120)
        r.raise_for_status()
        print(json.dumps(r.json(), indent=2))
    except httpx.ConnectError:
        print(f"❌ Không kết nối {BASE} — chạy: bash scripts/04-run-agent-bridge.sh")
        sys.exit(1)


if __name__ == "__main__":
    main()
