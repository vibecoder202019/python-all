# Module 28: Python · Backstage · Terraform · AWX · Kubernetes

Project tích hợp **Developer Portal (Backstage)** + **IaC (Terraform)** + **Automation (Ansible AWX)** + **Runtime (K8s)**, điều khiển bằng **Python API**.

Bạn có thể **gọi API để tạo task trên Ansible AWX** — task đó chạy playbook **deploy app vào Kubernetes**.

**Liên quan:** [15 AWX](../15-ansible-awx-minio-k8s/README.md) · [19 Terraform](../19-vault-terraform/README.md) · [23 Agent Bridge](../23-mcp-ai-agent-awx/README.md) · [09 FastAPI](../09-fastapi/README.md)

---

## Mục tiêu

1. Hiểu luồng: Backstage / curl → Python Bridge → AWX launch → Ansible → K8s  
2. Dùng `POST /api/v1/jobs` và `POST /api/v1/deploy` tạo task AWX  
3. Terraform chuẩn bị namespace/quota; Ansible rolling app  
4. Đăng ký Software Template Backstage (hoặc giả lập scaffolder)  
5. Chạy được toàn bộ demo **không cần** AWX/cluster (fixture)

---

## Cách tự học

```bash
cd learn-python-ai
bash 28-python-backstage-awx-k8s/scripts/setup.sh
bash 28-python-backstage-awx-k8s/scripts/02-run-all-examples.sh
bash 28-python-backstage-awx-k8s/scripts/03-run-bridge.sh   # terminal riêng
bash 28-python-backstage-awx-k8s/scripts/08-test-bridge-api.sh
```

Chi tiết lệnh: [readme_manual.md](readme_manual.md) · Labs: [labs/](labs/)

---

## Lý thuyết nền tảng

### Vì sao tách 5 lớp?

| Muốn… | Dùng |
|-------|------|
| Dev tự phục vụ, có catalog | **Backstage** |
| Namespace / quota / policy ổn định | **Terraform** |
| Audit, RBAC, schedule job | **AWX** |
| Apply Deployment theo biến | **Ansible** |
| API ổn định cho portal/CI | **Python Bridge** |

**Ví von:** Terraform xây “khu đất + hàng rào” (namespace). AWX+Ansible là “đội thi công” mỗi lần bạn bấm form Backstage / gọi API. Python Bridge là “quầy tiếp nhận đơn”.

### Tạo task AWX = Launch Job Template

Trên UI: Templates → Launch.  
Qua API: `POST /api/v2/job_templates/{id}/launch/` kèm `extra_vars`.  
Module này bọc API đó trong Bridge để Backstage/CI không cầm raw AWX token lung tung (token nằm phía Bridge).

---

## Nội dung chính

### 1. Python AWX client + CLI

- `project/awx_client.py` — list / launch / poll (có **demo fixture**)  
- `project/run_launch.py` — `list` | `launch` | `deploy`

### 2. Bridge FastAPI

| Endpoint | Việc |
|----------|------|
| `POST /api/v1/jobs` | Tạo task AWX tùy template |
| `POST /api/v1/deploy` | Shortcut deploy K8s |
| `POST /api/scaffolder/run` | Payload Backstage |
| `GET /api/backstage/catalog.yaml` | Export Resource entities |

### 3. Terraform / Ansible / K8s / Backstage

Xem [docs/01](docs/01-platform-architecture.md) → [docs/04](docs/04-terraform-ansible-k8s.md).

---

## Cấu trúc thư mục

```
28-python-backstage-awx-k8s/
├── project/           # awx_client, bridge_server, CLI
├── examples/          # 01–05
├── backstage/         # template + catalog
├── terraform/         # namespace + quota
├── ansible/           # deploy-app.yml
├── k8s/               # demo-app.yaml
├── docs/ labs/ scripts/
└── data/              # .env.example, awx_fixture.json
```

---

## FAQ

**Q: Chưa có AWX vẫn học được?**  
A: Có — `AWX_DEMO=true` dùng fixture.

**Q: Khác Module 23 Agent Bridge chỗ nào?**  
A: 23 phục vụ AI/n8n; 28 phục vụ **Backstage portal + Terraform prep + K8s deploy playbook** như một platform path.

**Q: Production có để Bridge public không?**  
A: Không. Chỉ nội bộ / mesh; mTLS hoặc SSO; AWX token scope tối thiểu.

---

## Bài tập

Xem [exercises/bai_tap.md](exercises/bai_tap.md).

## Cheatsheet

[cheatsheet/platform.md](cheatsheet/platform.md)
