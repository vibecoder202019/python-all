# AWX CLI cheatsheet (Module 15)

export AWX_HOST=http://localhost:8052
export AWX_TOKEN=xxx
export AWX_VERIFY_SSL=false

awx ping
awx me
awx job_templates list
awx projects list
awx inventories list
awx jobs list --order_by -created

awx projects sync --name "python-demo-playbooks" --wait
awx job_templates launch "TEMPLATE" --monitor
awx job_templates launch 7 --extra_vars '{"k":"v"}' --monitor
awx jobs stdout 42 --follow

# Config file: ~/.awx/credentials
# Terraform: terraform/awx-client/ + scripts/07-terraform-awx-client.sh
