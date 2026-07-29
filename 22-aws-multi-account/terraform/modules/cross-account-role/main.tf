terraform {
  required_providers {
    aws = {
      source                = "hashicorp/aws"
      configuration_aliases = [aws]
    }
  }
}

variable "role_name" {
  type = string
}

variable "management_account_id" {
  type = string
}

variable "external_id" {
  type    = string
  default = ""
}

variable "policy_json" {
  type = string
}

resource "aws_iam_role" "this" {
  provider = aws
  name     = var.role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = {
        AWS = "arn:aws:iam::${var.management_account_id}:root"
      }
      Action = "sts:AssumeRole"
      Condition = var.external_id != "" ? {
        StringEquals = {
          "sts:ExternalId" = var.external_id
        }
      } : null
    }]
  })
}

resource "aws_iam_role_policy" "inline" {
  provider = aws
  name     = "${var.role_name}-policy"
  role     = aws_iam_role.this.id
  policy   = var.policy_json
}

output "role_arn" {
  value = aws_iam_role.this.arn
}

output "role_name" {
  value = aws_iam_role.this.name
}
