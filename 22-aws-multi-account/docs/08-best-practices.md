# Best Practices — AWS Multi-Account

## Account strategy

- [ ] **Management** — không deploy app prod
- [ ] **Separate prod/nonprod** accounts
- [ ] **Audit/Log** account — immutable logs
- [ ] Email root member account → break-glass vault

## Identity

- [ ] **IAM Identity Center** thay IAM user dài hạn
- [ ] MFA bắt buộc
- [ ] Permission sets theo job function
- [ ] Không dùng `OrganizationAccountAccessRole` hàng ngày

## SCP

- [ ] Deny `organizations:LeaveOrganization` on Root
- [ ] Deny region không dùng
- [ ] Test SCP trên OU Sandbox trước
- [ ] Document mọi SCP attachment

## Terraform

- [ ] Remote state S3 + DynamoDB lock (Module 19/21)
- [ ] `terraform.tfvars` trong `.gitignore`
- [ ] Separate state per account/environment
- [ ] `prevent_destroy` on `aws_organizations_account`

## Secrets

- [ ] Vault (Module 19) cho external IDs / API keys
- [ ] Không hardcode account IDs trong public repo — dùng tfvars

## Liên kết AWS

- [AWS Multi-Account Strategy](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/)
- [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
