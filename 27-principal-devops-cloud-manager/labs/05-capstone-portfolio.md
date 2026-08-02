# Lab 05 — Capstone portfolio

**Đọc trước:** [docs/04-interview-and-portfolio.md](../docs/04-interview-and-portfolio.md)

## Mục tiêu

Gói toàn bộ lab thành hồ sơ xin **Principal DevOps** hoặc **Cloud Manager**.

## Bước

```bash
cp templates/one-pager-portfolio.md portfolio/one-pager.md
```

Điền one-pager + đảm bảo có:

| Artifact | Path |
|----------|------|
| ADR ×2 | `portfolio/ADR-00*.md` |
| Platform catalog | `portfolio/platform-catalog.md` |
| SLO + runbook + postmortem | `portfolio/slo-*`, `runbook-*`, `postmortem-*` |
| Scorecard + FinOps plan | `governance-scorecard.json`, `finops-30-day-plan.md` |
| Architecture | `architecture-ascii.md` |

### Narrative 3 phút (viết `portfolio/pitch.md`)

1. Vấn đề org lab  
2. Quyết định (ADR)  
3. Golden path  
4. Đo reliability + cost  
5. Việc quý tới  

## Done khi

- [ ] One-pager đọc suôn 2 phút  
- [ ] Pitch không chỉ liệt kê tool  
- [ ] Self-assessment từ docs/01 đã điền  

```bash
bash scripts/05-validate-portfolio.sh
```
