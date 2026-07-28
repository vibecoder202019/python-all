"""
Module 03 — Ví dụ 2: Kế thừa và Đa hình
Chạy: python examples/02_inheritance.py

YÊU CẦU ĐỀ BÀI:
  - Abstract class Shape với @abstractmethod area/perimeter
  - Rectangle và Circle kế thừa Shape
  - Polymorphism: Dog/Cat override speak()
  - Hàm print_shape_info nhận bất kỳ Shape nào

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Diện tích/chu vi Rectangle(4x5), Circle(r=3), Rectangle(10x2)
  - Tổng diện tích ≈ 68.27
  - 🐕 Rex: Woof!, 🐱 Mimi: Meow!, 🐕 Buddy: Woof!
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height})"


class Circle(Shape):
    PI = 3.14159265

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return self.PI * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * self.PI * self.radius

    def __repr__(self):
        return f"Circle(r={self.radius})"


class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return f"🐕 {self.name}: Woof!"


class Cat(Animal):
    def speak(self) -> str:
        return f"🐱 {self.name}: Meow!"


def print_shape_info(shape: Shape):
    print(f"  {shape} → area={shape.area():.2f}, perimeter={shape.perimeter():.2f}")


# ── Demo ──
if __name__ == "__main__":
    shapes = [Rectangle(4, 5), Circle(3), Rectangle(10, 2)]
    print("=== Shapes ===")
    for s in shapes:
        print_shape_info(s)  # đa hình: gọi area() tùy loại hình
    print(f"Tổng diện tích: {sum(s.area() for s in shapes):.2f}")

    print("\n=== Polymorphism ===")
    animals = [Dog("Rex"), Cat("Mimi"), Dog("Buddy")]
    for a in animals:
        print(f"  {a.speak()}")  # mỗi loài override speak() khác nhau
