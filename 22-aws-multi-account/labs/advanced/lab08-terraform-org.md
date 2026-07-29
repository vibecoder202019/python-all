# Lab 08 — Terraform Organizations

```bash
bash 22-aws-multi-account/scripts/04-terraform-plan.sh management
```

## Trước khi apply

- Organizations enabled
- Review plan: OU + SCP attachments

## Apply (tùy chọn)

```bash
cd terraform/environments/management
terraform apply
```

## Pass

Output `organization_id`, `sandbox_ou_id`
