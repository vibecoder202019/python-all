# Hướng dẫn chạy Manual — Module 13: Python & AWS Infra

> Copy từng lệnh và chạy **tuần tự**. **Cẩn thận:** bước `--apply` tạo tài nguyên AWS thật (có phí).

## Điều kiện

- AWS account + credentials (`aws configure` hoặc env vars)
- Python 3.10+, AWS CLI v2

---

## Phần A — Kiểm tra credentials (tương ứng `scripts/check_credentials.sh`)

```bash
aws sts get-caller-identity
```

```bash
python3 -c "import boto3; print(boto3.client('sts').get_caller_identity())"
```

---

## Phần B — Setup (tương ứng `scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install boto3 pyyaml
```

---

## Phần C — Ví dụ (tương ứng `scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/examples/01_boto3_basics.py
python 13-python-aws-infra/examples/02_s3_operations.py
python 13-python-aws-infra/examples/03_ec2_basics.py
python 13-python-aws-infra/examples/04_iam_basics.py
python 13-python-aws-infra/examples/05_cloudwatch.py
python 13-python-aws-infra/examples/06_generate_template.py
```

---

## Phần D — Dự án 6 bước DRY-RUN (tương ứng `scripts/run_project.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/project/step01_aws_connect.py --demo
python 13-python-aws-infra/project/step02_list_resources.py --demo
python 13-python-aws-infra/project/step03_create_s3.py --demo
python 13-python-aws-infra/project/step04_security_group.py --demo
python 13-python-aws-infra/project/step05_ec2_instance.py --demo
python 13-python-aws-infra/project/step06_final.py --demo
```

---

## Phần E — Tạo tài nguyên thật (tùy chọn, `--apply`)

> Chỉ chạy khi hiểu chi phí. Tương ứng `scripts/run_project.sh --apply`

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/project/step01_aws_connect.py --apply
python 13-python-aws-infra/project/step02_list_resources.py --apply
python 13-python-aws-infra/project/step03_create_s3.py --apply
python 13-python-aws-infra/project/step04_security_group.py --apply
python 13-python-aws-infra/project/step05_ec2_instance.py --apply
python 13-python-aws-infra/project/step06_final.py --apply
```

---

## Phần F — Xóa tài nguyên (tương ứng `scripts/destroy_infra.sh`)

Dry-run trước:

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/scripts/destroy_resources.py
```

Xóa thật:

```bash
python 13-python-aws-infra/scripts/destroy_resources.py --apply
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `check_credentials.sh` | A |
| `setup.sh` | B |
| `run_all_examples.sh` | C |
| `run_project.sh` | D (dry-run) / E (`--apply`) |
| `destroy_infra.sh` | F |

## Biến môi trường (tùy chọn)

```bash
export AWS_DEFAULT_REGION=ap-southeast-1
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
```
