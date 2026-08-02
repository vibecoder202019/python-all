"""
Module 12 — Dự án Bước 6: DevOps Toolkit CLI hoàn chỉnh

Chạy: python project/step06_final.py --help

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Gộp subcommand: disk-usage, parse-log, health-check, security-scan,
     live-or-die (website), filter-alerts (chống nhiễu).
  2. --demo chạy lần lượt các lệnh demo.
  3. Version 1.1.0; help đầy đủ cho mọi subcommand.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - --help liệt kê các subcommand.
  - --demo in output từng lệnh (disk, log, health, live-or-die, filter-alerts, security).
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
import time
from pathlib import Path

try:
    import httpx
except ImportError:
    httpx = None

from common import (
    disk_usage, parse_log_file, analyze_logs,
    scan_secrets, SKIP_DIRS,
)
from monitoring import (
    AlertEvent,
    AlertFilterConfig,
    AlertNoiseFilter,
    check_website,
    summarize_sites,
)

VERSION = "1.1.0"
MODULE_DIR = Path(__file__).parent.parent


def cmd_disk_usage(path: str):
    r = disk_usage(Path(path))
    print(f"📂 {r['path']}")
    print(f"   Files: {r['files']}  |  Size: {r['size_mb']} MB")


def cmd_parse_log(filepath: str):
    path = Path(filepath)
    if not path.exists():
        print(f"❌ Not found: {filepath}")
        return
    report = analyze_logs(parse_log_file(path))
    print(f"📋 {path.name} — {report['total']} entries, error rate: {report['error_rate']}%")
    for level, count in report["by_level"].items():
        print(f"   {level:8s}: {count}")


def cmd_health_check(urls: list[str]):
    if not urls:
        urls = ["https://api.github.com/zen", "https://www.google.com"]
    print("🏥 Health Check:")
    for url in urls:
        if httpx is None:
            print("   httpx not installed")
            return
        start = time.perf_counter()
        try:
            resp = httpx.get(url, timeout=5, follow_redirects=True)
            ms = (time.perf_counter() - start) * 1000
            icon = "✅" if resp.status_code < 400 else "❌"
            print(f"   {icon} {url} — HTTP {resp.status_code} ({ms:.0f}ms)")
        except Exception as e:
            ms = (time.perf_counter() - start) * 1000
            print(f"   ❌ {url} — {e} ({ms:.0f}ms)")


def cmd_security_scan(path: str):
    directory = Path(path)
    secrets = scan_secrets(directory)
    print(f"🔒 Security Scan: {directory}")
    print(f"   Secrets found: {len(secrets)}")
    for f in secrets:
        print(f"   ⚠️  [{f['type']}] {f['file']}:{f['line']}")
    print(f"   Result: {'✅ PASS' if not secrets else '⚠️  REVIEW NEEDED'}")


def cmd_live_or_die(urls: list[str]):
    """Website LIVE / DIE — rõ ràng hơn health-check generic."""
    sites = [(u, u) for u in urls] if urls else [
        ("Example", "https://example.com"),
        ("Dead local", "http://127.0.0.1:19999/"),
    ]
    print("🟢🔴 Website LIVE / DIE:")
    results = [check_website(name, url) for name, url in sites]
    for r in results:
        icon = "🟢" if r.state == "LIVE" else "🔴"
        print(f"   {icon} {r.state:4s}  {r.name:24s} {r.latency_ms:6.0f}ms  {r.reason}")
    s = summarize_sites(results)
    print(f"   Summary: {s['live']} LIVE / {s['die']} DIE")


def cmd_filter_alerts_demo():
    """Demo filter alert chống nhiễu (consecutive + cooldown + exclude)."""
    print("🔇 Alert noise filter:")
    cfg = AlertFilterConfig(
        min_severity="warning",
        consecutive_failures=3,
        cooldown_seconds=60.0,
        exclude_label_pairs=(("maintenance", "true"),),
        state_change_only=True,
    )
    filt = AlertNoiseFilter(cfg)
    stream = [
        AlertEvent("WebsiteDown", "critical", "firing", "a.example", message="fail 1"),
        AlertEvent("WebsiteDown", "critical", "firing", "a.example", message="fail 2"),
        AlertEvent("WebsiteDown", "critical", "firing", "a.example", message="fail 3 → alert"),
        AlertEvent("WebsiteDown", "critical", "firing", "a.example", message="spam cooldown"),
        AlertEvent("HighLatency", "info", "firing", "b.example", message="noise"),
        AlertEvent("WebsiteDown", "critical", "firing", "c.example",
                   labels={"maintenance": "true"}, message="planned"),
        AlertEvent("WebsiteDown", "critical", "resolved", "a.example", message="recovered"),
    ]
    sent = drop = 0
    for d in filt.process_batch(stream):
        if d.action == "SEND":
            sent += 1
            print(f"   📣 SEND  {d.alert.alertname}@{d.alert.instance} ({d.reason})")
        else:
            drop += 1
            print(f"   🔇 DROP  {d.alert.alertname}@{d.alert.instance} ({d.reason})")
    print(f"   Result: SEND={sent} DROP={drop}")


def cmd_report(path: str):
    """Tổng hợp report DevOps."""
    print(f"{'='*50}")
    print(f"  DevOps Toolkit Report v{VERSION}")
    print(f"{'='*50}\n")
    cmd_disk_usage(path)
    print()
    log_file = MODULE_DIR / "data" / "sample.log"
    if log_file.exists():
        cmd_parse_log(str(log_file))
    print()
    cmd_live_or_die([])
    print()
    cmd_filter_alerts_demo()
    print()
    cmd_security_scan(str(Path(path) / "data") if (Path(path) / "data").exists() else path)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devops-toolkit",
        description="DevOps & DevSecOps CLI Toolkit",
    )
    parser.add_argument("--version", action="version", version=f"devops-toolkit {VERSION}")
    parser.add_argument("--demo", action="store_true", help="Chạy demo tất cả commands")

    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("disk-usage", help="Phân tích disk usage")
    p.add_argument("--path", default=".")

    p = sub.add_parser("parse-log", help="Phân tích log file")
    p.add_argument("--file", default=str(MODULE_DIR / "data" / "sample.log"))

    p = sub.add_parser("health-check", help="Kiểm tra HTTP endpoints")
    p.add_argument("--url", action="append", default=[])

    p = sub.add_parser("live-or-die", help="Website LIVE / DIE check")
    p.add_argument("--url", action="append", default=[])

    p = sub.add_parser("filter-alerts", help="Demo filter alert chống nhiễu")

    p = sub.add_parser("security-scan", help="DevSecOps security audit")
    p.add_argument("--path", default=".")

    p = sub.add_parser("report", help="Tổng hợp DevOps report")
    p.add_argument("--path", default=str(MODULE_DIR))

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.demo:
        print(f"=== DevOps Toolkit v{VERSION} — Demo ===\n")
        cmd_disk_usage(str(MODULE_DIR))
        print()
        cmd_parse_log(str(MODULE_DIR / "data" / "sample.log"))
        print()
        cmd_health_check([])
        print()
        cmd_live_or_die([])
        print()
        cmd_filter_alerts_demo()
        print()
        cmd_security_scan(str(MODULE_DIR / "data"))
        return

    commands = {
        "disk-usage": lambda: cmd_disk_usage(args.path),
        "parse-log": lambda: cmd_parse_log(args.file),
        "health-check": lambda: cmd_health_check(args.url),
        "live-or-die": lambda: cmd_live_or_die(args.url),
        "filter-alerts": cmd_filter_alerts_demo,
        "security-scan": lambda: cmd_security_scan(args.path),
        "report": lambda: cmd_report(args.path),
    }

    if args.command in commands:
        commands[args.command]()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
