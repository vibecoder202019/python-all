# Hướng dẫn chạy Manual — Module 19: Vault + Terraform

> Lệnh trích từ `01-install-tools.sh`, `02-setup-vault-dev.sh`, `03-run-terraform.sh`, `04-verify-lab.sh`.

## Phần A — Cài đặt tools (`scripts/01-install-tools.sh --check`)

```bash
terraform --version
vault --version
jq --version
```

**Cài macOS (`--install`):**

```bash
brew tap hashicorp/tap
brew install hashicorp/tap/terraform hashicorp/tap/vault jq
```

---

## Phần B — Vault dev (`scripts/02-setup-vault-dev.sh`)

**Terminal 1:**

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
bash learn-python-ai/19-vault-terraform/vault/scripts/seed-secrets.sh
vault kv get secret/myapp/db
```

**Kiểm tra:**

```bash
vault status | grep Sealed
```

**Kỳ vọng:** `Sealed false`.

---

## Phần C — Terraform lab 01 (`scripts/03-run-terraform.sh 01-hello`)

```bash
mkdir -p learn-python-ai/19-vault-terraform/terraform/01-hello/output
cd learn-python-ai/19-vault-terraform/terraform/01-hello
terraform init -input=false
terraform fmt
terraform validate
terraform plan -input=false
terraform apply -input=false
terraform output
```

**Kiểm tra:**

```bash
cat output/hello.txt
bash learn-python-ai/19-vault-terraform/scripts/04-verify-lab.sh 01
```

---

## Phần D — Lab 02–04

```bash
cd learn-python-ai/19-vault-terraform/terraform/02-variables
terraform init -input=false && terraform apply -input=false

cd ../03-local-resources
terraform init -input=false && terraform apply -input=false

cd ../04-modules
terraform init -input=false && terraform apply -input=false
```

---

## Phần E — Lab Vault provider (cần Vault chạy)

```bash
export VAULT_ADDR=http://127.0.0.1:8200
export VAULT_TOKEN=root
bash learn-python-ai/19-vault-terraform/vault/scripts/seed-secrets.sh
cd learn-python-ai/19-vault-terraform/terraform/05-vault-provider
terraform init -input=false
terraform plan -input=false
terraform apply -input=false
bash learn-python-ai/19-vault-terraform/scripts/04-verify-lab.sh 07
```

---

## Bản đồ script ↔ manual

| Script | Phần |
|--------|------|
| `01-install-tools.sh` | A |
| `02-setup-vault-dev.sh` | B |
| `03-run-terraform.sh` | C–E |
| `04-verify-lab.sh` | Kiểm tra sau mỗi lab |

## Teardown

```bash
cd learn-python-ai/19-vault-terraform/terraform/01-hello
terraform destroy -input=false -auto-approve
```
