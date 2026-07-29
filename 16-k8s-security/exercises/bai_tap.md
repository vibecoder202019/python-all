# Bài tập Module 16

## Bài 1 (Dễ): Thêm SQLi pattern
Thêm pattern phát hiện `EXEC xp_cmdshell` vào `common.py`.

## Bài 2 (Trung bình): Phishing score
Mở rộng `check_phishing_url`: cảnh báo nếu domain có ≥ 2 dấu `-`.

## Bài 3 (Trung bình): Rate limit theo endpoint
Sửa WAF middleware: `/login` giới hạn 5 req/phút, `/search` 30 req/phút.

## Bài 4 (Khó): NetworkPolicy
Viết NetworkPolicy chỉ cho phép egress tới `443` (HTTPS) — chặn mọi port khác.

## Bài 5 (Khó): Security CLI
Thêm subcommand `scan-urls FILE` đọc file URL và in báo cáo phishing.

Đáp án: [exercises/solutions/solutions.py](exercises/solutions/solutions.py)
