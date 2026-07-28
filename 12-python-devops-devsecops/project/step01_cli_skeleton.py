"""
Dự án Bước 1 — CLI skeleton với argparse
Chạy: python project/step01_cli_skeleton.py --demo
"""
import argparse
import sys


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="devops-toolkit",
        description="DevOps Toolkit — CLI automation tool",
    )
    parser.add_argument("--demo", action="store_true", help="Chạy demo")
    parser.add_argument("--version", action="version", version="devops-toolkit 0.1.0")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.demo:
        print("=== DevOps Toolkit — Bước 1: CLI Skeleton ===")
        print("✓ argparse hoạt động")
        print("  python project/step01_cli_skeleton.py --help")
        print("  python project/step01_cli_skeleton.py --version")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
