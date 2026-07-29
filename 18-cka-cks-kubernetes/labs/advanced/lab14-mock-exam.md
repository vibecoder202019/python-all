# Lab 14 — Mock Exam (Advanced | CKA + CKS)

**Thời gian:** 120 phút | **Giới hạn:** Không xem đáp án, mở kubernetes.io/docs được phép

## Quy tắc

- Timer 120 phút
- Namespace: `exam-mock`
- Ghi điểm: mỗi task 1 điểm, cần ≥ 12/17 đậu mock CKA

## Tasks

### CKA Section (100 phút)

1. Tạo namespace `exam-mock`
2. Deployment `web` — nginx:1.25, 3 replicas, label app=web
3. Service ClusterIP `web-svc` port 80
4. Ingress `web.local` → web-svc
5. ConfigMap `app-cfg` key `ENV=exam`, mount vào pod `cfg-pod`
6. Secret `db-pass` key `password=secret`, env trong deployment `web`
7. PVC `data` 500Mi, pod `writer` mount `/data`, ghi file `done.txt`
8. Scale `web` lên 5 replicas
9. Role `pod-lister` + bind SA `exam-sa` — list pods only
10. Pod `fixed` từ broken YAML (image sai) — sửa cho Running
11. Node label `env=exam`, pod `special` schedule node đó (nodeSelector)
12. `kubectl top pod` (metrics-server) — ghi CPU pod web

### CKS Section (20 phút)

13. Label namespace enforce `baseline` PSS
14. NetworkPolicy deny-all + allow ingress nginx port 80 only
15. Pod securityContext: non-root, drop ALL capabilities

<details>
<summary>Đáp án gợi ý</summary>

Xem `exercises/solutions/mock-exam-answers.sh`
</details>

## Sau mock

- Ghi lại task mất > 10 phút
- Ôn lại domain yếu nhất
