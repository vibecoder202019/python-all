# Tích hợp Git / VCS (GitHub)

Terrakube kéo code Terraform từ Git — workflow giống Terraform Cloud.

---

## Chuẩn bị repository

### Cách 1 — Dùng repo python-all (khuyến nghị)

1. Fork https://github.com/vibecoder202019/python-all
2. Path workspace: `21-terraform-ui-terrakube/terraform/sample-workspace`

### Cách 2 — Repo riêng chỉ chứa Terraform

```bash
mkdir my-tf-demo && cd my-tf-demo
git init
cp -r /path/to/sample-workspace/* .
git add . && git commit -m "Initial terraform lab"
git remote add origin git@github.com:YOUR_USER/my-tf-demo.git
git push -u origin main
```

---

## Kết nối VCS trên Terrakube

1. **Settings** → **VCS Providers** → **Connect GitHub**
2. OAuth app Terrakube (Dex) — follow wizard UI
3. Authorize organization/repo access

> Lab local: nếu OAuth phức tạp, dùng **public repo** + personal access token theo docs Terrakube version hiện tại (UI có thể thay đổi — xem Settings → VCS).

---

## Gắn VCS vào Workspace

1. Workspace → **Settings** → **Version Control**
2. Repository: `YOUR_USER/python-all`
3. Branch: `main`
4. **Terraform Working Directory:** `21-terraform-ui-terrakube/terraform/sample-workspace`

---

## Trigger run

| Cách | Hành vi |
|------|---------|
| **Manual** | UI → Plan |
| **Webhook** | Push Git → auto plan (cấu hình trong workspace) |
| **Schedule** | Cron plan/apply (lab 10) |

---

## Branch strategy (production gợi ý)

```
main     → apply manual approval
develop  → plan only auto on push
feature/* → plan on PR
```

Terrakube + GitHub PR integration — xem docs Terrakube mới nhất cho VCS-driven workflows.

---

## Lab

→ [Lab 06 — GitHub VCS](../labs/intermediate/lab06-vcs-github.md)

**Tiếp:** [05-state-registry-rbac.md](05-state-registry-rbac.md)
