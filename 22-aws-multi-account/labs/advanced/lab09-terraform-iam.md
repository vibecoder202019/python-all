# Lab 09 — Terraform Cross-Account IAM

```bash
cd 22-aws-multi-account/terraform/environments/dev-workload
cp terraform.tfvars.example terraform.tfvars
# Điền management_account_id, dev_account_id
bash ../../../scripts/04-terraform-plan.sh dev-workload
```

## Apply

Tạo `DevOpsCrossAccountRole` + bucket S3 lab trong dev account.

## Verify

```bash
export DEV_ACCOUNT_ID=<dev-id>
bash ../../../scripts/03-assume-role-demo.sh
```

So sánh role Terraform vs Console lab 04.
