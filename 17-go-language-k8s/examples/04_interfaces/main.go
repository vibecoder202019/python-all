// Ví dụ 04 — Interfaces (đa hình trong Go)
// Chạy: go run examples/04_interfaces/main.go
package main

import (
	"fmt"
	"math"
)

// Shape — interface: tập method signature (không cần implements keyword)
type Shape interface {
	Area() float64
	Perimeter() float64
}

type Circle struct {
	Radius float64
}

type Rectangle struct {
	Width, Height float64
}

// Circle implements Shape vì có đủ methods Area và Perimeter
func (c Circle) Area() float64 {
	return math.Pi * c.Radius * c.Radius
}

func (c Circle) Perimeter() float64 {
	return 2 * math.Pi * c.Radius
}

func (r Rectangle) Area() float64 {
	return r.Width * r.Height
}

func (r Rectangle) Perimeter() float64 {
	return 2 * (r.Width + r.Height)
}

// printShape — nhận interface → bất kỳ type nào implement Shape đều truyền được
func printShape(s Shape) {
	fmt.Printf("Area=%.2f Perimeter=%.2f\n", s.Area(), s.Perimeter())
}

func main() {
	shapes := []Shape{
		Circle{Radius: 5},
		Rectangle{Width: 4, Height: 6},
	}
	for i, s := range shapes {
		fmt.Printf("Shape %d: ", i+1)
		printShape(s)
	}
}
