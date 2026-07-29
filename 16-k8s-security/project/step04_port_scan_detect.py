"""Module 16 — Bước 4: Port Scan Detector."""
import sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import detect_port_scan

def main():
    print("=== Bước 4: Port Scan Detector ===\n")
    now = time.time()
    scan = [{"src_ip": "10.0.0.77", "dst_port": p, "timestamp": now + i * 0.05}
            for i, p in enumerate(range(1, 25))]
    alerts = detect_port_scan(scan, threshold=10)
    print(f"  Phát hiện {len(alerts)} cảnh báo port scan")
    for a in alerts:
        print(f"  🚫 {a.detail}")

if __name__ == "__main__":
    main()
