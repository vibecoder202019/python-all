# Lab 10 — Log analysis RCA (Advanced)

**60 phút**

1. Mở [examples/sample-logs/incident-502.log](../../examples/sample-logs/incident-502.log)
2. Redact nếu cần — paste vào [log-rca.md](../../prompts/monitoring/log-rca.md)
3. AI đưa timeline + hypothesis
4. **Bạn** xác nhận: root cause có phải payment-svc OOM → 502?

## Pass

Timeline khớp log; mitigation proposal realistic (scale memory / fix leak).
