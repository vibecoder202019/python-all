// Ví dụ 03 — Functions, struct, methods
// Chạy: go run examples/03_functions_structs/main.go
package main

import (
	"fmt"
	"strings"
)

// Task — struct định nghĩa kiểu dữ liệu (giống class data-only)
type Task struct {
	ID    int
	Title string
	Done  bool
}

// String — method gắn vào Task (receiver (t Task))
func (t Task) String() string {
	status := "pending"
	if t.Done {
		status = "done"
	}
	return fmt.Sprintf("[%d] %s (%s)", t.ID, t.Title, status)
}

// markDone — pointer receiver (*Task) — cho phép sửa struct gốc
func (t *Task) markDone() {
	t.Done = true
}

// greet — function thường, trả về nhiều giá trị (idiomatic Go)
func greet(name string) (string, int) {
	msg := fmt.Sprintf("Xin chào, %s!", strings.ToUpper(name))
	return msg, len(name)
}

func main() {
	msg, length := greet("go developer")
	fmt.Println(msg, "— length:", length)

	task := Task{ID: 1, Title: "Học Go structs", Done: false}
	fmt.Println(task)

	task.markDone() // pointer receiver sửa task gốc
	fmt.Println("Sau markDone:", task)
}
