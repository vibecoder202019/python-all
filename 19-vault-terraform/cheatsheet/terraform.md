# Cheatsheet Terraform

terraform init          # Tai provider
terraform fmt -recursive  # Format HCL
terraform validate
terraform plan
terraform apply
terraform apply -auto-approve
terraform destroy
terraform show
terraform output
terraform output -json | jq

# Workspace
terraform workspace list|new|select

# Var
terraform apply -var="key=val"
export TF_VAR_environment=prod

# Target 1 resource
terraform apply -target=local_file.hello

# Import (resource da ton tai)
terraform import local_file.x /path/to/file

# State
terraform state list
terraform state show local_file.hello

# Module
module "x" {
  source = "./modules/x"
  arg    = var.y
}

# count / for_each
count    = length(var.list)
for_each = toset(var.list)

# Backend local (lab)
backend "local" { path = "../state/x.tfstate" }
