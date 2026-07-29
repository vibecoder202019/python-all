# Lab 06 — Kết nối GitHub VCS

**90 phút**

## Bước 1 — VCS Provider

1. **Settings** → **VCS Providers** → **Connect GitHub**
2. Hoàn tất OAuth (Dex / GitHub App theo wizard UI)

## Bước 2 — Workspace settings

1. Workspace lab 04 → **Version Control**
2. Chọn repository fork
3. Branch: `main`
4. Working dir: `21-terraform-ui-terrakube/terraform/sample-workspace`

## Bước 3 — Trigger

1. Sửa `app_name` variable trên UI → Plan
2. (Tùy chọn) Sửa `main.tf` trên Git → push → auto plan nếu bật webhook

## Pass

- [ ] VCS connected
- [ ] Plan chạy từ commit trên Git
- [ ] Log hiển thị commit SHA

Doc: [docs/04-vcs-github.md](../../docs/04-vcs-github.md)
