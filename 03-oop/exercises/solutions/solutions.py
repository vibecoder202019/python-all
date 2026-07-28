"""
Module 03 — Đáp án bài tập: Hình học, Stack, Thư viện, KNN
Chạy: python exercises/solutions/solutions.py

YÊU CẦU ĐỀ BÀI:
  - Class Rectangle: area, perimeter, is_square
  - Class Stack: push, pop, peek, is_empty với __len__
  - Class Library: mượn/trả sách, tìm theo tác giả
  - Abstract BaseModel + KNNClassifier cho ML cơ bản

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Square 5x5: area=25, is_square=True
  - Stack pop: 2, len=2
  - Borrowed: Python Crash Course
  - Predict [4,4]: ['A']
"""
from abc import ABC, abstractmethod
import math


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        return self.width == self.height


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack rỗng")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def borrow_book(self, isbn: str) -> Book | None:
        for book in self.books:
            if book.isbn == isbn and book.available:
                book.available = False
                return book
        return None

    def return_book(self, isbn: str) -> bool:
        for book in self.books:
            if book.isbn == isbn:
                book.available = True
                return True
        return False

    def search_by_author(self, author: str) -> list[Book]:
        return [b for b in self.books if b.author.lower() == author.lower()]


class BaseModel(ABC):
    @abstractmethod
    def train(self, X, y): ...
    @abstractmethod
    def predict(self, X): ...
    @abstractmethod
    def evaluate(self, X, y) -> float: ...


class KNNClassifier(BaseModel):
    def __init__(self, k: int = 3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def train(self, X, y):
        self.X_train = X
        self.y_train = y

    def _distance(self, a, b):
        return math.sqrt(sum((ai - bi) ** 2 for ai, bi in zip(a, b)))  # khoảng cách Euclidean

    def predict(self, X):
        predictions = []
        for x in X:
            distances = [(self._distance(x, xi), yi) for xi, yi in zip(self.X_train, self.y_train)]
            distances.sort()
            k_nearest = [label for _, label in distances[: self.k]]
            predictions.append(max(set(k_nearest), key=k_nearest.count))  # bỏ phiếu đa số
        return predictions

    def evaluate(self, X, y) -> float:
        preds = self.predict(X)
        correct = sum(1 for p, t in zip(preds, y) if p == t)
        return correct / len(y)


# ── Demo ──
if __name__ == "__main__":
    r = Rectangle(5, 5)
    print(f"Square 5x5: area={r.area()}, is_square={r.is_square()}")

    stack = Stack()
    for i in range(3):
        stack.push(i)
    print(f"Stack pop: {stack.pop()}, len={len(stack)}")

    lib = Library()
    lib.add_book(Book("Python Crash Course", "Eric Matthes", "ISBN001"))
    lib.add_book(Book("Fluent Python", "Luciano Ramalho", "ISBN002"))
    borrowed = lib.borrow_book("ISBN001")
    print(f"Borrowed: {borrowed.title if borrowed else 'None'}")

    X_train = [[1, 1], [2, 2], [3, 3], [6, 6], [7, 7], [8, 8]]
    y_train = ["A", "A", "A", "B", "B", "B"]
    knn = KNNClassifier(k=3)
    knn.train(X_train, y_train)
    print(f"Predict [4,4]: {knn.predict([[4, 4]])}")
