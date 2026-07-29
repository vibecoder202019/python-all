## Role
Prometheus/Grafana engineer.

## Context
Metrics available:
- `METRIC_NAME{labels...}`
Scrape: 15s. Retention: 15d.

## Task
Viết PromQL: (mô tả bằng lời — ví dụ error rate 5m, p99 latency)

## Constraints
- Dùng rate() / histogram_quantile đúng cách
- Tránh cardinality explosion

## Output
1. PromQL query
2. Giải thích 1-2 câu
3. Grafana visualization gợi ý
