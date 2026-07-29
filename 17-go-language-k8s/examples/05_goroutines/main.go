// Ví dụ 05 — Goroutines và Channels (concurrency)
// Chạy: go run examples/05_goroutines/main.go
package main

import (
	"fmt"
	"sync"
	"time"
)

// fetchData — giả lập I/O chậm
func fetchData(id int, ch chan<- string, wg *sync.WaitGroup) {
	defer wg.Done() // giảm counter WaitGroup khi goroutine xong
	time.Sleep(time.Duration(id*100) * time.Millisecond)
	ch <- fmt.Sprintf("Data from worker %d", id)
}

func main() {
	fmt.Println("=== Goroutines + Channels ===\n")

	// chan string — channel truyền string giữa goroutines
	ch := make(chan string, 3) // buffer 3 — không block đến khi đầy
	var wg sync.WaitGroup

	// go keyword — chạy function trong goroutine (lightweight thread)
	for i := 1; i <= 3; i++ {
		wg.Add(1)
		go fetchData(i, ch, &wg)
	}

	// WaitGroup — đợi tất cả goroutine hoàn thành
	wg.Wait()
	close(ch) // đóng channel sau khi gửi xong

	for msg := range ch {
		fmt.Println("  Received:", msg)
	}

	// select — multiplex channels (giống switch cho channels)
	fmt.Println("\n=== select timeout ===")
	timeout := time.After(50 * time.Millisecond)
	work := make(chan string)

	go func() {
		time.Sleep(200 * time.Millisecond)
		work <- "done"
	}()

	select {
	case w := <-work:
		fmt.Println("  Work:", w)
	case <-timeout:
		fmt.Println("  ⏱ Timeout — work quá chậm")
	}
}
