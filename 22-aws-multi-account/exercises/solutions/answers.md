# Đáp án gợi ý

## 1. Management vs Member
- Management: root org, billing, SCP, tạo account
- Member: workload tách biệt, assume role từ management/SSO

## 2. SCP vs IAM
- IAM grants permissions
- SCP sets maximum boundary (Deny wins); không grant thêm quyền

## 5. SCP test
- EC2 ngoài ap-southeast-1 → AccessDenied trên OU có scp-deny-regions

## 7–8. Terraform
- management: data org + OU + SCP
- dev-workload: provider assume_role + cross-account-role module
