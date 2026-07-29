# Module 21: Quản lý Terraform bằng UI Open Source — Terrakube

Tự học triển khai và vận hành **Terrakube** — nền tảng **open source** (Apache 2.0) quản lý Terraform/OpenTofu qua **giao diện web**, tương tự vai trò **AWX** đối với Ansible.

> **Tiên quyết:** [Module 19 — Terraform cơ bản](../19-vault-terraform/README.md). **Liên quan:** [Module 15 — AWX](../15-ansible-awx-minio-k8s/README.md), [Module 18 — K8s](../18-cka-cks-kubernetes/README.md).

---

## Terrakube vs AWX — So sánh nhanh

| | **AWX (Ansible)** | **Terrakube (Terraform)** |
|---|-------------------|---------------------------|
| **Công việc** | Playbook / Job Template | Workspace → Plan / Apply |
| **UI** | Job history, schedule, inventory | Run history, state, registry, RBAC |
| **State** | Không | Remote state tập trung |
| **Trigger** | Manual, schedule, webhook | UI, VCS push, schedule |
| **License** | Open source | Apache 2.0, self-host |

---

## Mục tiêu module

- Hiểu mô hình **TACOS** (Terraform Automation & Collaboration Software)
- Triển khai Terrakube **Docker Compose** (lab local HTTPS)
- Triển khai Terrakube **Helm trên minikube** (lab nâng cao)
- Tạo **Organization → Project → Workspace → Run** trên UI
- Kết nối Git (GitHub) hoặc chạy sample Terraform trong repo
- Xem **state**, log run, RBAC cơ bản

---

## Yêu cầu môi trường

| Công cụ | Phiên bản | Mục đích |
|---------|-----------|----------|
| **Docker Desktop** | ≥ 4.x | Chạy Terrakube stack |
| **docker compose** | v2 | Orchestration |
| **mkcert** | latest | HTTPS local (bắt buộc compose chính thức) |
| **Git** | ≥ 2.30 | Sample workspace / VCS |
| **minikube + helm** | (lab 09) | Deploy K8s |
| RAM | ≥ 8 GB | 4–6 container Terrakube |

```bash
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh
```

---

## Chạy nhanh (30–45 phút)

```bash
cd learn-python-ai   # hoặc python-all

# Bước 1 — Kiểm tra Docker, mkcert
bash 21-terraform-ui-terrakube/scripts/01-check-prerequisites.sh

# Bước 2 — Cập nhật /etc/hosts (script in hướng dẫn)
bash 21-terraform-ui-terrakube/scripts/02-prepare-hosts.sh --print

# Bước 3 — Clone Terrakube + Docker Compose + HTTPS
bash 21-terraform-ui-terrakube/scripts/03-deploy-terrakube-compose.sh

# Bước 4 — Đợi healthy (~2 phút)
bash 21-terraform-ui-terrakube/scripts/04-wait-healthy.sh

# Bước 5 — Mở UI
# https://terrakube.platform.local
# User: admin@example.com / Password: admin
```

Chi tiết từng bước: [docs/02-cai-dat-docker-compose.md](docs/02-cai-dat-docker-compose.md)

---

## Lộ trình học (2–3 tuần)

```
Tuần 1:  Khái niệm TACOS + deploy Compose (docs 01–02, lab 01–03)
Tuần 2:  Workspace, VCS, plan/apply UI (docs 03–04, lab 04–07)
Tuần 3:  Helm/minikube, RBAC, capstone (docs 05–07, lab 08–10)
```

---

## Cấu trúc module

```
21-terraform-ui-terrakube/
├── README.md
├── docs/                    # Hướng dẫn chi tiết
├── terraform/
│   └── sample-workspace/    # Code Terraform cho lab (provider local)
├── helm/
│   └── values-minikube.yaml # Lab K8s
├── labs/                    # 10 lab hands-on
├── scripts/                 # Deploy, verify, teardown
├── cheatsheet/
└── exercises/
```

---

## Lab (10 lab)

| # | Lab | Thời gian |
|---|-----|-----------|
| 01 | [Deploy Docker Compose](labs/basic/lab01-deploy-compose.md) | 60 phút |
| 02 | [Đăng nhập & tour UI](labs/basic/lab02-ui-tour.md) | 30 phút |
| 03 | [Organization & Project](labs/basic/lab03-org-project.md) | 45 phút |
| 04 | [Workspace + Plan/Apply](labs/intermediate/lab04-workspace-run.md) | 90 phút |
| 05 | [Xem State trên UI](labs/intermediate/lab05-state-ui.md) | 45 phút |
| 06 | [Kết nối GitHub VCS](labs/intermediate/lab06-vcs-github.md) | 90 phút |
| 07 | [RBAC team & quyền](labs/intermediate/lab07-rbac.md) | 60 phút |
| 08 | [Module Registry (private)](labs/advanced/lab08-module-registry.md) | 60 phút |
| 09 | [Helm trên minikube](labs/advanced/lab09-helm-minikube.md) | 120 phút |
| 10 | [Capstone pipeline](labs/advanced/lab10-capstone.md) | 120 phút |

---

## Tài liệu

1. [Lộ trình](docs/00-lo-trinh.md)
2. [Giới thiệu TACOS & Terrakube](docs/01-gioi-thieu-terrakube.md)
3. [Cài Docker Compose + HTTPS](docs/02-cai-dat-docker-compose.md)
4. [Workspace & Run](docs/03-workspace-va-run.md)
5. [Tích hợp Git / VCS](docs/04-vcs-github.md)
6. [State, Registry, RBAC](docs/05-state-registry-rbac.md)
7. [Helm + minikube](docs/06-helm-minikube.md)
8. [Production checklist](docs/07-production-checklist.md)

---

## Liên kết chính thức

- [Terrakube Docs](https://docs.terrakube.io/)
- [GitHub terrakube-io/terrakube](https://github.com/terrakube-io/terrakube)
- [Helm Chart](https://github.com/terrakube-io/terrakube-helm-chart)
