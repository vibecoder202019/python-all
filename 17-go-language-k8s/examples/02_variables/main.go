// Ví dụ 02 — Biến, kiểu dữ liệu, vòng lặp
// Chạy: go run examples/02_variables/main.go
package main

import "fmt"

func main() {
	// Khai báo ngắn := — Go tự suy kiểu
	name := "Học viên Go"
	age := 25
	price := 19.99
	isActive := true

	fmt.Printf("name=%s age=%d price=%.2f active=%v\n", name, age, price, isActive)

	// Array — kích thước cố định
	numbers := [3]int{10, 20, 30}

	// Slice — mảng động (dùng nhiều nhất, giống list Python)
	langs := []string{"Go", "Python", "Rust"}
	langs = append(langs, "TypeScript") // thêm phần tử

	fmt.Println("Array:", numbers)
	fmt.Println("Slice:", langs)

	// Map — giống dict Python
	scores := map[string]int{"Alice": 90, "Bob": 85}
	scores["Charlie"] = 88

	// for range — duyệt slice/map
	fmt.Println("\n--- for range slice ---")
	for i, lang := range langs {
		fmt.Printf("  [%d] %s\n", i, lang)
	}

	fmt.Println("\n--- for range map ---")
	for k, v := range scores {
		fmt.Printf("  %s: %d\n", k, v)
	}

	// if với khai báo biến inline
	if v, ok := scores["Alice"]; ok {
		fmt.Printf("\nAlice score: %d\n", v)
	}
}
