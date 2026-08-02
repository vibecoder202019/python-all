# SLO workbook — {{SERVICE_NAME}}

## User journey quan trọng

(Vd: checkout, login, API /health phụ thuộc)

## SLI

| SLI | Cách đo | Nguồn |
|-----|---------|-------|
| Availability | successful / total | … |
| Latency | p99 < Xs | … |

## SLO

| SLO | Cửa sổ | Mục tiêu |
|-----|--------|----------|
| Availability | 30 ngày | 99.9% |
| Latency p99 | 30 ngày | < 300ms |

## Error budget

- 99.9% / 30 ngày ≈ 43 phút downtime  
- Khi budget < 25%: đóng feature flag rủi ro, ưu tiên reliability  

## Alerting (ý tưởng)

- Burn rate nhanh → page  
- Burn rate chậm → ticket  

## Review cadence

Hàng tháng: xem cháy budget, quyết định đầu tư reliability.  
