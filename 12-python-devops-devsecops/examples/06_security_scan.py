"""
Module 12 — Ví dụ 6: DevSecOps Security Scanning

Chạy: python examples/06_security_scan.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Quét thư mục data/ tìm secret hardcode (API key, AWS key, private key).
  2. Quét file world-writable (permission 0o002).
  3. Phát hiện file .env (trừ .env.example).

KẾT QUẢ MONG ĐỢI (in ra terminal):
  - "🔑 Secret scan: N finding(s)" — có thể > 0 nếu data có sample secret.
  - "🔒 Permission scan" và "📁 Env files".
  - "Result: ✅ PASS" hoặc "⚠️  N issue(s) found".
═══════════════════════════════════════════════════════════════════════════
"""
import os
import re
from pathlib import Path

MODULE_DIR = Path(__file__).parent.parent
SCAN_DIR = MODULE_DIR / "data"

SECRET_PATTERNS = [
    (r"(?i)(api[_-]?key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]", "Hardcoded secret"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key"),
    (r"-----BEGIN (RSA |EC )?PRIVATE KEY-----", "Private key"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Personal Access Token"),
]

DANGEROUS_PERMISSIONS = 0o777
SKIP_DIRS = {".venv", "__pycache__", ".git", "node_modules"}


def scan_secrets(directory: Path) -> list[dict]:
    findings = []
    for filepath in directory.rglob("*"):
        if not filepath.is_file():
            continue
        if any(skip in filepath.parts for skip in SKIP_DIRS):
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
                    "snippet": match.group()[:50] + "...",
                })
    return findings


def scan_permissions(directory: Path) -> list[dict]:
    findings = []
    for filepath in directory.rglob("*"):
        if not filepath.is_file() or any(skip in filepath.parts for skip in SKIP_DIRS):
            continue
        mode = filepath.stat().st_mode & 0o777
        if mode & 0o002:  # world-writable
            findings.append({
                "file": str(filepath.relative_to(directory)),
                "permissions": oct(mode),
                "issue": "World-writable file",
            })
    return findings


def scan_env_files(directory: Path) -> list[dict]:
    findings = []
    for env_file in directory.rglob(".env*"):
        if env_file.name == ".env.example":
            continue
        if env_file.is_file():
            findings.append({
                "file": str(env_file.relative_to(directory)),
                "issue": "Env file detected — ensure not committed to git",
            })
    return findings


print("=== DevSecOps Security Scan ===\n")
print(f"Scanning: {SCAN_DIR}\n")

secrets = scan_secrets(SCAN_DIR)
permissions = scan_permissions(SCAN_DIR)
env_files = scan_env_files(SCAN_DIR)

print(f"🔑 Secret scan: {len(secrets)} finding(s)")
for f in secrets:
    print(f"   [{f['type']}] {f['file']}:{f['line']}")
    print(f"      {f['snippet']}")

print(f"\n🔒 Permission scan: {len(permissions)} finding(s)")
for f in permissions[:5]:
    print(f"   {f['file']} ({f['permissions']}) — {f['issue']}")

print(f"\n📁 Env files: {len(env_files)} finding(s)")
for f in env_files:
    print(f"   {f['file']} — {f['issue']}")

total = len(secrets) + len(permissions) + len(env_files)
status = "✅ PASS" if total == 0 else f"⚠️  {total} issue(s) found"
print(f"\nResult: {status}")
print("\n✓ Done")
