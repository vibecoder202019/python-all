# HashiCorp Vault cơ bản

## Vault là gì?

**Vault** = hệ thống quản lý **secrets** tập trung: password, API key, certificate, SSH key.

**Ví von:** Vault như **két sắt ngân hàng** — app không giữ chìa khóa gốc, chỉ xin quyền truy cập có thời hạn (token).

---

## Kiến trúc đơn giản

```
┌──────────┐     token/API      ┌─────────────┐
│   App    │ ─────────────────▶ │ Vault Server│
│ (Terraform│                   │  ┌─────────┐│
│  CI/CD)  │ ◀── secret ────────│  │ Secrets ││
└──────────┘                    │  │ Engine  ││
                                │  └─────────┘│
                                │  Policies   │
                                └─────────────┘
```

| Thành phần | Vai trò |
|------------|---------|
| **Seal/Unseal** | Vault mã hóa data — cần unseal key (prod) |
| **Auth method** | Xác thực: token, AppRole, K8s, LDAP... |
| **Secrets engine** | KV, Database, PKI, AWS... |
| **Policy** | ACL — path nào được read/write |

---

## Dev mode vs Production

| | Dev mode | Production |
|---|----------|------------|
| Lệnh | `vault server -dev` | `vault server -config=config.hcl` |
| Storage | In-memory | Consul, Raft, file |
| Unseal | Tự động | Shamir keys / auto-unseal |
| Root token | In ra console | Rotate ngay sau init |
| Dùng cho | **Lab, học** | Staging, Prod |

```bash
# Dev mode — CHỈ lab
vault server -dev -dev-root-token-id=root
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='root'
```

---

## KV Secrets Engine v2

```bash
# Enable KV v2 tại path secret/ (script lab đã enable)
vault secrets enable -path=secret kv-v2

# Ghi secret
vault kv put secret/myapp/db \
  username=admin \
  password=s3cr3t

# Đọc secret
vault kv get secret/myapp/db

# Chỉ lấy password
vault kv get -field=password secret/myapp/db

# Versioning — KV v2 lưu lịch sử
vault kv put secret/myapp/db password=newpass-v2
vault kv get -version=1 secret/myapp/db
```

**API path:** CLI `secret/myapp/db` → API `secret/data/myapp/db`

---

## Policy cơ bản

File HCL định nghĩa quyền:

```hcl
# vault/policies/readonly-kv.hcl
path "secret/data/myapp/*" {
  capabilities = ["read", "list"]
}

path "secret/metadata/myapp/*" {
  capabilities = ["list"]
}
```

```bash
# Nạp policy
vault policy write readonly-kv vault/policies/readonly-kv.hcl

# Tạo token gắn policy
vault token create -policy=readonly-kv -ttl=1h

# Test với token mới
export VAULT_TOKEN=<token-id>
vault kv get secret/myapp/db   # OK
vault kv put secret/myapp/db x=1  # Permission denied
```

---

## Token lifecycle

```bash
vault token lookup          # Thông tin token hiện tại
vault token renew           # Gia hạn (nếu renewable)
vault token revoke <token>  # Thu hồi
```

**Least privilege:** App dùng token/policy riêng — **không** dùng root token.

---

## Vault CLI hay dùng

```bash
vault status
vault secrets list
vault policy list
vault auth list
vault kv list secret/
```

---

## Lab module

- [lab07-vault-kv.md](../labs/basic/lab07-vault-kv.md)
- [lab08-vault-policies.md](../labs/intermediate/lab08-vault-policies.md)
- Policies mẫu: `vault/policies/`

**Tiếp theo:** [05-vault-nang-cao.md](05-vault-nang-cao.md)
