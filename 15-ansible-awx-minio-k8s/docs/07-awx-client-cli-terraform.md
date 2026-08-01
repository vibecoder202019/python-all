# AWX Client — CLI, kết nối server & quản lý ( + Terraform tùy chọn)

Hướng dẫn dùng **AWX CLI** (`awx`) và **Terraform AWX provider** để kết nối AWX server, quản lý resource và chạy job — bổ sung cho Python REST API (examples 01–06).

---

## AWX Client là gì?

| Công cụ | Vai trò |
|---------|---------|
| **AWX Web UI** | Click launch job, xem log |
| **Python + requests** | Tích hợp app (Module 15 `common.py`) |
| **awx CLI** | Terminal — quản lý & launch nhanh |
| **Terraform (awx provider)** | IaC — Project, Inventory, Job Template as code |

**AWX server** = cluster K8s (`k8s/awx/`). **AWX client** = máy bạn (laptop/CI) gọi API qua CLI/Terraform/Python.

---

## Phần 1 — Cài đặt AWX CLI

### Cài awxkit (pip)

```bash
cd learn-python-ai
source .venv/bin/activate
pip install awxkit

awx --version
```

Hoặc script module:

```bash
bash 15-ansible-awx-minio-k8s/scripts/06-setup-awx-cli.sh
```

| Gói | Lệnh | Giải thích |
|-----|------|------------|
| `awxkit` | `awx` | CLI chính thức gọi AWX REST API v2 |

---

## Phần 2 — Kết nối AWX server

### Bước 1 — AWX phải reachable

**Cách A — Port-forward (lab nhanh):**

```bash
kubectl port-forward svc/awx-service 8052:80 -n awx
# AWX URL: http://localhost:8052
```

**Cách B — Ingress (sau deploy):**

```bash
# /etc/hosts: 127.0.0.1 awx.local
open http://awx.local
```

### Bước 2 — Tạo OAuth Token

1. Đăng nhập AWX UI (`admin` + password từ secret K8s)
2. Góc phải → **User** → **Tokens** → **Create token**
3. Copy token — **chỉ hiện 1 lần**

```bash
kubectl get secret awx-admin-password -n awx -o jsonpath='{.data.password}' | base64 -d && echo
```

### Bước 3 — Cấu hình CLI

**Cách 1 — Biến môi trường (khuyến nghị lab):**

```bash
export AWX_HOST="http://localhost:8052"
export AWX_TOKEN="your-oauth-token"
export AWX_VERIFY_SSL=false   # lab HTTP
```

**Cách 2 — File credentials:**

```bash
mkdir -p ~/.awx
cp 15-ansible-awx-minio-k8s/awx-cli/credentials.example ~/.awx/credentials
chmod 600 ~/.awx/credentials
# Sửa host + oauth_token trong file
```

Nội dung mẫu:

```ini
[default]
host = http://localhost:8052
oauth_token = YOUR_TOKEN
verify_ssl = false
```

### Bước 4 — Kiểm tra kết nối

```bash
awx ping
# {"version": "...", "online": true}

awx me
# Thông tin user đang đăng nhập
```

Script demo:

```bash
bash 15-ansible-awx-minio-k8s/scripts/06-setup-awx-cli.sh --test
```

---

## Phần 3 — Quản lý bằng AWX CLI

### Cấu trúc tài nguyên AWX

```
Organization
  └── Project (Git SCM)
  └── Inventory
        └── Hosts
  └── Job Template = Project + Playbook + Inventory
  └── Jobs (mỗi lần launch)
```

### Liệt kê resource

```bash
# Job templates
awx job_templates list -f json | jq '.results[] | {id, name}'

# Projects
awx projects list

# Inventories
awx inventories list

# Jobs đang chạy / gần đây
awx jobs list --status running
awx jobs list --order_by -created
```

### Đồng bộ Project (pull Git)

```bash
# Lấy project id
awx projects list -f json | jq '.results[] | select(.name=="My Project") | .id'

awx project update 5 --wait
# Hoặc
awx projects sync --name "python-demo-playbooks" --wait
```

### Launch Job Template

```bash
# Theo tên
awx job_templates launch "python-script-demo" --monitor

# Theo ID + extra vars
awx job_templates launch 7 \
  --extra_vars '{"demo_mode": true, "message": "hello from cli"}' \
  --monitor

# Không chờ — lấy job id
awx job_templates launch 7 -f json | jq .id
```

| Flag | Ý nghĩa |
|------|---------|
| `--monitor` | Chờ job xong, in stdout |
| `--extra_vars` | JSON biến Ansible |
| `-f json` | Output JSON cho script |

### Xem log job

```bash
awx jobs stdout 42 --follow
awx jobs get 42 -f json | jq '{status, started, finished, elapsed}'
```

### Tạo resource nhanh (CLI — học thủ công)

```bash
# Organization
awx organizations create --name "CLI-Lab-Org"

# Inventory
awx inventories create --name "cli-inv" --organization 3

# Host
awx hosts create --name localhost --inventory 5 \
  --variables '{"ansible_connection": "local"}'
```

> Production: dùng **Terraform** (phần 4) hoặc AWX UI để tránh lệch cấu hình.

---

## Phần 4 — Terraform AWX Client (tùy chọn)

Quản lý cùng resource bằng code — thư mục [`terraform/awx-client/`](../terraform/awx-client/).

```bash
cd 15-ansible-awx-minio-k8s/terraform/awx-client
cp terraform.tfvars.example terraform.tfvars
# awx_host, awx_token, scm_url

bash ../../scripts/07-terraform-awx-client.sh plan
bash ../../scripts/07-terraform-awx-client.sh apply
```

Sau apply:

```bash
# Launch job template Terraform vừa tạo
awx job_templates launch "python-script-demo-tf" --monitor
```

### Import resource đã tạo tay trên UI

```bash
terraform import awx_job_template.python_script 7
```

---

## Phần 5 — So sánh 3 cách client

| Tác vụ | Python API | awx CLI | Terraform |
|--------|------------|---------|-----------|
| List templates | `list_job_templates()` | `awx job_templates list` | data source |
| Launch job | `launch_job()` | `awx job_templates launch` | không (dùng CLI/CI) |
| Tạo template | POST API | `awx job_templates create` | `awx_job_template` |
| GitOps / review | ❌ | ❌ | ✅ plan/apply |
| Tích hợp app Python | ✅ | subprocess awx | ❌ |

**Khuyến nghị:**

- **Học / debug:** awx CLI
- **App automation:** Python `AWXClient`
- **Định nghĩa infra AWX:** Terraform (tùy chọn)

---

## Phần 6 — Workflow lab đầy đủ

```bash
# 1. Deploy AWX + MinIO
bash 15-ansible-awx-minio-k8s/scripts/04-deploy-awx-instance.sh

# 2. Port-forward + token
kubectl port-forward svc/awx-service 8052:80 -n awx &
export AWX_HOST=http://localhost:8052
export AWX_TOKEN=<token>

# 3. CLI
bash 15-ansible-awx-minio-k8s/scripts/06-setup-awx-cli.sh --test
awx job_templates list

# 4. (Tùy chọn) Terraform client
bash 15-ansible-awx-minio-k8s/scripts/07-terraform-awx-client.sh apply

# 5. Launch
awx job_templates launch "python-script-demo-tf" --monitor

# 6. Python API (song song)
python 15-ansible-awx-minio-k8s/examples/02_launch_job.py
```

---

## Troubleshooting

| Lỗi | Cách xử lý |
|-----|------------|
| `401 Unauthorized` | Token sai/hết hạn — tạo token mới |
| `Connection refused` | Chưa port-forward hoặc AWX pod chưa Ready |
| `SSL verification failed` | `AWX_VERIFY_SSL=false` hoặc `verify_ssl = false` |
| Project sync fail | Kiểm tra `scm_url`, credential Git trên AWX |
| Terraform provider error | AWX version vs provider version — xem [registry](https://registry.terraform.io/providers/iwonderanddev/awx/latest) |

---

## Bài tập

1. Cấu hình `awx ping` thành công
2. List và launch 1 job template bằng CLI
3. Apply Terraform `awx-client` và launch template Terraform tạo
4. So sánh output `awx jobs stdout` vs Python `step05_monitor_job.py`

→ [exercises/bai_tap.md](../exercises/bai_tap.md)

---

## Liên kết

- [Terraform awx-client](../terraform/awx-client/README.md)
- [Module 19 Terraform](../19-vault-terraform/README.md)
- [AWX API docs](https://ansible.readthedocs.io/projects/awx/en/latest/api/index.html)
