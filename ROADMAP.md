# Roadmap chi tiết

## Giai đoạn 1: Nền tảng Python (Tuần 1-5)

```
Tuần 1-2: Module 01 — Python cơ bản
    ├── Biến, kiểu dữ liệu, toán tử
    ├── if/else, for, while
    ├── Hàm, lambda, *args/**kwargs
    └── List comprehension

Tuần 3: Module 02 — Cấu trúc dữ liệu
    ├── List, Tuple, Set, Dict
    ├── Stack, Queue (collections)
    └── Algorithm cơ bản (sort, search)

Tuần 4-5: Module 03 — OOP
    ├── Class & Object
    ├── Inheritance, Encapsulation
    ├── Magic methods (__str__, __repr__)
    └── Design patterns cơ bản
```

## Giai đoạn 2: Thực hành & Thư viện (Tuần 6-7)

```
Tuần 6: Module 04 — File I/O & Module
    ├── Đọc/ghi text, CSV, JSON
    ├── import, __name__ == "__main__"
    └── Tạo package riêng

Tuần 7: Module 05 — Thư viện Python
    ├── requests — gọi HTTP API
    ├── json, datetime, pathlib
    └── regex, logging
```

## Giai đoạn 3: Data Science (Tuần 8-9)

```
Tuần 8-9: Module 06 — Data Science
    ├── NumPy — mảng, vector hóa
    ├── Pandas — DataFrame, groupby, merge
    └── Matplotlib/Seaborn — visualization
```

## Giai đoạn 4: Machine Learning (Tuần 10-13)

```
Tuần 10-11: Module 07 — Machine Learning
    ├── Pipeline: load → clean → feature → train → evaluate
    ├── Classification (Iris, Titanic)
    ├── Regression (housing price)
    └── Cross-validation, hyperparameter tuning

Tuần 12-13: Module 08 — Deep Learning
    ├── Perceptron, activation functions
    ├── Keras Sequential API
    └── MNIST digit classification
```

## Giai đoạn 5: API & Dự án (Tuần 14-16)

```
Tuần 14-15: Module 09 — FastAPI
    ├── REST API concepts (GET, POST, PUT, DELETE)
    ├── Pydantic models, validation
    ├── Dependency injection
    └── Swagger UI / OpenAPI

Tuần 16: Module 10 — Dự án tổng hợp
    └── ML Model + FastAPI + Tests end-to-end
```

## Giai đoạn 6: Game, DevOps & AWS (Tuần 17-25)

```
Tuần 17-19: Module 11 — Game cho Trẻ em (Pygame)
    ├── Game loop, vẽ hình, input
    ├── Sprite, collision, score
    ├── Snake game (nâng cao)
    └── Dự án: Catch the Stars (6 bước)

Tuần 20-22: Module 12 — DevOps & DevSecOps
    ├── subprocess, pathlib, config
    ├── Log analysis, health check
    ├── Docker automation
    ├── Security scanning (DevSecOps)
    └── Dự án: DevOps Toolkit CLI (6 bước)

Tuần 23-25: Module 13 — Python & AWS Infrastructure
    ├── boto3, STS, credentials
    ├── S3, EC2, IAM, CloudWatch
    ├── CloudFormation template generation
    └── Dự án: AWS Infra Builder (S3 + SG + EC2)
```

## Giai đoạn 7: PostgreSQL (Tuần 26-28)

```
Tuần 26-28: Module 14 — PostgreSQL tự học
    ├── SQL cơ bản: CRUD, JOIN, aggregation
    ├── PL/pgSQL: function, procedure, RETURN QUERY
    ├── Trigger: BEFORE/AFTER, audit, validation
    ├── View, Materialized View, Index, EXPLAIN
    ├── Python psycopg2: query, transaction, gọi function
    └── Dự án: Library DB (mượn/trả sách, báo cáo)
```

## Giai đoạn bổ sung: Web defense & Search integrity

```
Module 25 — Web Security / Phishing / Google Search Integrity
    ├── Phishing URL + email red flags (awareness)
    ├── Security headers + input sanitize (OWASP defense)
    ├── Triage ranking drop: Security Issues / Manual / Core Update
    └── Lab khôi phục site bị hack → spam (chủ site only)
```

> Module 25 là **phòng thủ**. Không dạy tấn công phishing thật hay black-hat SEO.

## Giai đoạn bổ sung: DevSecOps CI/CD

```
Module 26 — Security in the pipeline
    ├── Gitleaks · pip-audit · Bandit/Semgrep · pytest
    ├── Docker · Trivy · Syft SBOM · policy gate
    ├── GitHub Actions workflow + pre-commit
    └── OIDC deploy / ZAP staging (concepts + YAML mẫu)
```

## Giai đoạn capstone nghề nghiệp: Principal / Cloud Manager

```
Module 27 — Principal DevOps Engineer & Cloud Manager
    ├── Career ladder L3→L4, 4 trụ: Platform / SRE / Gov / FinOps
    ├── ADR, golden path catalog, SLO, runbook, blameless postmortem
    ├── Governance scorecard + FinOps summary (Python lab)
    └── Portfolio 1-pager + interview narrative
```

## Mục tiêu sau khi hoàn thành

Sau lộ trình đầy đủ, bạn sẽ có thể:

- Viết Python sạch, dễ đọc, có cấu trúc
- Xử lý dữ liệu với Pandas/NumPy
- Train và đánh giá model ML cơ bản
- Hiểu neural network và train model đơn giản
- Xây dựng REST API với FastAPI
- Làm game 2D với Pygame
- Viết script DevOps/DevSecOps automation
- Tạo và quản lý AWS infrastructure bằng boto3
- Thiết kế schema, viết function/trigger PostgreSQL
- Kết nối Python ↔ PostgreSQL với psycopg2
- Deploy model ML qua API (local)
- Tiếp tục học MLOps (Kubernetes, CI/CD, KServe...)
- Xây portfolio Principal DevOps / Cloud Manager (ADR, FinOps, governance)
