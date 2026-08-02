# Lab 01 — ADR & system design

**Đọc trước:** README §8 + [docs/01-career-ladder.md](../docs/01-career-ladder.md)

## Mục tiêu

Viết 2 ADR và 1 sơ đồ kiến trúc — artifact Principal chuẩn.

## Bước

```bash
bash scripts/02-init-portfolio.sh
cp templates/ADR-template.md portfolio/ADR-001-compute-platform.md
cp templates/ADR-template.md portfolio/ADR-002-secret-strategy.md
```

### ADR-001 (bắt buộc)

Chủ đề: **EKS vs ECS vs Cloud Run/equivalent** cho workload chính của “công ty lab”.  
Điền đủ options, decision, consequences (cost + ops + security).

### ADR-002 (bắt buộc)

Chủ đề: **Vault vs SSM Parameter Store vs cloud secret manager** (liên hệ Module 19).

### Sơ đồ

Thêm `portfolio/architecture-ascii.md`: edge → app → data → observability (10–20 dòng ASCII).

## Done khi

- [ ] 2 ADR status Accepted (lab)  
- [ ] Mỗi ADR có impact business 1 câu  
- [ ] Sơ đồ đọc được bởi non-dev trong 2 phút  
