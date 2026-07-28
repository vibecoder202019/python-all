"""
Module 03 — Ví dụ 3: Magic Methods
Chạy: python examples/03_magic_methods.py

YÊU CẦU ĐỀ BÀI:
  - Vector: overload +, -, *, == và __repr__
  - ShoppingCart: __len__, __getitem__, __str__
  - Hiểu cách Python gọi magic methods khi dùng toán tử

KẾT QUẢ MONG ĐỢI (khi chạy):
  - v1 = Vector(3,4), |v1| = 5.00
  - v1 + v2 = Vector(4, 6), v1 * 2 = Vector(6, 8)
  - v1 == v2: False
  - Giỏ hàng 3 sản phẩm, tổng 15,900,000
  - Số lượng items: 4 (1 laptop + 2 mouse + 1 hub)
"""


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return False
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return 2  # vector 2 chiều luôn có 2 thành phần

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


class ShoppingCart:
    def __init__(self):
        self._items: list[tuple[str, float, int]] = []  # (tên, giá, số lượng)

    def add(self, name: str, price: float, qty: int = 1):
        self._items.append((name, price, qty))

    def __len__(self) -> int:
        return sum(qty for _, _, qty in self._items)  # tổng số lượng sản phẩm

    def __getitem__(self, index: int):
        return self._items[index]  # cho phép cart[0]

    def total(self) -> float:
        return sum(price * qty for _, price, qty in self._items)

    def __str__(self) -> str:
        lines = [f"  {name}: {price:,.0f} x {qty}" for name, price, qty in self._items]
        return "Cart:\n" + "\n".join(lines) + f"\n  Total: {self.total():,.0f}"


# ── Demo ──
if __name__ == "__main__":
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(f"v1 = {v1}, |v1| = {v1.magnitude():.2f}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 == v2: {v1 == v2}")

    cart = ShoppingCart()
    cart.add("Laptop", 15_000_000, 1)
    cart.add("Mouse", 200_000, 2)
    cart.add("USB-C Hub", 500_000, 1)
    print(f"\n{cart}")
    print(f"Số lượng items: {len(cart)}")
    print(f"Item đầu: {cart[0]}")
