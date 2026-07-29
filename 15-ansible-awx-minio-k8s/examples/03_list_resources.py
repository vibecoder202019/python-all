#!/usr/bin/env python3
"""
Module 15 — Ví dụ 03: Liệt kê AWX resources (templates, projects, jobs)

Chạy:
  python examples/03_list_resources.py templates
  python examples/03_list_resources.py jobs
  python examples/03_list_resources.py --demo
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import get_awx_client, handle_awx_error

ENDPOINTS = {
    "templates": "/job_templates/",
    "projects": "/projects/",
    "inventories": "/inventories/",
    "jobs": "/jobs/",
}


def demo_mode():
    print("=== DEMO: AWX Resources ===\n")
    print("templates  → GET /api/v2/job_templates/")
    print("projects   → GET /api/v2/projects/")
    print("jobs       → GET /api/v2/jobs/")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("resource", nargs="?", choices=list(ENDPOINTS.keys()))
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    if args.demo:
        demo_mode()
        return

    if not args.resource:
        print("Usage: python 03_list_resources.py <templates|projects|jobs>")
        sys.exit(1)

    print(f"=== Ví dụ 03: List {args.resource} ===\n")

    try:
        ctx = get_awx_client()
        result = ctx.client.get(ENDPOINTS[args.resource], params={"page_size": 20})
        items = result.get("results", [])

        for item in items:
            name = item.get("name", item.get("job_template_name", "?"))
            extra = ""
            if args.resource == "jobs":
                extra = f"[{item.get('status')}]"
            print(f"  id={item['id']:4d}  {name}  {extra}")

    except Exception as e:
        print(handle_awx_error(e))
        sys.exit(1)


if __name__ == "__main__":
    main()
