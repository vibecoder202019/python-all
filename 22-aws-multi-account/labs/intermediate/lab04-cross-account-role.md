# Lab 04 — Cross-Account Role (Console)

Trong **Dev account** (Switch role OrganizationAccountAccessRole):

1. IAM → Role → Create `DevOpsCrossAccountRole`
2. Trust: Management account ID + ExternalId `lab-module-22-dev`
3. Attach inline policy từ `policies/devops-scoped.json`

## Pass

Role trust policy khớp `policies/trust-devops-role.json` (thay MANAGEMENT_ACCOUNT_ID).
