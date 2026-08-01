# Hướng dẫn chạy Manual — Module 19: Vault + Terraform

> Copy từng lệnh và chạy **tuần tự**. Cần **2 terminal** cho Vault + Terraform.

## Điều kiện

- Terraform ≥ 1.6
- Vault CLI ≥ 1.15
- `jq` (khuyến nghị)

---

## Phần A — Kiểm tra tools (tương ứng `scripts/01-install-tools.sh --check`)

```bash
terraform --version
vault --version
jq --version
```

Cài trên macOS (nếu thiếu):

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform hashicorp/tap/vault jq
```

---

## Phần B — Vault dev server (tương ứng `scripts/02-setup-vault-dev.sh`)

**Terminal 1** — giữ chạy:

```bash
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
vault server -dev -dev-root-token-id=root -dev-listen-address=127.0.0.1:8200
```

**Terminal 2:**

```bash
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
vault status
vault secrets enable -path=secret kv-v2
cd learn-python-ai/19-vault-terraform
bash vault/scripts/seed-secrets.sh
vault kv get secret/myapp/db
```

---

## Phần C — Terraform lab 01 (tương ứng `scripts/03-run-terraform.sh 01-hello`)

```bash
cd learn-python-ai/19-vault-terraform/terraform/01-hello
terraform init -input=false
terraform fmt
terraform validate
terraform plan -input=false
terraform apply -input=false
terraform output
cat output/hello.txt
```

---

## Phần D — Terraform lab 02–04 (không cần Vault)

```bash
cd learn-python-ai/19-vault-terraform/terraform/02-variables
terraform init -input=false && terraform plan -input=false && terraform apply -input=false

cd ../03-local-resources
terraform init -input=false && terraform plan -input=false && terraform apply -input=false

cd ../04-modules
terraform init -input=false && terraform plan -input=false && terraform apply -input=false
```

---

## Phần E — Terraform + Vault (tương ứng `scripts/03-run-terraform.sh 05-vault-provider`)

> Vault phải đang chạy ở Terminal 1

```bash
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
cd learn-python-ai/19-vault-terraform/terraform/05-vault-provider
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
terraform output
```

---

## Phần F — Project Terraform (tương ứng `scripts/03-run-terraform.sh project`)

```bash
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
cd learn-python-ai/19-vault-terraform/terraform/project
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
```

---

## Phần G — Verify (tương ứng `scripts/04-verify-lab.sh`)

```bash
cd learn-python-ai/19-vault-terraform
bash scripts/04-verify-lab.sh 01
bash scripts/04-verify-lab.sh 07
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-install-tools.sh` | A |
| `02-setup-vault-dev.sh` | B |
| `03-run-terraform.sh 01-hello` | C |
| `03-run-terraform.sh 02/03/04` | D |
| `03-run-terraform.sh 05-vault-provider` | E |
| `03-run-terraform.sh project` | F |
| `04-verify-lab.sh` | G |

## Gỡ / dọn dẹp

```bash
cd learn-python-ai/19-vault-terraform/terraform/01-hello
terraform destroy -input=false -auto-approve
# Lặp cho từng thư mục terraform đã apply
# Ctrl+C Vault dev server ở Terminal 1
```
