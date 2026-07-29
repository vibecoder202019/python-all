# Lab 08 — Module Registry (Private)

**60 phút** | Advanced

## Mục tiêu

Hiểu publish module nội bộ — reuse code Terraform.

## Bước 1 — Module source

Code mẫu: `21-terraform-ui-terrakube/terraform/sample-module/`

Push lên Git repo riêng hoặc subdirectory trong fork.

## Bước 2 — Publish trên UI

1. **Registry** → **Modules** → **Publish**
2. Connect Git source module
3. Version tag: `1.0.0`

## Bước 3 — Consumer workspace

Tạo workspace mới dùng module (trong `main.tf` consumer):

```hcl
module "lab" {
  source      = "<registry-url-tu-UI>"
  environment = "dev"
  app_name    = "from-registry"
}
```

> URL registry lab thường: `terrakube-registry.platform.local` — copy từ UI Registry.

## Pass

- [ ] Module published
- [ ] Consumer plan thấy module source

Doc: [docs/05-state-registry-rbac.md](../../docs/05-state-registry-rbac.md)
