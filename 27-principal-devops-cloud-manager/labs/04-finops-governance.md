# Lab 04 — FinOps & governance scorecard

**Đọc trước:** README §6–7 + [docs/02-cloud-operating-model.md](../docs/02-cloud-operating-model.md)

## Mục tiêu

Đọc cost fixture + chấm governance; viết kế hoạch 30 ngày.

## Bước

```bash
bash scripts/03-run-governance-scorecard.sh
bash scripts/04-run-finops-summary.sh
```

Tạo `portfolio/finops-30-day-plan.md`:

1. Top 3 service theo spend — hành động gì?  
2. Xử lý `untagged_spend_pct`  
3. 5 mục `failed_items` điểm thấp nhất → owner giả + due date  
4. Liên hệ SCP / OIDC / backup với Module 22 & 26  

## Done khi

- [ ] Có `portfolio/governance-scorecard.json`  
- [ ] Plan 30 ngày ≤ 1 trang, ưu tiên P0 rõ  
