# Module 18: Tự học CKA + CKS — Kubernetes Administrator & Security

Lộ trình **tự học** chuẩn bị thi **CKA** (Certified Kubernetes Administrator) và **CKS** (Certified Kubernetes Security Specialist) — lý thuyết chi tiết + lab thực hành từ basic → advanced.

> **Lưu ý:** Module này **không thay thế** khóa học chính thức CNCF/Linux Foundation — bổ trợ ôn tập và thực hành tay.

---

## CKA vs CKS — Khác nhau thế nào?

| | **CKA** | **CKS** |
|---|---------|---------|
| **Focus** | Vận hành cluster K8s | Bảo mật cluster K8s |
| **Yêu cầu** | Hiểu K8s cơ bản | **Phải có CKA** (hoặc CKAD) còn hạn |
| **Thời gian thi** | 2 giờ | 2 giờ |
| **Số câu** | ~17 task | ~15 task |
| **Điểm đậu** | 66% | 67% |
| **Mở tài liệu** | ✅ kubernetes.io/docs | ✅ kubernetes.io/docs |

---

## Phạm vi thi (Exam Domains)

### CKA (2024/2025)

| Domain | Trọng số |
|--------|----------|
| Storage | 10% |
| Troubleshooting | 30% |
| Workloads & Scheduling | 15% |
| Services & Networking | 20% |
| Cluster Architecture, Installation & Configuration | 25% |

### CKS

| Domain | Trọng số |
|--------|----------|
| Cluster Setup & Hardening | 10% |
| Cluster Hardening | 15% |
| System Hardening | 15% |
| Minimize Microservice Vulnerabilities | 20% |
| Supply Chain Security | 20% |
| Monitoring, Logging, Runtime Security | 20% |

---

## Yêu cầu môi trường

| Công cụ | Mục đích |
|---------|----------|
| **kubectl** ≥ 1.28 | CLI chính khi thi CKA/CKS |
| **minikube** hoặc **kind** | Cluster lab local (khuyến nghị) |
| **kubeadm** cluster (VM) | Lab nâng cao CKA (backup etcd) |
| **helm** | Một số lab CKS |
| RAM ≥ 8 GB | Chạy cluster + lab |

```bash
# Setup lab (chạy 1 lần)
bash 18-cka-cks-kubernetes/scripts/01-setup-lab.sh
```

---

## Lộ trình học (8–12 tuần)

```
Tuần 1–2:  Nền tảng + Lab Basic (01–04)
Tuần 3–4:  CKA Workloads, Services, Storage (docs 02–04)
Tuần 5–6:  CKA Troubleshooting + Lab Intermediate (05–08)
Tuần 7–8:  CKA Cluster Architecture (docs 01, lab advanced 09–10)
Tuần 9–10: CKS Hardening + Security (docs 06–08)
Tuần 11–12: Mock exam + Lab Advanced CKS (11–14)
```

---

## Cấu trúc module

```
18-cka-cks-kubernetes/
├── README.md                 # File này
├── docs/                     # Lý thuyết chi tiết theo domain thi
│   ├── 00-lo-trinh-cka-cks.md
│   ├── 01-cka-cluster-architecture.md
│   ├── 02-cka-workloads-scheduling.md
│   ├── 03-cka-services-networking.md
│   ├── 04-cka-storage-troubleshooting.md
│   ├── 05-cks-cluster-hardening.md
│   ├── 06-cks-system-hardening.md
│   ├── 07-cks-microservice-supply-chain.md
│   ├── 08-cks-runtime-monitoring.md
│   └── 09-mock-exam-chien-luoc.md
├── labs/
│   ├── basic/        # Lab 01–04 (người mới K8s admin)
│   ├── intermediate/ # Lab 05–08 (CKA core)
│   └── advanced/     # Lab 09–14 (CKA troubleshoot + CKS)
├── manifests/        # YAML mẫu + broken YAML để sửa
├── cheatsheet/       # Lệnh kubectl hay dùng khi thi
├── scripts/          # Setup cluster, chạy lab, verify
└── exercises/        # Bài tập + đáp án
```

---

## Lab thực hành (14 lab)

| # | Lab | Level | CKA/CKS | Thời gian |
|---|-----|-------|---------|-----------|
| 01 | [Pod, Label, Namespace](labs/basic/lab01-pods-labels.md) | Basic | CKA | 30 phút |
| 02 | [Deployment & Scaling](labs/basic/lab02-deployments.md) | Basic | CKA | 30 phút |
| 03 | [Service & DNS](labs/basic/lab03-services.md) | Basic | CKA | 45 phút |
| 04 | [ConfigMap & Secret](labs/basic/lab04-config-secret.md) | Basic | CKA | 30 phút |
| 05 | [Ingress & NetworkPolicy](labs/intermediate/lab05-ingress-netpol.md) | Intermediate | CKA | 45 phút |
| 06 | [PVC, PV, StorageClass](labs/intermediate/lab06-storage.md) | Intermediate | CKA | 45 phút |
| 07 | [Scheduling & Taints](labs/intermediate/lab07-scheduling.md) | Intermediate | CKA | 45 phút |
| 08 | [RBAC](labs/intermediate/lab08-rbac.md) | Intermediate | CKA/CKS | 60 phút |
| 09 | [Troubleshoot Pod](labs/advanced/lab09-troubleshoot.md) | Advanced | CKA | 60 phút |
| 10 | [Backup etcd](labs/advanced/lab10-etcd-backup.md) | Advanced | CKA | 60 phút |
| 11 | [Pod Security Standards](labs/advanced/lab11-pod-security.md) | Advanced | CKS | 45 phút |
| 12 | [NetworkPolicy Zero Trust](labs/advanced/lab12-netpol-zero-trust.md) | Advanced | CKS | 45 phút |
| 13 | [Audit Log & Falco](labs/advanced/lab13-audit-falco.md) | Advanced | CKS | 60 phút |
| 14 | [Mock Exam Mixed](labs/advanced/lab14-mock-exam.md) | Advanced | CKA+CKS | 120 phút |

---

## Chạy nhanh

```bash
cd python-all   # hoặc learn-python-ai

# 1. Tạo cluster lab
bash 18-cka-cks-kubernetes/scripts/01-setup-lab.sh

# 2. Chạy lab basic tuần tự
bash 18-cka-cks-kubernetes/scripts/02-run-lab.sh basic 01

# 3. Verify lab hoàn thành
bash 18-cka-cks-kubernetes/scripts/03-verify-lab.sh 01

# 4. Xem cheatsheet
cat 18-cka-cks-kubernetes/cheatsheet/kubectl-cka.md
```

---

## Chiến lược thi CKA/CKS

1. **Đọc kỹ đề** — copy namespace, tên resource vào notepad
2. **`-n namespace`** — 80% lỗi mất điểm do quên namespace
3. **`kubectl explain`** — tra cứu field YAML khi thi: `kubectl explain pod.spec.containers`
4. **`--dry-run=client -o yaml`** — tạo YAML nhanh, sửa, apply
5. **Bookmark** kubernetes.io/docs — thi được mở tài liệu chính thức
6. **Skip** câu khó — làm câu dễ trước, quay lại sau

Chi tiết: [docs/09-mock-exam-chien-luoc.md](docs/09-mock-exam-chien-luoc.md)

---

## Tài liệu đọc theo thứ tự

1. [Lộ trình CKA/CKS](docs/00-lo-trinh-cka-cks.md)
2. [CKA — Cluster Architecture](docs/01-cka-cluster-architecture.md)
3. [CKA — Workloads & Scheduling](docs/02-cka-workloads-scheduling.md)
4. [CKA — Services & Networking](docs/03-cka-services-networking.md)
5. [CKA — Storage & Troubleshooting](docs/04-cka-storage-troubleshooting.md)
6. [CKS — Cluster Hardening](docs/05-cks-cluster-hardening.md)
7. [CKS — System Hardening](docs/06-cks-system-hardening.md)
8. [CKS — Supply Chain & Microservices](docs/07-cks-microservice-supply-chain.md)
9. [CKS — Runtime & Monitoring](docs/08-cks-runtime-monitoring.md)

---

## Liên kết module liên quan

- [Module 15 — AWX + MinIO + K8s](../15-ansible-awx-minio-k8s/README.md)
- [Module 16 — K8s Security](../16-k8s-security/README.md)
- [Module 17 — Go + Helm](../17-go-language-k8s/README.md)

## Tài liệu chính thức

- [CKA Exam](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/)
- [CKS Exam](https://training.linuxfoundation.org/certification/certified-kubernetes-security-specialist/)
- [Kubernetes Documentation](https://kubernetes.io/docs/home/)
