# Lab 09 — PromQL & Alerts (Advanced)

**60 phút**

1. Dùng [promql-query.md](../../prompts/monitoring/promql-query.md):
   - Task: p99 latency từ histogram `http_request_duration_seconds_bucket`
2. Dùng [alert-rule.md](../../prompts/monitoring/alert-rule.md):
   - Alert khi error rate > 1% trong 5 phút

Validate PromQL syntax (promtool nếu có, hoặc Grafana explore).

## Pass

Query có `histogram_quantile` hoặc `rate` đúng; alert có `for:` và annotations.
