"""
Module 15 — Dự án Bước 4: Python script cho Ansible AWX

Chạy: python project/step04_ansible_script.py --name "DevOps"
"""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", default="Step04")
    args = parser.parse_args()

    script = Path(__file__).parent.parent / "examples" / "04_python_script_for_ansible.py"

    print("=== Bước 4: Ansible Script Module ===\n")
    print("AWX playbook gọi:")
    print(f'  script: examples/04_python_script_for_ansible.py --name "{args.name}"\n')

    result = subprocess.run(
        [sys.executable, str(script), "--name", args.name],
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
