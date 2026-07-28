"""Đáp án Module 02"""
from collections import Counter, OrderedDict


def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))


def most_common_element(arr: list) -> any:
    return Counter(arr).most_common(1)[0][0]


def merge_dicts(d1: dict, d2: dict) -> dict:
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] = max(result[key], value)
        else:
            result[key] = value
    return result


def is_anagram(s1: str, s2: str) -> bool:
    return Counter(s1.lower()) == Counter(s2.lower())


class SimpleLRUCache:
    def __init__(self, capacity: int = 3):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    print(reverse_words("hello world python"))
    print(most_common_element([1, 2, 2, 3, 3, 3, 4]))
    print(merge_dicts({"a": 1, "b": 2}, {"b": 5, "c": 3}))
    print(is_anagram("listen", "silent"))

    cache = SimpleLRUCache(3)
    for k, v in [("a", 1), ("b", 2), ("c", 3), ("d", 4)]:
        cache.put(k, v)
        print(f"  put({k},{v}) → cache={dict(cache.cache)}")
