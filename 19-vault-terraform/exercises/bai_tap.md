# Bài tập Module 19 — Vault + Terraform

## Terraform
1. (Dễ) Apply `01-hello`, giải thích output của `terraform plan`.
2. (Dễ) Tạo biến `region=ap-southeast-1` trong `02-variables`, output ra file JSON.
3. (Trung bình) Dùng `for_each` tạo 5 file config cho 5 service giả lập.
4. (Trung bình) Viết module nhận `environment` + `replicas`, output file YAML.
5. (Khó) Cấu hình workspace dev/prod với state tách biệt.

## Vault
6. (Dễ) Ghi và đọc secret KV v2 path `secret/demo/api-key`.
7. (Trung bình) Policy read-only cho path `secret/data/demo/*`.
8. (Trung bình) Tạo token TTL 30m, renew 1 lần.
9. (Khó) Setup AppRole + login script bash.
10. (Khó) Giải thích khi nào dùng dynamic DB secret thay KV static.

## Tích hợp
11. Terraform đọc Vault, tạo `.env` — không hardcode password.
12. (Capstone) Lab 12 — manifest K8s + module config.

Đáp án: [solutions/lab-solutions.sh](solutions/lab-solutions.sh)
