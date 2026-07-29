variable "name" {
  type = string
}

variable "parent_id" {
  type = string
}

resource "aws_organizations_organizational_unit" "this" {
  name      = var.name
  parent_id = var.parent_id
}

output "ou_id" {
  value = aws_organizations_organizational_unit.this.id
}

output "ou_arn" {
  value = aws_organizations_organizational_unit.this.arn
}
