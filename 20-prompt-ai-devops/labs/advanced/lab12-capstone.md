# Lab 12 — Capstone: Incident response với AI (Advanced)

**120 phút**

## Scenario

14:32 UTC — alert `HighErrorRate` service `api-gateway`.  
502 tăng, log mẫu: [incident-502.log](../../examples/sample-logs/incident-502.log).  
Stack: K8s, payment-svc backend, Prometheus, Vault cho secrets.

## Nhiệm vụ (multi-prompt)

| Step | Prompt focus | Bạn verify |
|------|--------------|------------|
| 1 | Log RCA — timeline | Khớp timestamp log |
| 2 | K8s — check payment-svc OOM | kubectl describe (lab/giả lập) |
| 3 | Fix YAML — tăng memory limit | dry-run apply |
| 4 | PromQL alert tránh false positive | review query |
| 5 | Vault — không log password trong app | policy review |

## Rubric (25 điểm)

- Prompt R-C-T-O mỗi step (5×3)
- Không paste secret (5)
- Document verify commands (5)

**Pass:** ≥ 20/25 — tự chấm theo doc 08.
