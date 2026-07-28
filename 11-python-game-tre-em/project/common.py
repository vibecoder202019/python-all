"""
Module 11 — Hằng số dùng chung cho dự án Catch the Stars

File này tập trung các giá trị cấu hình (kích thước cửa sổ, màu sắc, kích thước
sprite) để các bước step01→step06 import và dùng nhất quán, tránh magic number.

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Định nghĩa kích thước cửa sổ và tốc độ khung hình (FPS).
  2. Định nghĩa bảng màu cho nền trời, cỏ, nhân vật, sao, đá và chữ.
  3. Định nghĩa kích thước nhân vật, sao và đá để va chạm chính xác.

KẾT QUẢ MONG ĐỢI:
  - Các file step*.py import từ common mà không cần lặp lại hằng số.
  - Game hiển thị đồng nhất: cửa sổ 800×600, 60 FPS, màu trời xanh nhạt.
═══════════════════════════════════════════════════════════════════════════
"""

# ── Kích thước cửa sổ và tốc độ game ──
WIDTH, HEIGHT = 800, 600   # Chiều rộng × cao cửa sổ (pixel)
FPS = 60                   # Số khung hình/giây — game mượt, không quá nhanh

# ── Bảng màu RGB (Red, Green, Blue) ──
SKY = (135, 206, 235)          # Xanh trời — màu nền phía trên
GRASS = (34, 139, 34)          # Xanh lá — dải cỏ phía dưới màn hình
PLAYER_COLOR = (100, 200, 255) # Xanh nhạt — màu phi hành gia (nhân vật)
STAR_COLOR = (255, 220, 0)     # Vàng — sao thưởng (+10 điểm khi bắt)
ROCK_COLOR = (120, 120, 120)   # Xám — đá phạt (-1 mạng khi va chạm)
TEXT_COLOR = (30, 30, 60)      # Xanh đậm — chữ HUD (điểm, mạng, level)

# ── Kích thước sprite (pixel) — dùng cho pygame.Rect và va chạm ──
PLAYER_W, PLAYER_H = 50, 50   # Chiều rộng × cao nhân vật
STAR_SIZE = 25                # Đường kính vùng va chạm sao (hình tròn)
ROCK_SIZE = 30                # Cạnh hình vuông vùng va chạm đá
