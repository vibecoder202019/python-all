"""
Module 03 — Ví dụ 1: Class cơ bản
Chạy: python examples/01_class_basics.py

YÊU CẦU ĐỀ BÀI:
  - Định nghĩa class với __init__, thuộc tính instance và class
  - Dùng @property và setter để validate dữ liệu (GPA 0-4)
  - Encapsulation: thuộc tính private (_gpa, _balance)
  - Implement __str__ và __repr__

KẾT QUẢ MONG ĐỢI (khi chạy):
  - Student(Nguyễn Văn A, GPA=3.80) sau enroll 2 môn
  - Trường: AI Academy, Môn: ['Python 101', 'Machine Learning']
  - Account(Minh, balance=1,300,000) sau nạp/rút
  - Lịch sử giao dịch: ['+500,000', '-200,000']
"""


class Student:
    school = "AI Academy"  # thuộc tính class — dùng chung cho mọi instance

    def __init__(self, name: str, student_id: str, gpa: float = 0.0):
        self.name = name
        self.student_id = student_id
        self._gpa = gpa  # private: truy cập qua property
        self._courses: list[str] = []

    @property
    def gpa(self) -> float:
        return self._gpa

    @gpa.setter
    def gpa(self, value: float):
        if not 0 <= value <= 4.0:
            raise ValueError("GPA phải từ 0.0 đến 4.0")
        self._gpa = value

    def enroll(self, course: str) -> None:
        if course not in self._courses:
            self._courses.append(course)

    def __str__(self) -> str:
        return f"Student({self.name}, GPA={self._gpa:.2f})"

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', id='{self.student_id}', gpa={self._gpa})"


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        self._balance = initial_balance
        self._transactions: list[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền nạp phải > 0")
        self._balance += amount
        self._transactions.append(f"+{amount:,.0f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")
        if amount > self._balance:
            raise ValueError(f"Số dư không đủ: {self._balance:,.0f}")
        self._balance -= amount
        self._transactions.append(f"-{amount:,.0f}")

    def __str__(self) -> str:
        return f"Account({self.owner}, balance={self._balance:,.0f})"


# ── Demo ──
if __name__ == "__main__":
    s = Student("Nguyễn Văn A", "SV001", 3.5)
    s.enroll("Python 101")
    s.enroll("Machine Learning")
    s.gpa = 3.8
    print(s)
    print(f"Trường: {Student.school}, Môn: {s._courses}")

    acc = BankAccount("Minh", 1_000_000)
    acc.deposit(500_000)
    acc.withdraw(200_000)
    print(acc)
    print(f"Lịch sử: {acc._transactions}")
