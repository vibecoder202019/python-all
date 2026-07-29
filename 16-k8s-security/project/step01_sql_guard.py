"""Module 16 — Bước 1: SQL Injection Guard."""
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import detect_sql_injection

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="' OR 1=1--")
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()
    print("=== Bước 1: SQL Injection Guard ===\n")
    if args.demo:
        for p in ["admin", "' OR 1=1--", "normal search"]:
            r = detect_sql_injection(p)
            print(f"  {'✅' if r.passed else '🚫'} {p!r}")
        return
    r = detect_sql_injection(args.input)
    print(f"{'✅ AN TOÀN' if r.passed else '🚫 CHẶN'}: {r.detail}")

if __name__ == "__main__":
    main()
