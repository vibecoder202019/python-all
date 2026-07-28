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

---

## Giải thích chi tiết (Tự học)

### Cấu hình AWS credentials

```bash
aws configure
# AWS Access Key ID: AKIA...
# AWS Secret Access Key: ...
# Default region: ap-southeast-1
```

Lưu vào `~/.aws/credentials` và `~/.aws/config`. boto3 **tự đọc** file này.

Hoặc biến môi trường:
```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=ap-southeast-1
```

---

### boto3 — Client vs Resource

```python
session = boto3.Session(region_name="ap-southeast-1")
s3_client = session.client("s3")      # Low-level — dict response
s3_resource = session.resource("s3")  # High-level — object oriented

sts.get_caller_identity()  # Kiểm tra đang dùng account/role nào
```

**Luôn gọi STS trước** khi deploy — tránh nhầm account production.

---

### File `examples/02_s3_operations.py`

```python
s3.put_object(Bucket=bucket, Key=key, Body=content.encode())
s3.head_object(Bucket=bucket, Key=key)   # Metadata, không tải body
s3.delete_object(Bucket=bucket, Key=key)
```

- **Bucket name** globally unique trên toàn AWS
- Region `ap-southeast-1` (Singapore) — gần VN, latency thấp

---

### File `examples/03_ec2_basics.py`

```python
ec2.describe_instances(Filters=[{"Name": "instance-state-name", "Values": ["running"]}])
ec2.describe_images(Owners=["amazon"], Filters=[{"Name": "name", "Values": ["al2023-*"]}])
```

- **AMI** — template OS + software để launch instance
- `t3.micro` — Free Tier eligible (750 giờ/tháng năm đầu)

---

### Dry-run vs Apply

```python
def dry_run_message(action, details, apply):
    prefix = "🔧 APPLY" if apply else "🔍 DRY-RUN"
```

| Mode | Hành vi |
|------|---------|
| Mặc định / `--demo` | Chỉ **in** kế hoạch, không gọi AWS API tạo resource |
| `--apply` | Gọi API thật — **tốn tiền**, cần xác nhận |

```bash
bash scripts/run_project.sh          # Dry-run an toàn
bash scripts/run_project.sh --apply    # Tạo thật — script hỏi gõ 'yes'
bash scripts/destroy_infra.sh --apply  # Xóa resources tag Project=python-all-learn
```

---

### Dự án AWS Infra — từng step

**`step03_create_s3.py`:**
```python
s3.create_bucket(Bucket=name, CreateBucketConfiguration={"LocationConstraint": region})
s3.put_bucket_tagging(Bucket=name, Tagging={"TagSet": default_tags()})
s3.put_bucket_versioning(..., VersioningConfiguration={"Status": "Enabled"})
```
- Versioning — giữ lại mọi phiên bản object (phục hồi khi xóa nhầm)

**`step04_security_group.py`:**
```python
ec2.create_security_group(GroupName=..., VpcId=vpc_id)
ec2.authorize_security_group_ingress(GroupId=sg_id, IpPermissions=[...])
```
- SG = firewall ảo — chỉ mở port cần thiết
- ⚠️ `0.0.0.0/0` cho SSH chỉ dùng lab — production restrict IP

**`step05_ec2_instance.py`:**
```python
ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t3.micro",
    SecurityGroupIds=[sg_id],
    UserData=user_data_script,   # Script chạy lần đầu boot
    TagSpecifications=[...],
)
waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])
```
- **UserData** — bash script cloud-init khi instance khởi động
- **Waiter** — poll đến khi state = running (tránh connect quá sớm)

**`step06_final.py`:**
```python
python project/step06_final.py status    # Xem infra hiện tại
python project/step06_final.py deploy --apply
python project/step06_final.py destroy --apply
```

---

### Script `destroy_resources.py`

```python
ec2.describe_instances(Filters=[{"Name": f"tag:{PROJECT_TAG_KEY}", "Values": [PROJECT_TAG_VALUE]}])
ec2.terminate_instances(InstanceIds=instance_ids)
```

- Chỉ xóa resource có tag `Project=python-all-learn` — an toàn hơn xóa all
- Thứ tự: EC2 → Security Group → S3 (SG phải xóa sau khi instance terminate)

---

## Bài tập

→ [exercises/bai_tap.md](exercises/bai_tap.md)

## Module liên quan

- Trước: [Module 12 — DevOps](../12-python-devops-devsecops/README.md)
- Sau: [MLOps Labs — AWS EC2 deploy](../../labs/) (repo mlops)
