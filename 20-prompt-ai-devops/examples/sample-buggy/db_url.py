"""File mẫu có bug — dùng Lab 04 prompt debug."""
from __future__ import annotations


def parse_port(value: str) -> int:
    """Chuyển string port sang int — có bug edge case."""
    return int(value)  # ValueError nếu value rỗng hoặc không phải số


def build_db_url(host: str, port: str, user: str, password: str) -> str:
    port_num = parse_port(port)
    return f"postgresql://{user}:{password}@{host}:{port_num}/app"


if __name__ == "__main__":
    # Bug: port="" gây ValueError
    print(build_db_url("localhost", "", "admin", "secret"))
