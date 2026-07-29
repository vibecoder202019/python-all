# Lab 02 — Đăng nhập & Tour UI

**30 phút**

## Đăng nhập

| Field | Value |
|-------|-------|
| URL | https://terrakube.platform.local |
| Email | admin@example.com |
| Password | admin |

## Checklist tour UI

Ghi chú ý nghĩa từng mục:

- [ ] **Organizations** — tenant / team
- [ ] **Projects** — nhóm workspace
- [ ] **Workspaces** — 1 Terraform stack
- [ ] **Registry** — private modules/providers
- [ ] **Settings** — users, VCS, tokens
- [ ] **Runs / Jobs** — lịch sử plan/apply (tên menu có thể khác theo version)

## Bài tập bảo mật

1. Đổi password admin (Settings → Profile / Security)
2. Ghi lại: tại sao **không** dùng `admin/admin` ngoài lab?

## Verify

```bash
bash 21-terraform-ui-terrakube/scripts/08-verify-lab.sh 02
```
