# Hướng dẫn chạy Manual — Module 22: AWS Multi-Account

> Lệnh trích từ `01-check-prerequisites.sh`, `05-verify-org.sh`, `03-assume-role-demo.sh`, `04-terraform-plan.sh`.

## Phần A — Kiểm tra (`scripts/01-check-prerequisites.sh`)

```bash
command -v aws
command -v terraform
command -v jq
aws sts get-caller-identity
terraform --version
jq --version
```

---

## Phần B — Verify Organizations (`scripts/05-verify-org.sh`)

```bash
aws organizations describe-organization
aws organizations list-accounts --output table
```

---

## Phần C — Lab Console (`scripts/02-run-lab.sh`)

```bash
find learn-python-ai/22-aws-multi-account/labs -name "lab01-*.md"
cat learn-python-ai/22-aws-multi-account/labs/basic/lab01-enable-organizations.md
```

---

## Phần D — Assume role (`scripts/03-assume-role-demo.sh`)

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

Export credentials từ output:

```bash
export AWS_ACCESS_KEY_ID=...
export AWS_SECRET_ACCESS_KEY=...
export AWS_SESSION_TOKEN=...
aws sts get-caller-identity
aws s3 ls | head -5
unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
```

---

## Phần E — Terraform (`scripts/04-terraform-plan.sh`)

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/management
cp terraform.tfvars.example terraform.tfvars
terraform init -input=false
terraform fmt
terraform validate
terraform plan -input=false
```

Dev workload:

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/dev-workload
cp terraform.tfvars.example terraform.tfvars
terraform init -input=false
terraform plan -input=false
```

**Apply (cẩn thận — tài nguyên thật):**

```bash
terraform apply -input=false
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-check-prerequisites.sh` | A |
| `05-verify-org.sh` | B |
| `02-run-lab.sh` | C |
| `03-assume-role-demo.sh` | D |
| `04-terraform-plan.sh` | E |

## Teardown

```bash
cd learn-python-ai/22-aws-multi-account/terraform/environments/dev-workload
terraform destroy -input=false
```
