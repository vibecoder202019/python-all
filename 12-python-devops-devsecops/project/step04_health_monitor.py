"""
Module 12 — Dự án Bước 4: Health-check monitor

Chạy: python project/step04_health_monitor.py --demo

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Subcommand health-check ping danh sách URL (--urls hoặc mặc định).
  2. Đo response time và phân loại healthy/unhealthy/unreachable.
  3. --demo chạy health check + parse-log mẫu.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - ✅/❌ cho từng endpoint kèm status và ms.
  - Demo kết hợp log analysis nếu có sample.log.
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
import time
from dataclasses import dataclass
from pathlib import Path

try:
    import httpx
except ImportError:
    httpx = None

from common import parse_log_file, analyze_logs


@dataclass
class HealthResult:
    name: str
    url: str
    status: str
    response_time_ms: float
    message: str


def check_url(name: str, url: str, timeout: float = 5.0) -> HealthResult:
    if httpx is None:
        return HealthResult(name, url, "skip", 0, "httpx not installed")
    start = time.perf_counter()
    try:
        resp = httpx.get(url, timeout=timeout, follow_redirects=True)
        elapsed = (time.perf_counter() - start) * 1000
        status = "healthy" if resp.status_code < 400 else "unhealthy"
        return HealthResult(name, url, status, round(elapsed, 1), f"HTTP {resp.status_code}")
    except Exception as e:
        elapsed = (time.perf_counter() - start) * 1000
        return HealthResult(name, url, "unreachable", round(elapsed, 1), str(e)[:60])


def cmd_health_check(urls: list[tuple[str, str]]):
    print("Health Check Report:")
    for name, url in urls:
        r = check_url(name, url)
        icon = "✅" if r.status == "healthy" else "❌"
        print(f"  {icon} {r.name:20s} {r.status:12s} {r.response_time_ms:6.0f}ms  {r.message}")


def main():
    parser = argparse.ArgumentParser(prog="devops-toolkit")
    sub = parser.add_subparsers(dest="command")

    p_hc = sub.add_parser("health-check", help="Kiểm tra health endpoints")
    p_hc.add_argument("--url", action="append", default=[])

    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    default_urls = [
        ("GitHub API", "https://api.github.com/zen"),
        ("Google", "https://www.google.com"),
    ]

    if args.demo:
        print("=== Bước 4: Health Monitor ===\n")
        cmd_health_check(default_urls)
    elif args.command == "health-check":
        urls = [(u, u) for u in args.url] if args.url else default_urls
        cmd_health_check(urls)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
