# Terraform — AWX Client (tùy chọn)

Quản lý **tài nguyên trên AWX server** bằng Terraform (Job Template, Project, Inventory…) — **không** deploy AWX K8s (phần đó dùng manifests + scripts `02–04`).

> **Yêu cầu:** AWX đã chạy + token API. Cài AWX trước: `scripts/04-deploy-awx-instance.sh`

---

## Provider

Dùng community provider [`iwonderanddev/awx`](https://registry.terraform.io/providers/iwonderanddev/awx/latest/docs).

| Input | Mô tả |
|-------|--------|
| `awx_host` | URL AWX, vd `http://localhost:8052` hoặc `http://awx.local` |
| `awx_token` | OAuth token từ AWX UI (User → Tokens) |
| `scm_url` | Git repo chứa playbook (fork python-all) |
| `scm_branch` | `main` |

---

## Chạy nhanh

```bash
# 1. Port-forward AWX (nếu chưa có ingress)
kubectl port-forward svc/awx-service 8052:80 -n awx

# 2. Tạo token trên AWX UI → copy

# 3. Terraform
cd 15-ansible-awx-minio-k8s/terraform/awx-client
cp terraform.tfvars.example terraform.tfvars
# Sửa awx_host, awx_token, scm_url

bash ../../scripts/07-terraform-awx-client.sh plan
bash ../../scripts/07-terraform-awx-client.sh apply   # khi sẵn sàng
```

---

## Resource được tạo (lab)

| Resource | Mục đích |
|----------|----------|
| `awx_organization` | Organization lab |
| `awx_project` | Project SCM → ansible-playbook/python-demo |
| `awx_inventory` | Inventory localhost lab |
| `awx_host` | Host `localhost` |
| `awx_job_template` | Template chạy `playbook-script.yml` |

---

## So với AWX CLI

| | **awx CLI** | **Terraform** |
|---|-------------|---------------|
| Use case | Chạy job ad-hoc, debug | GitOps / IaC, review PR |
| State | Không | `.tfstate` |
| Idempotent | Không | Có (plan/apply) |

Dùng **cả hai**: Terraform định nghĩa template; CLI launch test nhanh.

---

## Teardown

```bash
bash ../../scripts/07-terraform-awx-client.sh destroy
```

Không xóa AWX server — chỉ xóa resource Terraform quản lý.

Doc CLI: [docs/07-awx-client-cli-terraform.md](../docs/07-awx-client-cli-terraform.md)
