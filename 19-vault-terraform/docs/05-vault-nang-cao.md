# HashiCorp Vault nâng cao

## AppRole — Auth cho ứng dụng / CI

AppRole = username/password cho machine — Role ID + Secret ID → token.

```bash
# Enable AppRole
vault auth enable approle

# Tạo role gắn policy
vault write auth/approle/role/myapp \
  token_policies="readonly-kv" \
  token_ttl=1h \
  token_max_ttl=4h

# Lấy Role ID
vault read auth/approle/role/myapp/role-id

# Tạo Secret ID (một lần, bảo mật)
vault write -f auth/approle/role/myapp/secret-id

# Login lấy token
vault write auth/approle/login \
  role_id="<role-id>" \
  secret_id="<secret-id>"
```

**Use case:** Jenkins, GitHub Actions, Terraform trong CI — không embed root token.

Script lab: `vault/scripts/setup-approle.sh`

---

## Dynamic Secrets (Database engine — concept)

Thay vì lưu password DB tĩnh, Vault **tạo user tạm** khi app yêu cầu:

```
App ──▶ Vault ──▶ CREATE USER temp_xxx PASSWORD yyy TTL 1h ──▶ PostgreSQL
         │
         └──▶ Trả creds cho app
```

Lab mock (không cần Postgres thật): [lab10-dynamic-secrets.md](../labs/advanced/lab10-dynamic-secrets.md)

Production setup:

```bash
vault secrets enable database
vault write config/postgresql \
  plugin_name=postgresql-database-plugin \
  allowed_roles="readonly" \
  connection_url="postgresql://{{username}}:{{password}}@localhost:5432/mydb" \
  username="vault_admin" \
  password="adminpass"
```

---

## Audit Log

Ghi mọi request tới Vault — compliance, forensics:

```hcl
# vault/config/audit-file.hcl (production)
audit {
  type = "file"
  options = {
    file_path = "/vault/logs/audit.log"
  }
}
```

Dev mode không bật audit file — xem concept trong doc.

---

## PKI Engine (tóm tắt)

Vault làm **Certificate Authority** nội bộ — cấp TLS cert ngắn hạn:

```bash
vault secrets enable pki
vault write pki/root/generate/internal \
  common_name="lab.internal" ttl=8760h
```

CKS/DevSecOps: thay cert 1 năm bằng cert 24h rotate tự động.

---

## Vault trên Kubernetes (overview)

```bash
# Helm install Vault (production HA — đọc thêm HashiCorp docs)
helm repo add hashicorp https://helm.releases.hashicorp.com
helm install vault hashicorp/vault -n vault --create-namespace
```

**Injector:** Pod annotate để sidecar tự lấy secret — liên kết Module 15–18.

---

## High Availability (Raft)

Vault OSS hỗ trợ **Integrated Storage (Raft)** — 3+ node cluster, leader election.

Lab module dùng single-node Docker — đủ học concept; HA deploy xem [Vault production docs](https://developer.hashicorp.com/vault/tutorials/kubernetes/kubernetes-raft-deployment-guide).

---

## Security checklist

- [ ] Tắt/xóa root token sau init (prod)
- [ ] Enable audit
- [ ] TLS cho `VAULT_ADDR` (https)
- [ ] Policy least-privilege per app
- [ ] Rotate Secret ID định kỳ
- [ ] Không commit token vào Git

**Tiếp theo:** [06-vault-terraform-tich-hop.md](06-vault-terraform-tich-hop.md)
