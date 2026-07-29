# Rubric chấm prompt (Module 20)

## Mỗi prompt (thang 1–5)

| Tiêu chí | 1 | 3 | 5 |
|----------|---|---|---|
| Role | Thiếu | Có nhưng chung | Level + domain rõ |
| Context | Thiếu log/version | Đủ một phần | Đủ verify, redacted |
| Task | Nhiều việc lẫn | Một việc mơ hồ | Một việc cụ thể |
| Output | Không | Có format | Format + constraints |
| Safety | Secret plaintext | Một phần redact | Full redact + verify |

## Capstone lab 12 (25 điểm)

- 5 prompts × 3 điểm chất lượng = 15
- Không lộ secret = 5
- Verify commands documented = 5

Pass: ≥ 20

## Gợi ý đáp án lab 04

Root cause: `int("")` ValueError.  
Fix: default port 5432 hoặc validate + message rõ.

## Gợi ý lab 10

Root cause: payment-svc OOMKilled → connection refused → 502 gateway.
