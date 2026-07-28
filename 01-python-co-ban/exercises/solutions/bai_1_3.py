"""Đáp án Bài 1-3 — Module 01"""


def bmi_calculator(weight_kg: float, height_m: float) -> tuple[float, str]:
    bmi = round(weight_kg / (height_m ** 2), 1)
    if bmi < 18.5:
        category = "Thiếu cân"
    elif bmi < 25:
        category = "Bình thường"
    elif bmi < 30:
        category = "Thừa cân"
    else:
        category = "Béo phì"
    return bmi, category


def fizzbuzz(n: int = 100) -> None:
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()


def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


if __name__ == "__main__":
    print(bmi_calculator(70, 1.75))
    fizzbuzz(30)
    print(f"\nNguyên âm trong 'Hello World': {count_vowels('Hello World')}")
