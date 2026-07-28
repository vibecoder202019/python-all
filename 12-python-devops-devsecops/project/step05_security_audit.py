"""
Module 12 — Dự án Bước 5: Security-scan (DevSecOps)

Chạy: python project/step05_security_audit.py --demo

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Subcommand security-scan quét secret qua common.scan_secrets.
  2. Phát hiện file .env và .env.local.
  3. In kết quả PASS hoặc số issue tìm thấy.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "🔑 Secrets: N finding(s)" với file:line.
  - "📁 .env files: N" và "Result: ✅ PASS" hoặc "⚠️  N issue(s)".
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
from pathlib import Path
from common import scan_secrets, disk_usage


def cmd_security_scan(path: str):
    directory = Path(path)
    print(f"Security Scan: {directory}\n")

    secrets = scan_secrets(directory)
    print(f"🔑 Secrets: {len(secrets)} finding(s)")
    for f in secrets:
        print(f"   [{f['type']}] {f['file']}:{f['line']}")

    env_files = list(directory.rglob(".env")) + list(directory.rglob(".env.local"))
    env_files = [f for f in env_files if f.is_file()]
    print(f"\n📁 .env files: {len(env_files)}")
    for f in env_files:
        print(f"   ⚠️  {f.relative_to(directory)}")

    total = len(secrets) + len(env_files)
    print(f"\nResult: {'✅ PASS' if total == 0 else f'⚠️  {total} issue(s)'}")


def main():
    parser = argparse.ArgumentParser(prog="devops-toolkit")
    sub = parser.add_subparsers(dest="command")

    p_sec = sub.add_parser("security-scan", help="DevSecOps security audit")
    p_sec.add_argument("--path", default=".")

    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    module_dir = Path(__file__).parent.parent

    if args.demo:
        print("=== Bước 5: Security Audit ===\n")
        cmd_security_scan(str(module_dir / "data"))
    elif args.command == "security-scan":
        cmd_security_scan(args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
