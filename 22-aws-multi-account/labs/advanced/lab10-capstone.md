# Lab 10 — Capstone Landing Zone Mini

## Deliverable

| # | Console | Terraform |
|---|---------|-----------|
| 1 | Organizations + 2 OU | management/ apply OU+SCP |
| 2 | Dev account | tfvars dev_account_id |
| 3 | SSO user | (optional) |
| 4 | DevOpsCrossAccountRole | dev-workload/ module |
| 5 | SCP sandbox region | scp module |
| 6 | S3 cross-account | bucket policy |
| 7 | Document account IDs | notes/capstone.md |

## Rubric

Pass ≥ 6/7 — không commit terraform.tfvars thật.

## Cleanup

Xóa EC2/S3 lab, không xóa account member trừ khi chắc chắn.
