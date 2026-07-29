variable "policy_name" {
  type = string
}

variable "policy_file" {
  type = string
}

variable "target_id" {
  type = string
}

resource "aws_organizations_policy" "this" {
  name    = var.policy_name
  type    = "SERVICE_CONTROL_POLICY"
  content = file(var.policy_file)
}

resource "aws_organizations_policy_attachment" "this" {
  policy_id = aws_organizations_policy.this.id
  target_id = var.target_id
}

output "policy_id" {
  value = aws_organizations_policy.this.id
}
