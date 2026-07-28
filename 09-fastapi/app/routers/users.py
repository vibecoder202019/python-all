"""
Users CRUD router — minh họa REST API cơ bản.

MỤC ĐÍCH:
    Cung cấp các endpoint CRUD (Create, Read, Update, Delete) cho users
    dùng in-memory dict làm database demo.

YÊU CẦU:
    Pydantic schemas: UserCreate, UserResponse, UserUpdate (app/models/schemas.py)

KẾT QUẢ MONG ĐỢI:
    - GET /users — danh sách users (phân trang)
    - GET /users/{id} — chi tiết user
    - POST /users — tạo user mới (201)
    - PUT /users/{id} — cập nhật user
    - DELETE /users/{id} — xóa user (204)
"""
from fastapi import APIRouter, HTTPException

from app.models.schemas import UserCreate, UserResponse, UserUpdate

# APIRouter — nhóm các route liên quan, gắn vào app qua include_router
router = APIRouter()

# In-memory database (demo) — mất dữ liệu khi restart server
_users_db: dict[int, dict] = {
    1: {"id": 1, "name": "Nguyễn Văn A", "email": "a@example.com", "age": 25},
    2: {"id": 2, "name": "Trần Thị B", "email": "b@example.com", "age": 30},
}
_next_id = 3  # Auto-increment ID cho user mới


@router.get("", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10):
    """
    Lấy danh sách users (có phân trang).

    Query params:
        skip: bỏ qua N bản ghi đầu
        limit: số bản ghi tối đa trả về
    """
    users = list(_users_db.values())
    return users[skip : skip + limit]


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """Lấy thông tin user theo ID — trả 404 nếu không tồn tại."""
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")
    return _users_db[user_id]


@router.post("", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    """
    Tạo user mới.

    - FastAPI tự validate body qua UserCreate (Pydantic)
    - status_code=201: Created (chuẩn REST)
    - Kiểm tra email trùng → 400
    """
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
    """
    Cập nhật user — chỉ ghi đè các field client gửi lên.

    exclude_unset=True: bỏ qua field None/không gửi.
    """
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")

    update_data = user.model_dump(exclude_unset=True)
    _users_db[user_id].update(update_data)
    return _users_db[user_id]


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    """Xóa user — trả 204 No Content khi thành công."""
    if user_id not in _users_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} không tồn tại")
    del _users_db[user_id]
