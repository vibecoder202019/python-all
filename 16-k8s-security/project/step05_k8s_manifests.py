"""Module 16 — Bước 5: Kiểm tra manifest K8s security."""
import sys
from pathlib import Path

def main():
    print("=== Bước 5: K8s Security Manifests ===\n")
    k8s = Path(__file__).parent.parent / "k8s"
    required = [
        "namespace.yaml", "networkpolicy.yaml", "ingress-secure.yaml",
        "deployment.yaml", "configmap-app.yaml", "hpa.yaml",
    ]
    for f in required:
        path = k8s / f
        print(f"  {'✅' if path.exists() else '❌'} {f}")
    print("\nDeploy: bash scripts/02-deploy-lab.sh")

if __name__ == "__main__":
    main()
