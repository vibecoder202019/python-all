// Package models — định nghĩa struct dữ liệu
package models

import "time"

// Task — entity chính của API
type Task struct {
	ID        int       `json:"id"`
	Title     string    `json:"title"`
	Done      bool      `json:"done"`
	CreatedAt time.Time `json:"created_at"`
}

// CreateTaskRequest — body POST /tasks
type CreateTaskRequest struct {
	Title string `json:"title"`
}

// HealthResponse — GET /health
type HealthResponse struct {
	Status  string `json:"status"`
	Service string `json:"service"`
	Version string `json:"version"`
}
