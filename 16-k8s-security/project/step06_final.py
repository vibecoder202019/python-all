#!/usr/bin/env python3
"""Module 16 — Bước 6: Security CLI hoàn chỉnh."""
import argparse, json, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import (
    RateLimiter, detect_port_scan, detect_sql_injection,
    check_phishing_url, sanitize_input,
)

def cmd_sqli(args):
    r = detect_sql_injection(args.text)
    print(json.dumps({"passed": r.passed, "detail": r.detail}, ensure_ascii=False))
    sys.exit(0 if r.passed else 1)

def cmd_phishing(args):
    r = check_phishing_url(args.url)
    print(json.dumps({"passed": r.passed, "score": r.score, "detail": r.detail}, ensure_ascii=False))
    sys.exit(0 if r.passed else 1)

def cmd_ratelimit(args):
    limiter = RateLimiter(args.limit, args.window)
    for i in range(args.count):
        r = limiter.is_allowed(args.client)
        if not r.passed:
            print(f"Blocked at request #{i+1}")
            sys.exit(1)
    print(f"OK — {args.count} requests allowed")

def cmd_scan(args):
    now = time.time()
    log = [{"src_ip": args.ip, "dst_port": p, "timestamp": now + i * 0.1}
           for i, p in enumerate(range(args.from_port, args.to_port))]
    alerts = detect_port_scan(log, threshold=args.threshold)
    print(json.dumps([{"detail": a.detail, "score": a.score} for a in alerts], ensure_ascii=False))

def cmd_check_all(args):
    if args.demo:
        print("Security CLI — sqli | phishing | ratelimit | portscan | check-all")
        return
    tests = [
        ("SQLi safe", detect_sql_injection("hello").passed),
        ("SQLi block", not detect_sql_injection("' OR 1=1").passed),
        ("Phishing block", not check_phishing_url("http://login-verify.xyz").passed),
        ("Rate limit", RateLimiter(5, 10).is_allowed("x").passed),
    ]
    for name, ok in tests:
        print(f"  {'✅' if ok else '❌'} {name}")

def main():
    p = argparse.ArgumentParser(description="K8s Security CLI — Module 16")
    sub = p.add_subparsers(dest="cmd")

    s = sub.add_parser("sqli"); s.add_argument("text"); s.set_defaults(func=cmd_sqli)
    s = sub.add_parser("phishing"); s.add_argument("url"); s.set_defaults(func=cmd_phishing)
    s = sub.add_parser("ratelimit")
    s.add_argument("--client", default="127.0.0.1")
    s.add_argument("--count", type=int, default=10)
    s.add_argument("--limit", type=int, default=5)
    s.add_argument("--window", type=int, default=10)
    s.set_defaults(func=cmd_ratelimit)
    s = sub.add_parser("portscan")
    s.add_argument("--ip", default="10.0.0.1")
    s.add_argument("--from-port", type=int, default=20)
    s.add_argument("--to-port", type=int, default=40)
    s.add_argument("--threshold", type=int, default=10)
    s.set_defaults(func=cmd_scan)
    s = sub.add_parser("check-all"); s.add_argument("--demo", action="store_true"); s.set_defaults(func=cmd_check_all)

    args = p.parse_args()
    if not args.cmd:
        p.print_help(); return
    args.func(args)

if __name__ == "__main__":
    main()
