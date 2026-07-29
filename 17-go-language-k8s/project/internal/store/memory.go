// Package store — lưu trữ in-memory (thay bằng PostgreSQL ở production)
package store

import (
	"sync"

	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/models"
)

// TaskStore — interface cho phép mock trong test
type TaskStore interface {
	List() []models.Task
	Get(id int) (models.Task, bool)
	Create(title string) models.Task
	Toggle(id int) (models.Task, bool)
	Delete(id int) bool
}

// MemoryStore — thread-safe in-memory store
type MemoryStore struct {
	mu     sync.RWMutex // RWMutex — nhiều reader hoặc 1 writer
	tasks  []models.Task
	nextID int
}

func NewMemoryStore() *MemoryStore {
	return &MemoryStore{nextID: 1}
}

func (s *MemoryStore) List() []models.Task {
	s.mu.RLock()
	defer s.mu.RUnlock()
	out := make([]models.Task, len(s.tasks))
	copy(out, s.tasks)
	return out
}

func (s *MemoryStore) Get(id int) (models.Task, bool) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	for _, t := range s.tasks {
		if t.ID == id {
			return t, true
		}
	}
	return models.Task{}, false
}

func (s *MemoryStore) Create(title string) models.Task {
	s.mu.Lock()
	defer s.mu.Unlock()
	t := models.Task{ID: s.nextID, Title: title, Done: false, CreatedAt: models.Now()}
	s.nextID++
	s.tasks = append(s.tasks, t)
	return t
}

func (s *MemoryStore) Toggle(id int) (models.Task, bool) {
	s.mu.Lock()
	defer s.mu.Unlock()
	for i, t := range s.tasks {
		if t.ID == id {
			s.tasks[i].Done = !s.tasks[i].Done
			return s.tasks[i], true
		}
	}
	return models.Task{}, false
}

func (s *MemoryStore) Delete(id int) bool {
	s.mu.Lock()
	defer s.mu.Unlock()
	for i, t := range s.tasks {
		if t.ID == id {
			s.tasks = append(s.tasks[:i], s.tasks[i+1:]...)
			return true
		}
	}
	return false
}
