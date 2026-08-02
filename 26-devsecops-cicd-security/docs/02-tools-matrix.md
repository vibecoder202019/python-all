# Ma trận tools DevSecOps CI/CD

| Stage | Tool (lab) | Thay thế phổ biến | Output |
|-------|------------|-------------------|--------|
| Secret | Gitleaks | TruffleHog, detect-secrets | JSON / SARIF |
| SCA | pip-audit | OSV-Scanner, Dependabot, Snyk | JSON |
| SAST | Bandit | Semgrep, CodeQL, Sonar | JSON / SARIF |
| SAST rules | Semgrep `p/owasp-top-ten` | CodeQL QL packs | Findings |
| IaC | Trivy config | Checkov, tfsec | Report |
| Unit | pytest | — | JUnit |
| Image build | Docker Buildx | Podman, Kaniko | OCI image |
| Image CVE | Trivy | Grype, Snyk Container | Table / SARIF |
| SBOM | Syft | Trivy sbom, Anchore | CycloneDX |
| Sign | Cosign | Notary | Signature |
| DAST | ZAP baseline | Burp Enterprise | HTML |
| Policy | Branch protection + severity YAML | OPA/Conftest | Gate |
| Deploy auth | GitHub OIDC | Vault JWT | Short-lived creds |

## Cài nhanh (macOS)

```bash
brew install gitleaks trivy syft
pip install bandit pip-audit pre-commit
```

## GitHub Actions tương ứng

File: `pipelines/github-actions/devsecops.yml`
