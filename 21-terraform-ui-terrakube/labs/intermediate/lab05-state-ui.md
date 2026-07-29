# Lab 05 — Xem State trên UI

**45 phút** | Sau lab 04 Apply thành công

## Bài tập

1. Workspace `local-files-demo` → tab **States**
2. Mở state version mới nhất
3. Tìm resource `local_file.app_config`
4. So sánh với `terraform show` local (Module 19):

```bash
cd 21-terraform-ui-terrakube/terraform/sample-workspace
terraform show   # chi local state — khac remote Terrakube
```

## Câu hỏi

1. Tại sao không commit `.tfstate` lên Git khi dùng Terrakube?
2. Ai có quyền xem state trong team?
3. Restore state nếu apply lỗi — tra docs Terrakube **State rollback**

## Pass

Giải thích được remote state vs local file state.
