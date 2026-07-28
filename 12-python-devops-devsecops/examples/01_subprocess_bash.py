"""
DevOps 01 — Chạy lệnh Bash/Shell từ Python
Chạy: python examples/01_subprocess_bash.py
"""
import subprocess
import shlex
import sys
from datetime import datetime


def run_command(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    """Chạy lệnh shell an toàn."""
    print(f"  $ {cmd}")
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True, check=check
    )
    if result.stdout.strip():
        print(f"    stdout: {result.stdout.strip()[:200]}")
    if result.stderr.strip():
        print(f"    stderr: {result.stderr.strip()[:200]}")
    return result


def run_command_safe(cmd: str) -> tuple[int, str, str]:
    """Chạy lệnh không raise exception — trả (returncode, stdout, stderr)."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


print("=== Subprocess & Bash Automation ===\n")

print("1. Thông tin hệ thống:")
run_command("uname -s")
run_command("python3 --version")

print("\n2. Liệt kê file (5 file đầu):")
run_command("ls -la | head -6")

print("\n3. Disk usage:")
run_command("df -h . | tail -1")

print("\n4. Chạy lệnh an toàn (không crash nếu fail):")
code, out, err = run_command_safe("git status --short 2>/dev/null | head -3")
print(f"    returncode={code}")

print("\n5. Pipeline — đếm file Python:")
code, out, _ = run_command_safe("find . -name '*.py' 2>/dev/null | wc -l")
print(f"    Số file .py: {out.strip()}")

print(f"\n✓ Hoàn thành lúc {datetime.now().strftime('%H:%M:%S')}")
