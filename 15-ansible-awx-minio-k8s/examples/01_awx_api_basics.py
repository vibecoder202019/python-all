#!/usr/bin/env python3
"""
Module 15 — Ví dụ 01: Kết nối AWX API và liệt kê Job Template

Chạy:
  export AWX_URL="http://localhost:8052"
  export AWX_TOKEN="your-token"
  python examples/01_awx_api_basics.py

═══════════════════════════════════════════════════════════════════════════
HỌC ĐƯỢC GÌ:
  - AWX REST API dùng Bearer token
  - GET /api/v2/job_templates/ — liệt kê template
  - Cấu trúc response: {"count": N, "results": [...]}
═══════════════════════════════════════════════════════════════════════════
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import get_awx_client, handle_awx_error


def main():
    print("=== Ví dụ 01: AWX API Basics ===\n")

    try:
        ctx = get_awx_client()
        print(f"✅ Kết nối AWX: {ctx.base_url}\n")

        templates = ctx.client.list_job_templates()
        print(f"Tìm thấy {len(templates)} Job Template:\n")
        print(f"{'ID':>6}  {'Name':<40}")
        print("-" * 50)
        for t in templates:
            print(f"{t['id']:>6}  {t['name']:<40}")

    except Exception as e:
        print(handle_awx_error(e))
        print("\n💡 Gợi ý:")
        print("  kubectl port-forward svc/awx-service 8052:80 -n awx")
        print("  AWX UI → User → Tokens → Create → export AWX_TOKEN='...'")
        sys.exit(1)


if __name__ == "__main__":
    main()
