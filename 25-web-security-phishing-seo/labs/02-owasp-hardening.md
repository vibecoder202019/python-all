# Lab 02 — OWASP hardening (defense)

**Mục tiêu:** Hiểu input validation + security headers giúp giảm XSS/SQLi/clickjacking.

## Bước

```bash
python3 examples/03_security_headers_check.py
python3 examples/04_owasp_input_sanitizer.py
```

## Việc cần làm

1. Viết CSP tối thiểu cho blog tĩnh (chỉ `'self'` + CDN font giả định).
2. Thêm 1 payload XSS mới vào ví dụ 04 và xác nhận bị flag.
3. Liên hệ Module 16: headers tương tự annotation Ingress NGINX.

## Ghi nhớ

Sanitize + parameterized query + CSP là **phòng thủ**. Không dùng payload để tấn công site live.
