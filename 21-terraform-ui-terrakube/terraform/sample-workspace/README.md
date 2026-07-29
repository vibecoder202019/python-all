# Sample workspace — chạy trên Terrakube UI

Terraform tạo file JSON local — **không cần AWS**, phù hợp lab.

## Working directory (VCS)

```
21-terraform-ui-terrakube/terraform/sample-workspace
```

## Variables gợi ý trên UI

| Key | Value |
|-----|-------|
| environment | dev |
| app_name | terrakube-lab |

## Test local (trước khi đưa lên Terrakube)

```bash
cd 21-terraform-ui-terrakube/terraform/sample-workspace
terraform init && terraform plan
```

## Sau Apply trên Terrakube

Kiểm tra tab **States** — resource `local_file.app_config`.
