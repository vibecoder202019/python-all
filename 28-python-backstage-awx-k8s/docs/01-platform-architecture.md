# Kiến trúc Platform: Python · Backstage · Terraform · AWX · K8s

```
┌─────────────┐     HTTP      ┌──────────────────┐     REST      ┌─────────────┐
│  Backstage  │──────────────►│  Python Bridge   │─────────────►│ Ansible AWX │
│  Template   │  /scaffolder │  FastAPI :8090   │  /launch/    │  Job + PB   │
└─────────────┘               └────────┬─────────┘              └──────┬──────┘
                                       │                               │
              curl / CI / script ──────┘                               │ k8s module
                                                                       ▼
┌─────────────┐   apply ns/quota    ┌─────────────┐            ┌─────────────┐
│  Terraform  │───────────────────►│  Namespace  │◄───────────│  Kubernetes │
│  (trước)    │                     │ platform-   │  Deployment│  cluster    │
└─────────────┘                     │ apps        │            └─────────────┘
                                    └─────────────┘
```

## Vai trò từng lớp

| Lớp | Việc làm | Không làm |
|-----|----------|-----------|
| **Terraform** | Tạo namespace, quota, meta ConfigMap | Không build image / không rolling update app mỗi ngày |
| **Backstage** | UX: form + catalog + ownership | Không SSH vào cluster |
| **Python Bridge** | API ổn định, auth, map payload → AWX | Không chứa logic Ansible chi tiết |
| **AWX** | RBAC, audit, schedule, credentials | Không thay thế GitOps dài hạn (Argo CD) |
| **Ansible** | Apply Deployment/Service từ extra_vars | Không quản lý VPC/IAM (để Terraform) |

## Luồng tạo task (đúng nhu cầu của bạn)

1. Gọi API Bridge: `POST /api/v1/jobs` hoặc `POST /api/v1/deploy`
2. Bridge gọi AWX: `POST /api/v2/job_templates/{id}/launch/`
3. AWX chạy playbook `ansible/deploy-app.yml` với `extra_vars`
4. Playbook dùng `kubernetes.core.k8s` apply lên cluster

## Demo không cần cluster

`AWX_DEMO=true` (mặc định khi thiếu `AWX_URL`) → client đọc `data/awx_fixture.json`, vẫn luyện API/catalog.
