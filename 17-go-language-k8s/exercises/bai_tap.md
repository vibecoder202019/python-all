# Bài tập Module 17: Go + Kubernetes + Helm

## Bài 1 (Dễ): Struct và method
Thêm field `Priority int` vào struct `Task` và method `IsHighPriority() bool`.

## Bài 2 (Trung bình): API endpoint
Thêm `GET /tasks?done=true` lọc task theo trạng thái done.

## Bài 3 (Trung bình): Middleware
Viết middleware đếm tổng số request — expose qua `GET /metrics`.

## Bài 4 (Khó): Helm values
Thêm `values.yaml` option `ingress.tls.enabled` và template TLS secret.

## Bài 5 (Khó): Integration test
Viết test tạo → toggle → delete task qua httptest.

Đáp án: [exercises/solutions/solutions.go](exercises/solutions/solutions.go)
