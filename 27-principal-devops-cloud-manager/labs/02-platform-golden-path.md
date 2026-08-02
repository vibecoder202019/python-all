# Lab 02 — Platform golden path

**Đọc trước:** README §4 + Module 26 README

## Mục tiêu

Thiết kế **golden path** để product team ship trong ≤ 1 ngày (lab giả lập).

## Bước

Tạo `portfolio/platform-catalog.md` gồm:

1. **Who we are** — Platform team phục vụ ai  
2. **Products** — (ví dụ) CI template, Terraform module VPC, observability defaults, secret pattern  
3. **Golden path** — checklist tạo service mới (repo → CI Module 26 → staging → prod)  
4. **SLAs nội bộ** — thời gian support ticket P1/P2  
5. **Escape hatch** — khi được phép lệch chuẩn + ai approve  

Copy tham chiếu CI:

```bash
# Ghi vào catalog: path workflow chuẩn
echo "Golden CI: 26-devsecops-cicd-security/pipelines/github-actions/devsecops.yml" >> portfolio/platform-catalog.md
```

## Done khi

- [ ] Catalog ≤ 2 trang nhưng đủ onboarding engineer mới  
- [ ] Có metric adoption (% service dùng golden path) — dù chỉ là target giả  
