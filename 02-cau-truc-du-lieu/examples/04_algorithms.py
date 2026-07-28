"""Module 02 — Algorithms cơ bản"""


def linear_search(arr: list, target) -> int:
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr: list, target) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(arr: list) -> list:
    result = arr.copy()
    n = len(result)
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Tìm 2 số có tổng = target — dùng dict O(n)."""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None


# --- Demo ---
data = [2, 5, 8, 12, 16, 23, 38, 45, 67, 78]
target = 23

print(f"Mảng: {data}")
print(f"Linear search {target}: index={linear_search(data, target)}")
print(f"Binary search {target}: index={binary_search(data, target)}")

unsorted = [64, 34, 25, 12, 22, 11, 90]
print(f"\nBubble sort: {unsorted} → {bubble_sort(unsorted)}")

nums = [2, 7, 11, 15]
result = two_sum(nums, 9)
print(f"\nTwo Sum [2,7,11,15], target=9: indices={result} → values=({nums[result[0]]}, {nums[result[1]]})")
