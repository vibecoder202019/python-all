# Multi-stage build — image nhỏ, an toàn hơn
# Stage 1: build binary
FROM golang:1.22-alpine AS builder

WORKDIR /src
# Copy go.mod trước — tận dụng Docker layer cache
COPY go.mod ./
COPY . .

# CGO_ENABLED=0 — static binary, chạy trên alpine/scratch
# -ldflags="-s -w" — strip debug info, giảm size
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o /server ./cmd/server

# Stage 2: runtime image tối giản
FROM alpine:3.19

# CA certs — cần nếu gọi HTTPS ra ngoài
RUN apk add --no-cache ca-certificates

# Non-root user — best practice K8s security
RUN adduser -D -u 1000 appuser
USER appuser

WORKDIR /app
COPY --from=builder /server .

EXPOSE 8080
ENV PORT=8080

# HEALTHCHECK — Docker/K8s probe
HEALTHCHECK --interval=30s --timeout=3s \
  CMD wget -qO- http://localhost:8080/health || exit 1

ENTRYPOINT ["./server"]
