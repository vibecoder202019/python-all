# DevSecOps pipeline — lý thuyết & best practices

## Shift-left security

Đưa kiểm tra bảo mật **sớm** (commit / PR), không chờ production bị exploit.

```
Dev laptop          CI (PR)              Staging           Prod
pre-commit    →   secrets/SAST/SCA  →   DAST/ZAP     →   monitor
gitleaks          Trivy + SBOM          OIDC deploy       runtime
```

## Các lớp bắt buộc (baseline 2025+)

1. **Secrets** — Gitleaks trên full history PR  
2. **SCA** — dependency CVE (pip-audit / OSV / npm audit)  
3. **SAST** — Bandit + Semgrep OWASP  
4. **Tests** — không deploy code đỏ  
5. **Container** — Trivy CRITICAL fail  
6. **SBOM** — CycloneDX/SPDX lưu artifact (compliance / recall)  
7. **Policy gate** — required checks trên branch protection  

## Lớp nâng cao (production)

- **Pin Actions** theo commit SHA (chống supply-chain tag move)  
- **Cosign** ký image + SLSA provenance  
- **OIDC** cloud deploy (AWS/GCP/Azure) — không lưu long-lived key  
- **DAST** ZAP baseline nightly trên staging  
- **IaC scan** Checkov nếu có Terraform/K8s manifests  
- **Admission** Kyverno/OPA trên cluster (Module 16/18)  

## Fail-closed vs warn

| Giai đoạn team | Secrets | CRITICAL CVE | HIGH CVE | Bandit HIGH |
|----------------|---------|--------------|----------|-------------|
| Lab / tuần 1 | fail | fail | warn | warn (fix dần) |
| Prod mature | fail | fail | fail | fail |

Xem `policy/severity-gate.yaml`.

## Liên kết Module

- 12: viết script scan bằng Python  
- 19: Vault cho secret runtime  
- 25: self-assessment web / ZAP ngoài CI  
- 26 (module này): **orchestrate** mọi thứ trong CI/CD  
