# Lab 02 — Chạy local gates

```bash
bash scripts/setup.sh
bash scripts/01-check-prerequisites.sh
bash scripts/02-run-local-pipeline.sh
ls -la reports/
```

## Việc làm

1. Mở `reports/bandit.json` (nếu có) — tìm finding liên quan **MD5** trong `sample-app/app.py`.  
2. Giải thích vì sao lab **cố ý** để MD5; production nên dùng gì (`hashlib.sha256` / password hashers).  
3. Nếu có Trivy: ghi 0–3 CVE CRITICAL (hoặc “none”).  
4. Chạy `bash scripts/06-teardown.sh` rồi chạy lại pipeline — reports tạo lại.

## Kỳ vọng

- Tests xanh  
- Bandit cảnh báo MD5  
- Secrets: không có private key thật  
