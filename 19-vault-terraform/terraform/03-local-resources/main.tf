terraform {
  required_version = ">= 1.6"
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.4"
    }
  }
}

provider "local" {}

variable "users" {
  type    = list(string)
  default = ["alice", "bob", "charlie"]
}

# count — tao file theo index
resource "local_file" "user_count" {
  count    = length(var.users)
  filename = "${path.module}/output/count-${count.index}-${var.users[count.index]}.txt"
  content  = "User #${count.index}: ${var.users[count.index]}"
}

# for_each — tao file theo key (on dinh hon khi xoa phan tu giua list)
resource "local_file" "user_foreach" {
  for_each = toset(var.users)
  filename = "${path.module}/output/fe-${each.key}.txt"
  content  = "Hello, ${each.key}!"
}

output "user_files" {
  value = [for f in local_file.user_foreach : f.filename]
}
