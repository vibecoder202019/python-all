#!/usr/bin/env python3
"""Module 16 — Ví dụ 06: Quét cấu hình bảo mật K8s (dry-run)."""
import argparse
import json
import sys
from pathlib import Path

# Rules kiểm tra manifest YAML cơ bản
SECURITY_RULES = [
    {
        "id": "NETPOL-001",
        "check": lambda m: m.get("kind") == "NetworkPolicy",
        "message": "Nên có NetworkPolicy giới hạn traffic pod",
    },
    {
        "id": "ING-001",
        "check": lambda m: (
            m.get("kind") == "Ingress"
            and "nginx.ingress.kubernetes.io/limit-rps" in m.get("metadata", {}).get("annotations", {})
        ),
        "message": "Ingress nên có rate limit annotation",
    },
    {
        "id": "SEC-001",
        "check": lambda m: (
            m.get("kind") == "Ingress"
            and "nginx.ingress.kubernetes.io/configuration-snippet" in m.get("metadata", {}).get("annotations", {})
        ),
        "message": "Ingress nên có security headers (configuration-snippet)",
    },
]


def load_yaml_files(directory: Path) -> list[dict]:
    """Đọc tất cả YAML trong thư mục (multi-doc)."""
    try:
        import yaml
    except ImportError:
        print("pip install pyyaml")
        sys.exit(1)

    manifests = []
    for f in sorted(directory.glob("**/*.yaml")):
        for doc in yaml.safe_load_all(f.read_text(encoding="utf-8")):
            if doc:
                manifests.append(doc)
    return manifests


def scan_manifests(manifests: list[dict]) -> list[dict]:
    findings = []
    for rule in SECURITY_RULES:
        found = any(rule["check"](m) for m in manifests)
        findings.append({"rule": rule["id"], "passed": found, "message": rule["message"]})
    return findings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--demo", action="store_true")
    args = parser.parse_args()

    k8s_dir = Path(__file__).parent.parent / "k8s"
    print("=== Ví dụ 06: K8s Security Scanner ===\n")

    if args.demo or not k8s_dir.exists():
        print("🔍 DEMO — rules kiểm tra:")
        for r in SECURITY_RULES:
            print(f"  [{r['id']}] {r['message']}")
        return

    manifests = load_yaml_files(k8s_dir)
    print(f"Đọc {len(manifests)} manifest từ k8s/\n")

    for finding in scan_manifests(manifests):
        icon = "✅" if finding["passed"] else "⚠️ "
        print(f"  {icon} [{finding['rule']}] {finding['message']}")

    print(f"\n{json.dumps(scan_manifests(manifests), indent=2, ensure_ascii=False)}")


if __name__ == "__main__":
    main()
