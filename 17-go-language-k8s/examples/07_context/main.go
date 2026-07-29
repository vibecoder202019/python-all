// Ví dụ 07 — Context (timeout, cancellation — advanced)
// Chạy: go run examples/07_context/main.go
package main

import (
	"context"
	"fmt"
	"time"
)

// slowOperation — giả lập API call chậm
func slowOperation(ctx context.Context, name string) (string, error) {
	select {
	case <-time.After(2 * time.Second):
		return fmt.Sprintf("Kết quả của %s", name), nil
	case <-ctx.Done():
		// ctx.Done() — channel đóng khi timeout hoặc cancel
		return "", ctx.Err()
	}
}

func main() {
	fmt.Println("=== Context với timeout ===")

	// context.WithTimeout — tự cancel sau duration
	ctx, cancel := context.WithTimeout(context.Background(), 500*time.Millisecond)
	defer cancel() // luôn gọi cancel để giải phóng resource

	result, err := slowOperation(ctx, "fetch-users")
	if err != nil {
		fmt.Printf("  ❌ Lỗi: %v\n", err) // context deadline exceeded
	} else {
		fmt.Printf("  ✅ %s\n", result)
	}

	fmt.Println("\n=== Context với deadline đủ dài ===")
	ctx2, cancel2 := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel2()

	result2, err2 := slowOperation(ctx2, "fetch-tasks")
	if err2 != nil {
		fmt.Printf("  ❌ %v\n", err2)
	} else {
		fmt.Printf("  ✅ %s\n", result2)
	}
}
