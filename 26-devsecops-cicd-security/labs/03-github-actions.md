# Lab 03 — Bật GitHub Actions

```bash
bash scripts/03-enable-github-actions.sh
```

## Việc làm

1. Copy `pipelines/github-actions/devsecops.yml` → `.github/workflows/devsecops.yml` (repo python-all hoặc repo app).  
2. Push branch → mở tab **Actions** — xem job parallel secrets/SCA/SAST.  
3. Settings → Branches → Rule trên `main`: require  
   - Secret scan  
   - SAST  
   - Build · Trivy · SBOM  
4. (Tuỳ) Tắt Semgrep `continue-on-error` khi đã có token / chấp nhận fail.

## Lưu ý monorepo

Giữ `APP_DIR: 26-devsecops-cicd-security/sample-app`. Repo app riêng → `APP_DIR: .`.
