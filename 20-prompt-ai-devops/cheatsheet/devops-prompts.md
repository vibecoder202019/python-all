# DevOps prompt snippets

## Python debug
Role: senior Python | Context: traceback + file | Task: root cause + minimal fix | Output: diff

## K8s troubleshoot
Include: describe + logs + events | -n NS every command | Output: Cause|Verify|Fix table

## K8s YAML
No :latest | requests/limits | probes | apiVersion explicit | dry-run verify

## Vault
[REDACTED] tokens | KV v2 paths secret/data/ | least privilege review

## Terraform
plan review only | table Resource|Action|Risk | no secret in .tf

## PromQL
rate() over 5m | histogram_quantile for latency | alert needs for: duration

## Logs RCA
Timeline UTC | 3 hypotheses ranked | confirm commands | no PII in prompt

## Cursor Agent
Goal / Constraints / Done when / run tests before done
