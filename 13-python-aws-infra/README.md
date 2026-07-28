# Module 13: Python & AWS — Tạo Infrastructure

Học dùng **boto3** (AWS SDK for Python) để quản lý và tạo infrastructure trên AWS — S3, EC2, VPC, IAM, CloudWatch.

## Mục tiêu

- Cấu hình AWS credentials an toàn
- Dùng boto3 client/session
- Tạo và quản lý S3, EC2, Security Group
- Inventory tài nguyên AWS bằng Python
- Hoàn thành CLI **AWS Infra Builder** qua 6 bước tuần tự

## Yêu cầu

- Python 3.10+
- Tài khoản AWS (Free Tier đủ cho học)
- AWS CLI hoặc credentials (`~/.aws/credentials`)

```bash
# Cấu hình credentials (chọn 1 cách)
aws configure
# hoặc export AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION
```

> **⚠️ Chi phí:** EC2/S3 có thể phát sinh phí. Module mặc định **dry-run** — chỉ tạo thật khi thêm flag `--apply`. Luôn chạy `destroy_infra.sh` sau khi học xong.

---

## Chạy nhanh

```bash
bash scripts/setup.sh                              # Cài boto3 (1 lần)
bash scripts/run_all_examples.sh                   # Ví dụ 01→06 tuần tự
bash scripts/run_project.sh                        # Dự án 6 bước (dry-run)
bash scripts/run_project.sh --apply                # Tạo infra thật trên AWS
bash scripts/destroy_infra.sh --apply              # Xóa tài nguyên đã tạo
```

---

## Lộ trình

| Bước | File | Nội dung | Level |
|------|------|----------|-------|
| 01 | `examples/01_boto3_basics.py` | Session, credentials, STS | Cơ bản |
| 02 | `examples/02_s3_operations.py` | S3 list, upload, bucket policy | Cơ bản |
| 03 | `examples/03_ec2_basics.py` | EC2 instances, regions, AMIs | Trung bình |
| 04 | `examples/04_iam_security.py` | IAM users, roles, least privilege | Trung bình |
| 05 | `examples/05_cloudwatch.py` | Metrics, alarms, log groups | Nâng cao |
| 06 | `examples/06_generate_template.py` | Generate CloudFormation YAML | Nâng cao |
| 🎯 | `project/` | **AWS Infra Builder CLI** (6 step) | Dự án |

---

## boto3 — Kiến trúc cơ bản

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Session   │ ──► │   Client    │ ──► │  AWS API    │
│ (credentials)│     │ (low-level) │     │  (S3, EC2)  │
└─────────────┘     └─────────────┘     └─────────────┘
                           │
                    ┌─────────────┐
                    │  Resource   │
                    │ (high-level)│
                    └─────────────┘
```

```python
import boto3

session = boto3.Session(region_name="ap-southeast-1")
s3 = session.client("s3")
ec2 = session.resource("ec2")

# Kiểm tra identity
sts = session.client("sts")
identity = sts.get_caller_identity()
print(identity["Arn"])
```

---

## Dự án tuần tự: AWS Infra Builder

Stack học tập gồm:

```
1. Verify AWS credentials
2. Inventory resources (EC2, S3, VPC)
3. Tạo S3 bucket (lưu artifacts)
4. Tạo Security Group (port 22, 80)
5. Launch EC2 t3.micro (Amazon Linux 2023)
6. CLI hoàn chỉnh + config YAML
```

Tất cả resources được tag: `Project=python-all-learn`

Config: `data/infra_config.yaml`

---

## Cấu trúc IAM tối thiểu ( học tập )

Policy cần cho module này:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {"Effect": "Allow", "Action": [
      "ec2:*", "s3:*", "iam:Get*", "iam:List*",
      "sts:GetCallerIdentity", "cloudwatch:*", "logs:*"
    ], "Resource": "*"}
  ]
}
```

> Production: dùng least privilege, không dùng `*` — module này dùng quyền rộng **chỉ cho môi trường lab**.

---

## Bash scripts

| Script | Mục đích |
|--------|---------|
| `setup.sh` | Cài boto3, tạo config mẫu |
| `run_all_examples.sh` | Chạy examples tuần tự |
| `run_project.sh` | Build infra 6 bước |
| `destroy_infra.sh` | Xóa resources có tag Project |
| `check_credentials.sh` | Kiểm tra AWS đã cấu hình chưa |

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module liên quan

- Trước: [Module 12 — DevOps](../12-python-devops-devsecops/README.md)
- Sau: [MLOps Labs — AWS EC2 deploy](../../labs/) (repo mlops)
