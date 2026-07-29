// Task API — entry point
// Chạy local: go run ./cmd/server
// Build:       go build -o bin/server ./cmd/server
package main

import (
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/handlers"
	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/middleware"
	"github.com/vibecoder202019/python-all/17-go-language-k8s/project/internal/store"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	// Dependency injection — store → handler
	memStore := store.NewMemoryStore()
	h := handlers.New(memStore)

	mux := http.NewServeMux()
	h.RegisterRoutes(mux)

	// Middleware chain — CORS → Logging → handler
	handler := middleware.CORS(middleware.Logging(mux))

	addr := fmt.Sprintf(":%s", port)
	log.Printf("go-task-api listening on %s", addr)
	log.Fatal(http.ListenAndServe(addr, handler))
}
