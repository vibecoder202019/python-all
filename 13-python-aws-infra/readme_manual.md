# Hướng dẫn chạy Manual — Module 13: Python & AWS Infra

> Lệnh trích từ `setup.sh`, `check_credentials.sh`, `run_all_examples.sh`, `run_project.sh`, `destroy_infra.sh`.

## Phần 0 — Kiểm tra credentials (`scripts/check_credentials.sh`)

```bash
aws --version
aws sts get-caller-identity
```

**Fallback (chỉ boto3):**

```bash
python3 -c "import boto3; print(boto3.client('sts').get_caller_identity())"
```

**Kỳ vọng:** JSON có `Account`, `Arn`.

---

## Phần A — Cài đặt (`scripts/setup.sh`)

```bash
cd learn-python-ai
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install boto3 pyyaml
mkdir -p 13-python-aws-infra/data
```

**Kiểm tra:**

```bash
python -c "import boto3, yaml; print('OK')"
test -f 13-python-aws-infra/data/infra_config.yaml || bash 13-python-aws-infra/scripts/setup.sh
```

---

## Phần B — Ví dụ (`scripts/run_all_examples.sh`)

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/examples/01_boto3_basics.py
python 13-python-aws-infra/examples/02_s3_operations.py
python 13-python-aws-infra/examples/03_ec2_basics.py
python 13-python-aws-infra/examples/04_iam_security.py
python 13-python-aws-infra/examples/05_cloudwatch.py
python 13-python-aws-infra/examples/06_generate_template.py
```

---

## Phần C — Dự án DRY-RUN (`scripts/run_project.sh`)

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

## Phần D — APPLY thật (tùy chọn, có phí)

```bash
python 13-python-aws-infra/project/step01_aws_connect.py --apply
# ... lặp step02–step06 với --apply
```

---

## Phần E — Xóa tài nguyên (`scripts/destroy_infra.sh`)

Dry-run:

```bash
cd learn-python-ai
source .venv/bin/activate
python 13-python-aws-infra/scripts/destroy_resources.py
```

Xóa thật:

```bash
python 13-python-aws-infra/scripts/destroy_resources.py --apply
```

**Kiểm tra:**

```bash
aws ec2 describe-instances --filters "Name=tag:Project,Values=python-all-learn" --query 'Reservations[].Instances[].State.Name'
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `check_credentials.sh` | 0 |
| `setup.sh` | A |
| `run_all_examples.sh` | B |
| `run_project.sh` | C / D |
| `destroy_infra.sh` | E |
