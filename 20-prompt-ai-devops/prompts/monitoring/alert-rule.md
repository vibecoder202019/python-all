## Role
SRE viết alert Prometheus.

## Context
- Metric: ...
- SLA / SLO: ...
- On-call runbook: (link hoặc placeholder)

## Task
Alert rule YAML:
- expr, for, labels severity
- annotations: summary, description, runbook_url

## Constraints
- Tránh alert fatigue — có `for` hợp lý
- Group name rõ ràng

## Output
prometheus rule group YAML
