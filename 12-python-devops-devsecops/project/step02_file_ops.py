"""
Module 12 — Dự án Bước 2: Lệnh disk-usage và list-files

Chạy: python project/step02_file_ops.py --demo

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Subcommand disk-usage: phân tích dung lượng thư mục (--path).
  2. Subcommand list-files: liệt kê file theo pattern (--pattern).
  3. --demo chạy cả hai lệnh trên thư mục module.

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - disk-usage: Path, Files, Size (MB).
  - list-files: top 10 file .py kèm size KB.
═══════════════════════════════════════════════════════════════════════════
"""
import argparse
from pathlib import Path
from common import disk_usage, SKIP_DIRS


def cmd_disk_usage(path: str):
    result = disk_usage(Path(path))
    print(f"Path:   {result['path']}")
    print(f"Files:  {result['files']}")
    print(f"Size:   {result['size_mb']} MB")


def cmd_list_files(path: str, pattern: str = "*.py"):
    base = Path(path)
    files = sorted(base.rglob(pattern))[:10]
    print(f"Top files matching '{pattern}' in {path}:")
    for f in files:
        if not any(s in f.parts for s in SKIP_DIRS):
            print(f"  {f.relative_to(base)}  ({f.stat().st_size // 1024} KB)")


def main():
    parser = argparse.ArgumentParser(prog="devops-toolkit")
    sub = parser.add_subparsers(dest="command")

    p_disk = sub.add_parser("disk-usage", help="Phân tích disk usage")
    p_disk.add_argument("--path", default=".", help="Thư mục cần quét")

    p_list = sub.add_parser("list-files", help="Liệt kê file")
    p_list.add_argument("--path", default=".")
    p_list.add_argument("--pattern", default="*.py")

    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    if args.demo or args.command == "disk-usage":
        print("=== Bước 2: File Operations ===\n")
        module_dir = Path(__file__).parent.parent
        cmd_disk_usage(str(module_dir))
        print()
        cmd_list_files(str(module_dir / "examples"))
    elif args.command == "list-files":
        cmd_list_files(args.path, args.pattern)
    elif args.command == "disk-usage":
        cmd_disk_usage(args.path)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
