"""
DevOps 03 — Log Analyzer
Chạy: python examples/03_log_analyzer.py
"""
import re
from collections import Counter
from datetime import datetime
from pathlib import Path

MODULE_DIR = Path(__file__).parent.parent
LOG_FILE = MODULE_DIR / "data" / "sample.log"

LOG_PATTERN = re.compile(
    r"\[(?P<timestamp>[\d-]+ [\d:]+)\] (?P<level>\w+): (?P<message>.+)"
)


def parse_log(filepath: Path) -> list[dict]:
    entries = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        match = LOG_PATTERN.match(line.strip())
        if match:
            entries.append(match.groupdict())
    return entries


def analyze(entries: list[dict]) -> dict:
    levels = Counter(e["level"] for e in entries)
    errors = [e for e in entries if e["level"] == "ERROR"]
    return {
        "total_lines": len(entries),
        "by_level": dict(levels),
        "error_count": len(errors),
        "errors": errors,
        "error_rate": round(len(errors) / len(entries) * 100, 1) if entries else 0,
    }


print("=== Log Analyzer ===\n")

if not LOG_FILE.exists():
    print(f"Log file not found: {LOG_FILE}")
    print("Chạy: bash scripts/setup.sh")
    exit(1)

entries = parse_log(LOG_FILE)
report = analyze(entries)

print(f"File: {LOG_FILE.name}")
print(f"Total entries: {report['total_lines']}")
print(f"\nBy level:")
for level, count in report["by_level"].items():
    bar = "█" * count
    print(f"  {level:8s} {count:3d} {bar}")

print(f"\nError rate: {report['error_rate']}%")
if report["errors"]:
    print("\nErrors:")
    for e in report["errors"]:
        print(f"  [{e['timestamp']}] {e['message']}")

print("\n✓ Done")
