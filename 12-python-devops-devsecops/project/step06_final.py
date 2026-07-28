"""
Dự án Bước 6 — DevOps Toolkit CLI hoàn chỉnh
Chạy: python project/step06_final.py --help
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

VERSION = "1.0.0"
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
        cmd_security_scan(str(MODULE_DIR / "data"))
        return

    commands = {
        "disk-usage": lambda: cmd_disk_usage(args.path),
        "parse-log": lambda: cmd_parse_log(args.file),
        "health-check": lambda: cmd_health_check(args.url),
        "security-scan": lambda: cmd_security_scan(args.path),
        "report": lambda: cmd_report(args.path),
    }

    if args.command in commands:
        commands[args.command]()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
