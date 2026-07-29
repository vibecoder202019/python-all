// Ví dụ 06 — HTTP server + JSON (nền tảng REST API)
// Chạy: go run examples/06_http_json/main.go
// Test: curl http://localhost:8080/health
//       curl http://localhost:8080/tasks
package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

// Task — struct JSON với tags (map field → key JSON)
type Task struct {
	ID    int    `json:"id"`
	Title string `json:"title"`
	Done  bool   `json:"done"`
}

var tasks = []Task{
	{ID: 1, Title: "Học Go syntax", Done: true},
	{ID: 2, Title: "Viết HTTP server", Done: false},
}

func main() {
	// http.HandleFunc — đăng ký route handler
	http.HandleFunc("/health", healthHandler)
	http.HandleFunc("/tasks", tasksHandler)

	addr := ":8080"
	fmt.Printf("Server chạy tại http://localhost%s\n", addr)
	fmt.Println("Thử: curl http://localhost:8080/tasks")

	// ListenAndServe — block, lắng nghe request
	log.Fatal(http.ListenAndServe(addr, nil))
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	// w.Header — set response headers
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
}

func tasksHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	// json.NewEncoder(w).Encode — serialize struct → JSON response
	json.NewEncoder(w).Encode(tasks)
}
