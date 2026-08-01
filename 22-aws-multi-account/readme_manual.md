# Hướng dẫn chạy Manual — Module 22: AWS Multi-Account

> Copy từng lệnh và chạy **tuần tự**. **Cẩn thận:** Terraform apply tạo tài nguyên AWS Organizations thật.

## Điều kiện

- AWS account (admin/root lần đầu bật Organizations)
- AWS CLI v2, Terraform ≥ 1.6, `jq`
- Module 13, 19 (khuyến nghị)

---

## Phần A — Kiểm tra (tương ứng `scripts/01-check-prerequisites.sh`)

```bash
aws --version
terraform --version
jq --version
aws sts get-caller-identity
```

---

## Phần B — Verify Organizations (tương ứng `scripts/05-verify-org.sh`)

```bash
aws organizations describe-organization
aws organizations list-accounts --output table
```

---

## Phần C — Lab Console (tương ứng `scripts/02-run-lab.sh`)

Lab 01 — bật Organizations:

```bash
cd learn-python-ai/22-aws-multi-account
cat labs/basic/lab01-enable-organizations.md
```

Làm theo từng bước trong AWS Console (checklist trong `console/`).

Lab khác:

```bash
cat labs/basic/lab03-create-member-account.md
cat labs/intermediate/lab06-scp-deny-root.md
cat labs/advanced/lab09-terraform-modules.md
```

---

## Phần D — Assume role demo (tương ứng `scripts/03-assume-role-demo.sh`)

```bash
export DEV_ACCOUNT_ID=123456789012
export ROLE_NAME=DevOpsCrossAccountRole
export EXTERNAL_ID=lab-module-22-dev
aws sts assume-role \
  --role-arn "arn:aws:iam::${DEV_ACCOUNT_ID}:role/${ROLE_NAME}" \
  --role-session-name module22-lab \
  --external-id "$EXTERNAL_ID" \
  --output json
```

Export credentials từ output (AccessKeyId, SecretAccessKey, SessionToken):

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
aws sts get-caller-identity
aws s3 ls
```

---

## Phần E — Terraform plan (tương ứng `scripts/04-terraform-plan.sh`)

Management account:

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/management
cp terraform.tfvars.example terraform.tfvars
terraform init -input=false
terraform fmt
terraform validate
terraform plan -input=false
```

Apply (chỉ khi đã hiểu chi phí):

```bash
terraform apply -input=false
```

Dev workload environment:

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/dev-workload
cp terraform.tfvars.example terraform.tfvars
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
```

---

## Phần F — Mở lab bằng script

```bash
cd learn-python-ai/22-aws-multi-account
bash scripts/02-run-lab.sh 01
bash scripts/02-run-lab.sh 05
bash scripts/04-terraform-plan.sh management
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `05-verify-org.sh` | B |
| `02-run-lab.sh` | C, F |
| `03-assume-role-demo.sh` | D |
| `04-terraform-plan.sh` | E |

## Biến môi trường

```bash
export AWS_DEFAULT_REGION=ap-southeast-1
export DEV_ACCOUNT_ID=YOUR_DEV_ACCOUNT_ID
export ROLE_NAME=DevOpsCrossAccountRole
export EXTERNAL_ID=lab-module-22-dev
```

## Gỡ / dọn dẹp

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/dev-workload
terraform destroy -input=false
cd ../management
terraform destroy -input=false
```
