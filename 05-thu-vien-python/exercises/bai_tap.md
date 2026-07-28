# Bài tập Module 05

## Bài 1: Gọi Public API (Dễ)
Dùng `requests` gọi `https://api.github.com/users/{username}`, in tên, số repo public.

## Bài 2: Parse log với regex (Trung bình)
Parse dòng log Apache: `127.0.0.1 - - [15/Jan/2024:10:30:00] "GET /api HTTP/1.1" 200 1234`

## Bài 3: Retry decorator (Khó)
Viết decorator `@retry(max_attempts=3, delay=1)` cho hàm gọi API.

Đáp án: [solutions/solutions.py](solutions/solutions.py)
