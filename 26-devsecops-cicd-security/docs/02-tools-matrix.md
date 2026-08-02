# Ma trận tools — giải thích cho người mới

Mỗi tool làm **một việc**. Pipeline ghép chúng lại (Module 26 README).

## Bảng tra nhanh

| Stage | Tool (lab) | Thay thế | Bạn đọc output để tìm gì? |
|-------|------------|----------|---------------------------|
| Secret | Gitleaks | TruffleHog | API key, token, private key trong git |
| SCA | pip-audit | OSV, Dependabot | CVE trong `requirements.txt` |
| SAST | Bandit | Semgrep, CodeQL | Pattern code Python nguy hiểm |
| SAST rules | Semgrep OWASP | CodeQL | Rule đa ngôn ngữ / OWASP |
| IaC | Trivy config | Checkov | Misconfig K8s/Terraform |
| Unit | pytest | — | Logic app có còn đúng |
| Image | Docker Buildx | Kaniko | Artifact chạy được |
| Image CVE | Trivy | Grype | CVE OS + lib trong image |
| SBOM | Syft | Trivy sbom | Danh sách package |
| Sign | Cosign | Notary | Chữ ký image |
| DAST | ZAP | Burp | Lỗi trên URL đang chạy |
| Gate | Branch protection | OPA | Có được merge không |
| Deploy auth | OIDC | Vault JWT | Quyền cloud tạm |

## Cài trên macOS (khi sẵn sàng)

```bash
brew install gitleaks trivy syft
pip install bandit pip-audit pre-commit
```

## Khi nào dùng tool nào? (câu hỏi học)

1. “Tôi nghi commit nhầm AWS key” → **Gitleaks** (+ rotate key)  
2. “CVE trên PyPI vừa ra” → **pip-audit** / Dependabot  
3. “Code có MD5 / SQL nối chuỗi không?” → **Bandit / Semgrep**  
4. “Image production có openssl cũ không?” → **Trivy image**  
5. “Site staging có XSS không?” → **ZAP** (sau khi đã deploy staging)  

## GitHub Actions tương ứng

File: `pipelines/github-actions/devsecops.yml`  
Giải thích từng job: xem README mục “Các lớp bảo mật trong pipeline”.
