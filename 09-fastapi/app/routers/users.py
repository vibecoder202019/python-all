"""Users CRUD router — minh họa REST API cơ bản"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import UserCreate, UserResponse, UserUpdate

router = APIRouter()

# In-memory database (demo)
_users_db: dict[int, dict] = {
    1: {"id": 1, "name": "Nguyễn Văn A", "email": "a@example.com", "age": 25},
    2: {"id": 2, "name": "Trần Thị B", "email": "b@example.com", "age": 30},
}
_next_id = 3


@router.get("", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10):
    """Lấy danh sách users (có phân trang)."""
    users = list(_users_db.values())
    return users[skip : skip + limit]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Lấy thông tin user theo ID."""
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")
    return _users_db[user_id]


@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """Tạo user mới."""
    global _next_id
    for existing in _users_db.values():
        if existing["email"] == user.email:
            raise HTTPException(status_code=400, detail="Email đã tồn tại")

    new_user = {"id": _next_id, **user.model_dump()}
    _users_db[_next_id] = new_user
    _next_id += 1
    return new_user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate):
    """Cập nhật user."""
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")

    update_data = user.model_dump(exclude_unset=True)
    _users_db[user_id].update(update_data)
    return _users_db[user_id]


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    """Xóa user."""
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")
    del _users_db[user_id]
