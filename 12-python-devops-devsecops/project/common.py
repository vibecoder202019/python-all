"""
Module 12 — Tiện ích dùng chung cho dự án DevOps Toolkit

Cung cấp regex phân tích log, mẫu quét secret, và các hàm helper cho
disk usage, parse log, quét bảo mật — dùng lại ở step03→step06.

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Định nghĩa pattern regex đọc log dạng [timestamp] LEVEL: message.
  2. Định nghĩa danh sách pattern phát hiện secret (API key, AWS key, GitHub token).
  3. Cung cấp hàm parse_log_file, analyze_logs, scan_secrets, disk_usage.

KẾT QUẢ MONG ĐỢI:
  - parse_log_file trả list dict {timestamp, level, message}.
  - analyze_logs trả thống kê total, by_level, errors, error_rate.
  - scan_secrets trả list finding {file, type, line}.
  - disk_usage trả {path, files, size_mb}.
═══════════════════════════════════════════════════════════════════════════
"""
import re
from collections import Counter
from pathlib import Path

# ── Regex đọc dòng log: [2024-01-15 10:30:00] INFO: message ──
LOG_PATTERN = re.compile(
    r"\[(?P<timestamp>[\d-]+ [\d:]+)\] (?P<level>\w+): (?P<message>.+)"
)

# ── Các pattern DevSecOps — (regex, mô tả loại secret) ──
SECRET_PATTERNS = [
    (r"(?i)(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]", "Hardcoded secret"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Token"),
]

# ── Thư mục bỏ qua khi quét file (tránh quét cache, venv, git) ──
SKIP_DIRS = {".venv", "__pycache__", ".git", "node_modules"}


def parse_log_file(filepath: Path) -> list[dict]:
    """Đọc file log, trả list entry khớp LOG_PATTERN."""
    entries = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        match = LOG_PATTERN.match(line.strip())
        if match:
            entries.append(match.groupdict())
    return entries


def analyze_logs(entries: list[dict]) -> dict:
    """Thống kê log: đếm theo level, tính error_rate (%)."""
    levels = Counter(e["level"] for e in entries)
    errors = [e for e in entries if e["level"] == "ERROR"]
    return {
        "total": len(entries),
        "by_level": dict(levels),
        "errors": errors,
        "error_rate": round(len(errors) / len(entries) * 100, 1) if entries else 0,
    }


def scan_secrets(directory: Path) -> list[dict]:
    """Quét thư mục tìm secret hardcode — trả {file, type, line}."""
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
    """Tính tổng số file và dung lượng (MB) trong thư mục."""
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
