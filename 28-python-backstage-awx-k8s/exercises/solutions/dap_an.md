# Đáp án gợi ý

1. `python3 project/run_launch.py --demo launch --template-id 7 --extra-vars '{"app_name":"bt1","replicas":1}'`
2. `curl -X POST http://127.0.0.1:8090/api/v1/jobs -H 'Content-Type: application/json' -H 'X-API-Key: dev-bridge-key-change-me' -d '{"template_id":7,"extra_vars":{"app_name":"bt2"}}'`
3. Terraform = drift-controlled infra chậm đổi; Ansible/AWX = thao tác app thường xuyên + audit.
4. Thêm object vào `job_templates` với `id` mới → chạy lại example 01.
5. `AWX_DEMO=false` + token; `run_launch.py launch --wait`.
