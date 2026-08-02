# Lab 01 — Phishing awareness

**Mục tiêu:** Phân biệt URL/email an toàn vs giả mạo bằng heuristics.

## Bước

```bash
bash scripts/01-check-prerequisites.sh
python3 examples/01_phishing_url_analyzer.py
python3 examples/02_email_header_red_flags.py
```

## Việc cần làm

1. Thêm 2 URL vào `data/sample_urls.txt` (1 sạch, 1 giả brand).
2. Chạy lại analyzer — giải thích vì sao score cao/thấp.
3. Với email RISK: liệt kê 3 hành động người dùng nên làm (không click, báo cáo, kiểm tra domain chính thức).

## Không làm

Không gửi email phishing thật, không host trang giả mạo public.
