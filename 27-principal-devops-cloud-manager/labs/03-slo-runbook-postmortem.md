# Lab 03 — SLO, runbook, postmortem

**Đọc trước:** README §5 + [docs/03-leadership-and-communication.md](../docs/03-leadership-and-communication.md)

## Mục tiêu

Bộ reliability tối thiểu cho 1 dịch vụ giả `payments-api`.

## Bước

```bash
cp templates/slo-workbook-template.md portfolio/slo-payments-api.md
cp templates/runbook-template.md portfolio/runbook-payments-api.md
cp templates/postmortem-template.md portfolio/postmortem-2026-lab.md
```

Điền:

1. SLO availability 99.9% + error budget tính tay  
2. Runbook: 3 symptom, rollback, escalation  
3. Postmortem giả: deploy bad config → 5xx 40 phút — **blameless**, ≥ 3 action items systemic  

## Done khi

- [ ] Error budget số phút/tháng ghi đúng  
- [ ] Postmortem không đổ lỗi cá nhân  
- [ ] Có action “cải thiện platform/golden path”  
