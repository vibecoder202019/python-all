// Package handlers — HTTP handlers cho Task API
package handlers

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"

	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/models"
	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/store"
)

const version = "1.0.0"

type Handler struct {
	Store store.TaskStore
}

func New(store store.TaskStore) *Handler {
	return &Handler{Store: store}
}

// RegisterRoutes — đăng ký tất cả routes lên ServeMux
func (h *Handler) RegisterRoutes(mux *http.ServeMux) {
	mux.HandleFunc("/health", h.Health)
	mux.HandleFunc("/tasks", h.Tasks)
	mux.HandleFunc("/tasks/", h.TaskByID)
}

func (h *Handler) Health(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, models.HealthResponse{
		Status: "ok", Service: "go-task-api", Version: version,
	})
}

func (h *Handler) Tasks(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		writeJSON(w, http.StatusOK, h.Store.List())
	case http.MethodPost:
		var req models.CreateTaskRequest
		if err := json.NewDecoder(r.Body).Decode(&req); err != nil || strings.TrimSpace(req.Title) == "" {
			writeError(w, http.StatusBadRequest, "title required")
			return
		}
		task := h.Store.Create(req.Title)
		writeJSON(w, http.StatusCreated, task)
	default:
		writeError(w, http.StatusMethodNotAllowed, "method not allowed")
	}
}

func (h *Handler) TaskByID(w http.ResponseWriter, r *http.Request) {
	id, err := parseID(r.URL.Path)
	if err != nil {
		writeError(w, http.StatusBadRequest, "invalid id")
		return
	}

	switch r.Method {
	case http.MethodGet:
		if task, ok := h.Store.Get(id); ok {
			writeJSON(w, http.StatusOK, task)
		} else {
			writeError(w, http.StatusNotFound, "task not found")
		}
	case http.MethodPatch:
		if task, ok := h.Store.Toggle(id); ok {
			writeJSON(w, http.StatusOK, task)
		} else {
			writeError(w, http.StatusNotFound, "task not found")
		}
	case http.MethodDelete:
		if h.Store.Delete(id) {
			w.WriteHeader(http.StatusNoContent)
		} else {
			writeError(w, http.StatusNotFound, "task not found")
		}
	default:
		writeError(w, http.StatusMethodNotAllowed, "method not allowed")
	}
}

func parseID(path string) (int, error) {
	parts := strings.Split(strings.Trim(path, "/"), "/")
	if len(parts) != 2 {
		return 0, strconv.ErrSyntax
	}
	return strconv.Atoi(parts[1])
}

func writeJSON(w http.ResponseWriter, code int, v any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)
	json.NewEncoder(w).Encode(v)
}

func writeError(w http.ResponseWriter, code int, msg string) {
	writeJSON(w, code, map[string]string{"error": msg})
}
