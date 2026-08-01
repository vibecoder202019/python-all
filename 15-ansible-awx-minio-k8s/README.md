# Module 15: Ansible AWX + MinIO + Kubernetes + Python

Học **Python thực chiến** kết hợp **AWX** (Ansible automation), **MinIO** (S3 storage) và triển khai trên **Kubernetes** — dành cho DevOps Engineer.

**Repo liên quan:** [k8s-awx-minio-guide](https://github.com/vibecoder202019/mlops/tree/main/k8s-awx-minio-guide) — tài liệu infra chi tiết (trong repo MLOps)

**Lab capstone (AI + n8n):** Sau module này, học [Module 23 — MCP AI Agent](../23-mcp-ai-agent-awx/README.md) và [Module 24 — n8n](../24-n8n-ai-automation/labs/capstone/README.md) để tự động hóa AWX qua AI agent và workflow.

## Mục tiêu

- Triển khai AWX và MinIO trên Kubernetes (local)
- Gọi **AWX REST API** từ Python (`requests`)
- Chạy **Python script** trong Ansible playbook trên AWX
- Upload artifact lên **MinIO** bằng `boto3`
- Hoàn thành CLI **AWX Automation Toolkit** qua 6 bước

---

## Lý thuyết nền tảng

### AWX là gì?

**AWX** = giao diện web quản lý Ansible. Bạn tạo **Job Template** → nhấn Launch → AWX chạy playbook trên inventory.

### MinIO là gì?

**MinIO** = object storage tương thích **Amazon S3 API**. Python dùng `boto3` với `endpoint_url` trỏ về MinIO.

### Python + AWX — 3 cách tích hợp

| Cách | Mô tả | File ví dụ |
|------|-------|------------|
| **Trong playbook** | `script` module chạy file `.py` | `examples/04_python_script_for_ansible.py` |
| **Gọi AWX API** | Python trigger job, poll status | `examples/02_launch_job.py` |
| **Pipeline** | Report Python → MinIO → AWX | `examples/06_full_pipeline.py` |
| **AWX CLI** | Terminal — list/launch/sync | `examples/07_awx_cli_launch.sh` |
| **Terraform (tùy chọn)** | IaC Job Template, Project | `terraform/awx-client/` |

### Kiến trúc lab

```
Browser → AWX Web UI (awx.local)
              │
              ▼
         AWX Task Pod ──Python playbook──► MinIO (S3)
              ▲
Python CLI ───┘ (REST API launch job)
awx CLI ──────┘ (awx job_templates launch)
Terraform ────┘ (awx_job_template as code — tùy chọn)
```

---

## Yêu cầu

- Hoàn thành Module 01–05 (Python cơ bản, requests)
- Module 12–13 (DevOps, boto3) — khuyến nghị
- Docker Desktop + Kubernetes enabled (8 GB RAM)
- `kubectl`, `helm` (cài AWX Operator)

---

## Chạy nhanh (1 lệnh)

```bash
# Cài Python deps (1 lần)
bash 15-ansible-awx-minio-k8s/scripts/setup.sh

# Demo Python — KHÔNG cần AWX/MinIO
bash 15-ansible-awx-minio-k8s/scripts/run_all_examples.sh --demo

# Dự án 6 bước (demo mode)
bash 15-ansible-awx-minio-k8s/scripts/run_project.sh

# Triển khai K8s (AWX + MinIO — ~15 phút)
bash 15-ansible-awx-minio-k8s/scripts/01-check-prerequisites.sh
bash 15-ansible-awx-minio-k8s/scripts/02-deploy-minio.sh
bash 15-ansible-awx-minio-k8s/scripts/03-deploy-awx-operator.sh
bash 15-ansible-awx-minio-k8s/scripts/04-deploy-awx-instance.sh
bash 15-ansible-awx-minio-k8s/scripts/05-verify-all.sh
```

### Cấu hình AWX token

```bash
# Port-forward AWX
kubectl port-forward svc/awx-service 8052:80 -n awx

# Tạo token: AWX UI → User → Tokens → Create
export AWX_URL="http://localhost:8052"
export AWX_TOKEN="your-token-here"

# Test API
python 15-ansible-awx-minio-k8s/examples/01_awx_api_basics.py

# AWX CLI (awxkit)
bash 15-ansible-awx-minio-k8s/scripts/06-setup-awx-cli.sh
export AWX_HOST="http://localhost:8052"
export AWX_TOKEN="your-token-here"
bash 15-ansible-awx-minio-k8s/scripts/06-setup-awx-cli.sh --test

# Terraform AWX client (tùy chọn — sau khi AWX chạy)
bash 15-ansible-awx-minio-k8s/scripts/07-terraform-awx-client.sh plan
```

---

## Lộ trình

| Bước | File | Nội dung | Level |
|------|------|----------|-------|
| 01 | `examples/01_awx_api_basics.py` | Kết nối AWX API, list templates | Cơ bản |
| 02 | `examples/02_launch_job.py` | Launch Job Template | Cơ bản |
| 03 | `examples/03_list_resources.py` | List projects, jobs | Trung bình |
| 04 | `examples/04_python_script_for_ansible.py` | Script cho Ansible module | Trung bình |
| 05 | `examples/05_minio_boto3.py` | Upload MinIO bằng boto3 | Trung bình |
| 06 | `examples/06_full_pipeline.py` | Pipeline Python→MinIO→AWX | Nâng cao |
| 07 | `examples/07_awx_cli_launch.sh` | Launch job bằng **awx CLI** | Trung bình |
| 📘 | `docs/07-awx-client-cli-terraform.md` | **AWX CLI + Terraform client** chi tiết | Đọc thêm |
| 🔧 | `terraform/awx-client/` | Terraform quản lý template/project (tùy chọn) | Nâng cao |
| 🎯 | `project/` | **AWX Automation CLI** (6 step) | Dự án |

---

## Dự án tuần tự: AWX Automation CLI

```
project/
├── common.py              # AWXClient, MinIO helper
├── step01_awx_connect.py  # Kết nối + xác minh API
├── step02_launch_job.py   # Launch job template
├── step03_minio_upload.py # Upload report S3
├── step04_ansible_script.py # Python script cho Ansible
├── step05_monitor_job.py  # Poll job + stdout
└── step06_final.py        # CLI hoàn chỉnh
```

```bash
python 15-ansible-awx-minio-k8s/project/step06_final.py --help
python 15-ansible-awx-minio-k8s/project/step06_final.py list-templates
python 15-ansible-awx-minio-k8s/project/step06_final.py pipeline --demo
python 15-ansible-awx-minio-k8s/project/step06_final.py launch --template-id 7 --wait
```

---

## Kubernetes manifests

Manifest AWX + MinIO nằm trong `k8s/`:

```
k8s/
├── minio/     # Namespace, Secret, PVC, Deployment, Service, Ingress
└── awx/       # AWX Operator CR, Ingress
```

Thêm vào `/etc/hosts`:
```
127.0.0.1 minio.local minio-api.local awx.local
```

| Dịch vụ | URL | Credential |
|---------|-----|------------|
| MinIO Console | http://minio.local | minioadmin / minioadmin123 |
| AWX Web UI | http://awx.local | admin / (kubectl get secret) |

---

## Ansible playbook cho AWX

```
ansible-playbook/python-demo/
├── playbook-script.yml         # Chạy Python script
├── playbook-minio-python.yml   # Python → MinIO
└── playbook-custom-module.yml  # Custom module
```

Tạo Job Template trên AWX:
- **Project SCM:** Git → repo python-all, path `15-ansible-awx-minio-k8s/ansible-playbook/python-demo/`
- **Playbook:** `playbook-script.yml`

---

## Bash scripts

| Script | Mục đích |
|--------|---------|
| `scripts/setup.sh` | Cài requests, boto3 |
| `scripts/run_all_examples.sh` | Chạy examples (--demo) |
| `scripts/run_project.sh` | Dự án 6 bước |
| `scripts/01-check-prerequisites.sh` | Kiểm tra K8s |
| `scripts/02-deploy-minio.sh` | Deploy MinIO |
| `scripts/03-deploy-awx-operator.sh` | Cài AWX Operator |
| `scripts/04-deploy-awx-instance.sh` | Tạo AWX instance |
| `scripts/05-verify-all.sh` | Kiểm tra health |
| `scripts/06-setup-awx-cli.sh` | Cài `awxkit`, test `awx ping` |
| `scripts/07-terraform-awx-client.sh` | Plan/apply Terraform AWX client |

---

## AWX Client — CLI & Terraform (tùy chọn)

**AWX server** = deploy K8s (`scripts/02–04`). **AWX client** = laptop/CI quản lý qua API.

| Công cụ | Khi dùng |
|---------|----------|
| **awx CLI** | Debug, launch job, sync project |
| **Python API** | Tích hợp ứng dụng |
| **Terraform** | GitOps — Organization, Project, Job Template |

Hướng dẫn đầy đủ: [docs/07-awx-client-cli-terraform.md](docs/07-awx-client-cli-terraform.md)

```bash
# CLI
pip install awxkit   # hoặc scripts/06-setup-awx-cli.sh
export AWX_HOST=http://localhost:8052 AWX_TOKEN=xxx
awx job_templates list
awx job_templates launch "My Template" --monitor

# Terraform (tùy chọn)
cd terraform/awx-client && cp terraform.tfvars.example terraform.tfvars
bash ../../scripts/07-terraform-awx-client.sh apply
```

## Giải thích chi tiết (Tự học)

### File `project/common.py`

```python
class AWXClient:
    def launch_job(self, template_id, extra_vars=None):
        # POST /api/v2/job_templates/{id}/launch/
        return self.post(f"/job_templates/{template_id}/launch/", payload)
```

| Method | API | Mục đích |
|--------|-----|----------|
| `list_job_templates()` | GET `/job_templates/` | Liệt kê template |
| `launch_job()` | POST `.../launch/` | Chạy job |
| `wait_for_job()` | GET `/jobs/{id}/` (poll) | Đợi hoàn thành |
| `upload_to_minio()` | boto3 S3 | Upload artifact |

### File `examples/02_launch_job.py`

```python
result = ctx.client.launch_job(template_id, extra_vars=extra)
job_id = result.get("job")  # API trả job id mới tạo
```

`extra_vars` truyền biến vào playbook Ansible — tương đương `-e` khi chạy `ansible-playbook`.

### AWX REST API — Endpoint quan trọng

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/api/v2/job_templates/` | List templates |
| POST | `/api/v2/job_templates/{id}/launch/` | Launch job |
| GET | `/api/v2/jobs/{id}/` | Job status |
| GET | `/api/v2/jobs/{id}/stdout/?format=txt` | Job output |

---

## FAQ

**Hỏi:** Không có AWX, học module này được không?  
**Đáp:** Có — chạy `--demo` cho examples/project. Phần K8s cần Docker Desktop.

**Hỏi:** `401 Unauthorized` khi gọi API?  
**Đáp:** Token hết hạn — tạo token mới trên AWX UI.

**Hỏi:** MinIO upload fail?  
**Đáp:** `kubectl port-forward svc/minio 9000:9000 -n minio` hoặc dùng DNS nội bộ từ AWX pod.

**Hỏi:** `awx: command not found`?  
**Đáp:** `bash scripts/06-setup-awx-cli.sh` hoặc `pip install awxkit`.

**Hỏi:** Terraform AWX provider lỗi version?  
**Đáp:** Xem [terraform/awx-client/README.md](terraform/awx-client/README.md) — AWX server phải đang chạy trước khi apply.

---

## Bài tập

Xem [exercises/bai_tap.md](exercises/bai_tap.md) — 5 bài từ dễ đến khó.

---

## Liên kết

- [Module 12 — DevOps](../12-python-devops-devsecops/README.md)
- [Module 13 — AWS boto3](../13-python-aws-infra/README.md)
- [k8s-awx-minio-guide](https://github.com/vibecoder202019/mlops/tree/main/k8s-awx-minio-guide) — tài liệu infra đầy đủ
