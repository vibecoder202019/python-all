# Backstage Software Template → AWX

## Ý tưởng

Developer không cần biết AWX URL. Họ chọn template **Provision / Deploy via AWX**, điền `app_name`, `image`, `replicas` → Scaffolder gọi Bridge → AWX tạo job.

## File trong module

| File | Vai trò |
|------|---------|
| `backstage/template.yaml` | Software Template |
| `backstage/catalog-info.yaml` | Component + API entity |
| `backstage/location.yaml` | Đăng ký vào Backstage |
| `backstage/skeletons/demo-service/` | Skeleton catalog cho app mới |

## Đăng ký Location (Backstage đã chạy)

Catalog → Create → Register Existing Component → URL tới `location.yaml` (Git raw hoặc file local plugin).

Hoặc `app-config.yaml`:

```yaml
catalog:
  locations:
    - type: file
      target: /path/to/28-python-backstage-awx-k8s/backstage/location.yaml
```

## Action HTTP

Template dùng `http:backstage:request` (cần plugin HTTP actions). Lab không có Backstage full: giả lập bằng:

```bash
curl -X POST http://127.0.0.1:8090/api/scaffolder/run \
  -H "Content-Type: application/json" \
  -H "X-API-Key: $BRIDGE_API_KEY" \
  -d '{"values":{"app_name":"from-bs","image":"nginx:1.27-alpine","replicas":2}}'
```

## Annotation gợi ý

`awx.io/job-template-id` trên Resource entity — portal link thẳng tới automation.
