# Bài tập Module 15: Ansible AWX + MinIO + Kubernetes + Python

## Bài 1: AWX API client (Dễ)
Viết function `get_job_count()` trả số job trong AWX (dùng `GET /api/v2/jobs/`).

## Bài 2: Launch job với extra vars (Trung bình)
Mở rộng `launch_job.py`: nhận file JSON `--vars-file vars.json` truyền vào AWX.

## Bài 3: MinIO list objects (Trung bình)
Dùng boto3 liệt kê tất cả object trong bucket `awx-artifacts` prefix `reports/`.

## Bài 4: Custom Ansible module (Khó)
Viết module `disk_usage_python` trả % disk usage — gọi từ playbook AWX.

## Bài 5: Full automation CLI (Khó)
Mở rộng `step06_final.py` thêm subcommand `watch --job-id N` — poll và in stdout realtime.

Đáp án tham khảo: [exercises/solutions/solutions.py](exercises/solutions/solutions.py)
