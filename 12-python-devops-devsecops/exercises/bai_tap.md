# Bài tập Module 12: DevOps & DevSecOps

## Bài 1: Backup script (Dễ)
Viết script Python backup thư mục `data/` sang `backup/` với timestamp.

## Bài 2: Cron-style scheduler (Trung bình)
Dùng `schedule` library chạy health-check mỗi 60 giây, log kết quả.

## Bài 3: GitHub Actions generator (Trung bình)
Viết script generate `.github/workflows/ci.yml` từ template Python.

## Bài 4: Full DevSecOps pipeline (Khó)
Mở rộng `step06_final.py`: thêm `dependency-scan` (pip audit), `lint` (ruff).

## Bài 5: Monitor website + filter nhiễu (Trung bình)
1. Thêm 2 URL vào `data/websites.yaml`, chạy `examples/07_website_live_or_die.py`.
2. Sửa `consecutive_failures=2` trong example 08 — quan sát SEND tăng thế nào.
3. Giải thích vì sao cần cooldown khi site vẫn DIE.

Đáp án: [exercises/solutions/solutions.py](exercises/solutions/solutions.py)
