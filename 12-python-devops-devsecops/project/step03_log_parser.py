"""
Module 12 — Dự án Bước 3: Lệnh parse-log

Chạy: python project/step03_log_parser.py --demo

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Subcommand parse-log phân tích file log qua common.parse_log_file.
  2. In thống kê total, error_rate, by_level và danh sách ERROR.
  3. --demo dùng data/sample.log mặc định.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "Log: sample.log (N entries)" và error rate %.
  - Đếm theo level; liệt kê errors nếu có.
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
from pathlib import Path
from common import parse_log_file, analyze_logs


def cmd_parse_log(filepath: str):
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        return
    entries = parse_log_file(path)
    report = analyze_logs(entries)
    print(f"Log: {path.name} ({report['total']} entries)")
    print(f"Error rate: {report['error_rate']}%")
    for level, count in report["by_level"].items():
        print(f"  {level:8s}: {count}")
    if report["errors"]:
        print("\nErrors:")
        for e in report["errors"]:
            print(f"  [{e['timestamp']}] {e['message']}")


def main():
    parser = argparse.ArgumentParser(prog="devops-toolkit")
    sub = parser.add_subparsers(dest="command")

    p_log = sub.add_parser("parse-log", help="Phân tích log file")
    p_log.add_argument("--file", required=False, help="Log file path")

    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    module_dir = Path(__file__).parent.parent
    log_file = str(module_dir / "data" / "sample.log")

    if args.demo:
        print("=== Bước 3: Log Parser ===\n")
        cmd_parse_log(log_file)
    elif args.command == "parse-log":
        cmd_parse_log(args.file or log_file)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
