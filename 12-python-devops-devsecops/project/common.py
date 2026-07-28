"""Shared utilities for DevOps Toolkit project."""
import re
from collections import Counter
from pathlib import Path

LOG_PATTERN = re.compile(
    r"\[(?P<timestamp>[\d-]+ [\d:]+)\] (?P<level>\w+): (?P<message>.+)"
)

SECRET_PATTERNS = [
    (r"(?i)(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]", "Hardcoded secret"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Token"),
]

SKIP_DIRS = {".venv", "__pycache__", ".git", "node_modules"}


def parse_log_file(filepath: Path) -> list[dict]:
    entries = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        match = LOG_PATTERN.match(line.strip())
        if match:
            entries.append(match.groupdict())
    return entries


def analyze_logs(entries: list[dict]) -> dict:
    levels = Counter(e["level"] for e in entries)
    errors = [e for e in entries if e["level"] == "ERROR"]
    return {
        "total": len(entries),
        "by_level": dict(levels),
        "errors": errors,
        "error_rate": round(len(errors) / len(entries) * 100, 1) if entries else 0,
    }


def scan_secrets(directory: Path) -> list[dict]:
    findings = []
    for filepath in directory.rglob("*"):
        if not filepath.is_file() or any(s in filepath.parts for s in SKIP_DIRS):
            continue
        try:
            content = filepath.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for pattern, desc in SECRET_PATTERNS:
            for match in re.finditer(pattern, content):
                findings.append({
                    "file": str(filepath.relative_to(directory)),
                    "type": desc,
                    "line": content[:match.start()].count("\n") + 1,
                })
    return findings


def disk_usage(path: Path) -> dict:
    total_size = 0
    file_count = 0
    for f in path.rglob("*"):
        if f.is_file() and not any(s in f.parts for s in SKIP_DIRS):
            total_size += f.stat().st_size
            file_count += 1
    return {
        "path": str(path),
        "files": file_count,
        "size_mb": round(total_size / (1024 * 1024), 2),
    }
