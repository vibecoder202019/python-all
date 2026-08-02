# Hướng dẫn chạy Manual — Module 27: Principal DevOps & Cloud Manager

> **Trước khi gõ lệnh:** đọc [README.md](README.md) (*Lý thuyết nền tảng*) và docs/01–04.  
> Module nghiêng về **artifact viết** (ADR, runbook…) + script chấm điểm — không chỉ cài tool.

## Phần 0 — Lý thuyết

1. README: Principal vs Senior, 4 trụ cột, golden path, SLO, FinOps, ADR  
2. [docs/01-career-ladder.md](docs/01-career-ladder.md)  
3. [docs/02-cloud-operating-model.md](docs/02-cloud-operating-model.md)  
4. [docs/03-leadership-and-communication.md](docs/03-leadership-and-communication.md)  

Tự kiểm tra: giải thích error budget; khác Platform vs Cloud Manager.

---

## Phần A — Setup

```bash
cd learn-python-ai
bash 27-principal-devops-cloud-manager/scripts/setup.sh
bash 27-principal-devops-cloud-manager/scripts/01-check-prerequisites.sh
bash 27-principal-devops-cloud-manager/scripts/02-init-portfolio.sh
```

---

## Phần B — Governance + FinOps scripts

```bash
bash 27-principal-devops-cloud-manager/scripts/03-run-governance-scorecard.sh
cat 27-principal-devops-cloud-manager/portfolio/governance-scorecard.json

bash 27-principal-devops-cloud-manager/scripts/04-run-finops-summary.sh
cat 27-principal-devops-cloud-manager/portfolio/finops-summary.json
```

**Kỳ vọng lab fixture:** grade khoảng **C**, có failed OIDC/backup/budget/SLO…

Chạy tay:

```bash
python3 27-principal-devops-cloud-manager/project/governance_scorecard.py
python3 27-principal-devops-cloud-manager/project/finops_summary.py
```

---

## Phần C — Labs viết portfolio

```bash
# Lab 01
cp 27-principal-devops-cloud-manager/templates/ADR-template.md \
   27-principal-devops-cloud-manager/portfolio/ADR-001-compute-platform.md
# … điền theo labs/01

# Lab 05 validate
bash 27-principal-devops-cloud-manager/scripts/05-validate-portfolio.sh
```

---

## Phần D — Teardown

```bash
bash 27-principal-devops-cloud-manager/scripts/06-teardown.sh
```

---

## Bản đồ script

| Script | Phần |
|--------|------|
| `setup.sh` | A |
| `01-check-prerequisites.sh` | A |
| `02-init-portfolio.sh` | A |
| `03-run-governance-scorecard.sh` | B |
| `04-run-finops-summary.sh` | B |
| `05-validate-portfolio.sh` | C |
| `06-teardown.sh` | D |
