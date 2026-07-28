"""
Bước 01 — Cửa sổ game và màu sắc
Chạy: python examples/01_cua_so_va_mau.py
Nhấn ESC hoặc đóng cửa sổ để thoát.
"""
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Bước 1: Cửa sổ & Màu sắc")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)

# Bảng màu cho trẻ em
COLORS = {
    "sky": (135, 206, 235),
    "grass": (34, 139, 34),
    "sun": (255, 215, 0),
    "cloud": (255, 255, 255),
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # Vẽ nền trời và cỏ
    screen.fill(COLORS["sky"])
    pygame.draw.rect(screen, COLORS["grass"], (0, HEIGHT - 100, WIDTH, 100))

    # Vẽ mặt trời
    pygame.draw.circle(screen, COLORS["sun"], (700, 80), 50)

    # Vẽ mây (3 hình tròn)
    for cx in [150, 400, 600]:
        pygame.draw.circle(screen, COLORS["cloud"], (cx, 100), 30)
        pygame.draw.circle(screen, COLORS["cloud"], (cx + 25, 95), 25)
        pygame.draw.circle(screen, COLORS["cloud"], (cx - 20, 95), 25)

    text = font.render("Buổi 1: Vẽ bầu trời! Nhấn ESC để thoát", True, (50, 50, 50))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
