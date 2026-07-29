# AWS Multi-Account cheatsheet

# Identity
aws sts get-caller-identity
aws organizations describe-organization
aws organizations list-accounts

# Switch role CLI
aws sts assume-role --role-arn arn:aws:iam::DEV:role/ROLE --role-session-name s

# Terraform assume_role provider
assume_role { role_arn = "..." session_name = "tf" }

# Key ARNs
OrganizationAccountAccessRole  # break-glass member account
DevOpsCrossAccountRole         # lab custom role

# SCP
Effective = IAM AND SCP
Test SCP on Sandbox OU first

# Files
policies/trust-devops-role.json
terraform/environments/management
terraform/environments/dev-workload
