# Lab 04 — Workspace + Plan/Apply

**90 phút**

## Cách A — VCS (GitHub, khuyến nghị)

1. Fork repo `python-all`
2. Workspace → Create trong project `demo-infra`
3. Name: `local-files-demo`
4. VCS: repo fork, branch `main`
5. **Working directory:**
   ```
   21-terraform-ui-terrakube/terraform/sample-workspace
   ```

## Cách B — Không VCS (upload / CLI)

Nếu chưa kết nối GitHub: tạo workspace **CLI-driven** hoặc upload theo UI version hiện tại — tham khảo [Terrakube docs Workspace](https://docs.terrakube.io/).

Hoặc test code local trước:

```bash
cd 21-terraform-ui-terrakube/terraform/sample-workspace
terraform init && terraform plan
```

## Variables trên UI

| Key | Value |
|-----|-------|
| environment | dev |
| app_name | terrakube-lab |

## Chạy Run

1. **Queue Plan** / **Plan**
2. Đọc log — tìm `Plan: 1 to add`
3. **Confirm Apply**
4. Run status: **Applied**

## Verify

- [ ] Run completed without error
- [ ] Output có `config_file`
- [ ] Tab States có resource `local_file`

```bash
bash 21-terraform-ui-terrakube/scripts/08-verify-lab.sh 04
```

Doc: [docs/03-workspace-va-run.md](../../docs/03-workspace-va-run.md)
