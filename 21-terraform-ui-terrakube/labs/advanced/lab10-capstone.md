# Lab 10 — Capstone Pipeline

**120 phút** | Advanced

## Scenario

Team `platform` vận hành Terraform qua Terrakube — giống AWX cho infra.

## Yêu cầu hoàn thành

| # | Task | Done |
|---|------|------|
| 1 | Terrakube chạy (Compose hoặc Helm) | ☐ |
| 2 | Org `lab-org`, project `demo-infra` | ☐ |
| 3 | Workspace VCS → `sample-workspace` | ☐ |
| 4 | Variables `environment=prod`, `app_name=capstone` | ☐ |
| 5 | Plan + Apply thành công | ☐ |
| 6 | RBAC: 1 team plan-only | ☐ |
| 7 | Document URL + ai được apply prod | ☐ |
| 8 | Teardown script chạy được | ☐ |

## Deliverable

File `notes/capstone.md` (tự tạo):

- Sơ đồ luồng: Git push → Terrakube → executor → state
- 3 khác biệt so với chạy `terraform` CLI local
- 2 khác biệt so với AWX Module 15

## Rubric

Pass nếu hoàn thành ≥ 7/8 mục.
