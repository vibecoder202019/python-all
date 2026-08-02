# Lab 01 — Map pipeline stages

**Đọc trước:** [README lý thuyết §3](../README.md) + [docs/03-glossary-for-beginners.md](../docs/03-glossary-for-beginners.md)

## Mục tiêu

Nối mỗi stage với tool và câu hỏi “fail thì làm gì?”.

## Việc làm

1. Đọc [docs/01-devsecops-pipeline.md](../docs/01-devsecops-pipeline.md)  
2. Mở `pipelines/github-actions/devsecops.yml` — liệt kê **tên job** theo thứ tự  
3. Điền bảng:

| # | Job | Tool | Fail → hành động |
|---|-----|------|------------------|
| 1 | | | |
| … | | | |

4. So với `policy/severity-gate.yaml` — CRITICAL container fail ngay; HIGH đang warn. Viết 1 câu khi nào bạn bật fail HIGH.
