#!/usr/bin/env python3
"""Module 16 — Ví dụ 04: Phát hiện Port Scan từ log."""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "project"))
from common import detect_port_scan

def main():
    print("=== Ví dụ 04: Port Scan Detection ===\n")

    # Log bình thường — 1 IP, 2 port
    normal_log = [
        {"src_ip": "10.0.0.5", "dst_port": 80, "timestamp": time.time()},
        {"src_ip": "10.0.0.5", "dst_port": 443, "timestamp": time.time() + 0.5},
    ]
    alerts = detect_port_scan(normal_log, threshold=10)
    print(f"  Log bình thường: {len(alerts)} cảnh báo (mong đợi 0)")

    # Log port scan — 1 IP quét 15 port trong 3 giây
    now = time.time()
    scan_log = [
        {"src_ip": "10.0.0.99", "dst_port": port, "timestamp": now + i * 0.1}
        for i, port in enumerate(range(20, 35))
    ]
    alerts = detect_port_scan(scan_log, threshold=10, window_seconds=5)
    print(f"  Log port scan:   {len(alerts)} cảnh báo (mong đợi 1)")
    for a in alerts:
        print(f"    🚫 {a.detail}")

if __name__ == "__main__":
    main()
