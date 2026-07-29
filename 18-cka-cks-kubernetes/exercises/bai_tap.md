# Bài tập Module 18 — CKA/CKS

## CKA
1. (Dễ) Tạo pod nginx namespace `cka-lab` chỉ bằng 1 lệnh kubectl.
2. (Trung bình) Scale deployment lên 4 replicas, update image, rollback 1 revision.
3. (Trung bình) PVC 1Gi + pod mount `/data`.
4. (Khó) Role + RoleBinding: SA chỉ được list/get pods.
5. (Khó) Sửa 4 broken pods lab 09 trong ≤ 30 phút.

## CKS
6. Namespace enforce PSS `restricted`, deploy pod compliant.
7. NetworkPolicy: deny all + allow frontend→backend:8080.
8. Viết audit policy log mọi delete Secret.
9. Giải thích seccomp `RuntimeDefault` vs `Unconfined`.
10. (Mock) Hoàn thành lab 14 trong 120 phút.

Đáp án: [exercises/solutions/mock-exam-answers.sh](exercises/solutions/mock-exam-answers.sh)
