# DevSecOps CI/CD cheatsheet

## Học trước

README Module 26 → docs/03 glossary → docs/01 → docs/02

## Nhớ nhanh SAST vs DAST

- **SAST** = đọc code (Bandit)  
- **DAST** = đánh URL đang chạy (ZAP)  
- **SCA** = CVE thư viện (pip-audit)  
- **Trivy image** = CVE trong container/OS  

## Local

```bash
bash scripts/setup.sh
bash scripts/02-run-local-pipeline.sh
```

## Stages

```
Gitleaks → pip-audit → Bandit/Semgrep → pytest → Docker → Trivy → Syft → Gate
```

## Cài tool

```bash
brew install gitleaks trivy syft
pip install bandit pip-audit pre-commit
pre-commit install  # dùng pipelines/pre-commit-config.yaml
```

## Copy workflow

```bash
cp pipelines/github-actions/devsecops.yml .github/workflows/devsecops.yml
# Sửa APP_DIR
```

## Prod checklist

- [ ] Branch protection + required checks  
- [ ] Fail CRITICAL (secrets, CVE, SAST)  
- [ ] SBOM artifact giữ ≥ 90 ngày  
- [ ] OIDC deploy — không static cloud key  
- [ ] Pin action SHA  
- [ ] ZAP trên staging  
