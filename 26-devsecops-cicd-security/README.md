# Module 26: DevSecOps CI/CD — Security in the Pipeline

Xây **pipeline CI/CD có bảo mật xuyên suốt** (shift-left) theo best practices hiện nay: secrets → SCA → SAST → build → container/SBOM → policy gate → deploy an toàn.

> **Liên quan:** [Module 12](../12-python-devops-devsecops/README.md) (script DevSecOps) · [Module 16](../16-k8s-security/README.md) · [Module 25](../25-web-security-phishing-seo/README.md) (self-test web)

---

## Mục tiêu

- Hiểu mô hình **DevSecOps pipeline** hiện đại (GitHub Actions làm chuẩn lab)
- Chạy scan **local** giống CI: Gitleaks, Bandit, pip-audit, Trivy, SBOM
- Đặt **policy gate** (fail khi CRITICAL/HIGH)
- Biết OIDC deploy, không nhét long-lived cloud key vào CI
- Copy workflow mẫu vào repo thật của bạn

---

## Best-practice pipeline (2025–2026)

```
┌─────────────┐
│  git push   │
└──────┬──────┘
       ▼
┌──────────────────────────────────────────────────────────┐
│ 1. Secret scan     Gitleaks / TruffleHog                 │
│ 2. SCA / deps      pip-audit, OSV-Scanner, npm audit     │
│ 3. SAST            Bandit + Semgrep (OWASP rules)        │
│ 4. IaC (nếu có)    Checkov / Trivy config                │
│ 5. Unit tests      pytest                                │
│ 6. Build image     Docker Buildx                         │
│ 7. Container CVE   Trivy / Grype                         │
│ 8. SBOM            Syft → CycloneDX/SPDX artifact        │
│ 9. Sign (prod)     Cosign + provenance (optional)        │
│10. Policy gate     fail on CRITICAL (và HIGH nếu sẵn)    │
│11. Deploy          OIDC → cloud/K8s (no static keys)     │
│12. DAST (staging)  ZAP baseline (nightly / post-deploy)  │
└──────────────────────────────────────────────────────────┘
```

### Nguyên tắc

| Nguyên tắc | Thực tế trong module |
|------------|----------------------|
| **Shift-left** | Secret + SAST trước khi build image |
| **Fail closed** | Job `policy-gate` chặn merge/deploy nếu P0 |
| **Least privilege** | OIDC / short-lived token, không `AWS_SECRET` dài hạn |
| **Supply chain** | SBOM + pin action SHA (prod) + scan base image |
| **Defense in depth** | Nhiều lớp scan; không tin một tool duy nhất |
| **Fast feedback** | Parallel jobs; cache deps; Trivy severity filter |

---

## Chạy nhanh (local, không cần GitHub)

```bash
cd learn-python-ai
bash 26-devsecops-cicd-security/scripts/setup.sh
bash 26-devsecops-cicd-security/scripts/01-check-prerequisites.sh
bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh
```

Pipeline GitHub Actions mẫu:

[`pipelines/github-actions/devsecops.yml`](pipelines/github-actions/devsecops.yml)

Copy vào repo app:

```bash
mkdir -p .github/workflows
cp 26-devsecops-cicd-security/pipelines/github-actions/devsecops.yml \
   .github/workflows/devsecops.yml
```

---

## Lộ trình lab

| Lab | Nội dung |
|-----|----------|
| [01](labs/01-pipeline-stages.md) | Map từng stage → tool |
| [02](labs/02-run-local-gates.md) | Chạy local pipeline + đọc báo cáo |
| [03](labs/03-github-actions.md) | Bật workflow trên GitHub |
| [04](labs/04-policy-and-oidc.md) | Policy gate + OIDC deploy concepts |

Docs: [docs/01-devsecops-pipeline.md](docs/01-devsecops-pipeline.md) · [docs/02-tools-matrix.md](docs/02-tools-matrix.md)

---

## Cấu trúc

```
26-devsecops-cicd-security/
├── sample-app/              # Mini FastAPI (cố ý có finding lab)
├── pipelines/
│   └── github-actions/      # Workflow best-practice
├── policy/                  # Severity / fail rules
├── scripts/                 # Local pipeline mirror CI
├── reports/                 # Output scan (gitignored)
├── labs/
├── docs/
├── cheatsheet/
├── README.md
└── readme_manual.md
```

---

## FAQ

**Khác Module 12?**  
12 = viết script Python DevOps/scan cơ bản. **26 = pipeline CI/CD đầy đủ** (Actions YAML + gate + SBOM + container).

**Bắt buộc cài hết tool?**  
`02-run-local-pipeline.sh` chạy phần có sẵn; thiếu Trivy/Gitleaks sẽ **skip có cảnh báo** (lab vẫn học được flow).

**Production khác lab?**  
Pin GitHub Action theo commit SHA, bật branch protection + required checks, Cosign sign, DAST trên staging, secret management (Vault — Module 19).

---

[readme_manual.md](readme_manual.md) | [cheatsheet/devsecops-pipeline.md](cheatsheet/devsecops-pipeline.md)
