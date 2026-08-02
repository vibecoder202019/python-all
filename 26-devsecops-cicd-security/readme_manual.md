# Hướng dẫn chạy Manual — Module 26: DevSecOps CI/CD Security

> Lệnh từ `setup.sh`, `01-check-prerequisites.sh`, `02-run-local-pipeline.sh`, `03-enable-github-actions.sh`, `06-teardown.sh`.

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r 26-devsecops-cicd-security/sample-app/requirements.txt
pip install pytest httpx bandit pip-audit pyyaml
mkdir -p 26-devsecops-cicd-security/reports
```

**Tuỳ chọn:**

```bash
brew install gitleaks trivy syft
```

**Kiểm tra:**

```bash
bandit --version
pip-audit --version
python -c "import fastapi; print('ok')"
```

---

## Phần B — Prerequisites (`scripts/01-check-prerequisites.sh`)

```bash
python3 --version
test -f 26-devsecops-cicd-security/pipelines/github-actions/devsecops.yml
command -v gitleaks || echo "gitleaks optional"
command -v trivy || echo "trivy optional"
command -v docker || echo "docker optional"
```

---

## Phần C — Local pipeline (`scripts/02-run-local-pipeline.sh`)

```bash
bash 26-devsecops-cicd-security/scripts/02-run-local-pipeline.sh
ls 26-devsecops-cicd-security/reports/
```

**Kỳ vọng từng bước:**

| Stage | Kỳ vọng lab |
|-------|-------------|
| Gitleaks | OK hoặc SKIP |
| pip-audit | OK / warn |
| Bandit | Thấy MD5 finding trong sample-app |
| pytest | PASS |
| Docker+Trivy | OK nếu có Docker |
| SBOM | File cyclonedx nếu có syft |

Chạy tay từng tool:

```bash
bandit -r 26-devsecops-cicd-security/sample-app -ll
pip-audit -r 26-devsecops-cicd-security/sample-app/requirements.txt
cd 26-devsecops-cicd-security/sample-app && pytest -q
docker build -t devsecops-lab-app:local 26-devsecops-cicd-security/sample-app
trivy image --severity CRITICAL --exit-code 1 devsecops-lab-app:local
```

---

## Phần D — GitHub Actions (`scripts/03-enable-github-actions.sh`)

```bash
bash 26-devsecops-cicd-security/scripts/03-enable-github-actions.sh
mkdir -p .github/workflows
cp 26-devsecops-cicd-security/pipelines/github-actions/devsecops.yml \
   .github/workflows/devsecops.yml
# Commit + push → xem tab Actions
```

---

## Phần E — Pre-commit

```bash
pip install pre-commit
cp 26-devsecops-cicd-security/pipelines/pre-commit-config.yaml .pre-commit-config.yaml
# Sửa path bandit args cho repo của bạn
pre-commit install
pre-commit run --all-files
```

---

## Phần F — Teardown

```bash
bash 26-devsecops-cicd-security/scripts/06-teardown.sh
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | B |
| `02-run-local-pipeline.sh` | C |
| `03-enable-github-actions.sh` | D |
| `06-teardown.sh` | F |
