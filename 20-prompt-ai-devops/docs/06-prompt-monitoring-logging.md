# Prompt AI cho Monitoring & Logging

## Prometheus / PromQL

### Context hữu ích

- Metric name + labels có sẵn (`http_requests_total{job="api"}`)
- Scrape interval, retention
- Ngưỡng SLA (p99 < 500ms, error rate < 1%)

Template: [prompts/monitoring/promql-query.md](../prompts/monitoring/promql-query.md)

---

## Prompt viết PromQL

```markdown
## Task
PromQL: error rate 5xx / total requests — ratio 5 phút, group by service label.
Metric: http_requests_total{status=~"5.."} và tổng không filter status.

## Output
- Query PromQL
- Giải thích 1 dòng
- Grafana panel type gợi ý (timeseries / stat)
```

---

## Alert rules

```markdown
Context: Kubernetes API, metric up{job="kube-api"} == 0.
Task: Prometheus alert rule:
- for: 2m
- severity: critical
- annotations: summary + runbook_url placeholder

Output: YAML prometheus rule group, labels team=platform
```

Template: [prompts/monitoring/alert-rule.md](../prompts/monitoring/alert-rule.md)

---

## Logging — parse & RCA

```markdown
## Role
SRE phân tích incident.

## Context
Log sample (100 dòng) nginx + app JSON — đính kèm.
Incident: spike 502 14:32–14:45 UTC.

## Task
1. Regex/grep pattern tìm request_id lỗi
2. Timeline 5 bullet (UTC)
3. 3 root cause giả thuyết ranked
4. Cần thêm log/metric nào để xác nhận

## Output
Markdown. Lệnh: kubectl logs / jq / rg gợi ý.
```

Template: [prompts/monitoring/log-rca.md](../prompts/monitoring/log-rca.md)

---

## Structured logging (Python)

```markdown
Task: Refactor @file app/logging_config.py dùng structlog JSON:
- fields: timestamp, level, request_id, user_id
- không log password/token keys
- tương thích FastAPI middleware

Output: diff + example log line JSON
```

---

## Dashboard Grafana (mô tả)

```markdown
Task: Mô tả dashboard 6 panel cho FastAPI service:
- RPS, latency p50/p99, error rate, active connections, CPU, memory
Data source: Prometheus.
Output: table Panel | Query | Visualization | Threshold |
```

---

## Datadog / CloudWatch (tùy chọn)

Cùng pattern R-C-T-O — thay PromQL bằng ngôn ngữ query tương ứng, nêu rõ platform.

---

## Lab

- [Lab 09 — PromQL & alerts](../labs/advanced/lab09-prometheus.md)
- [Lab 10 — Log RCA](../labs/advanced/lab10-logging-rca.md)

**Tiếp:** [07-cursor-agent-workflow.md](07-cursor-agent-workflow.md)
