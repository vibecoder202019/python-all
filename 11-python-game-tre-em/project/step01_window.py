"""
Module 11 — Dự án Bước 1: Cửa sổ và nền trời

Chạy: python project/step01_window.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Import hằng số từ common.py (WIDTH, HEIGHT, FPS, SKY, GRASS).
  2. Vẽ nền trời xanh và dải cỏ xanh phía dưới.
  3. Hiển thị tiêu đề "Catch the Stars — Bước 1: Nền game".

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - Cửa sổ 800×600, nền trời + cỏ, chữ tiêu đề giữa màn hình.
  - ESC hoặc đóng cửa sổ để thoát.
═══════════════════════════════════════════════════════════════════════════
"""
import pygame
import sys
from common import WIDTH, HEIGHT, FPS, SKY, GRASS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Stars — Bước 1")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28, bold=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill(SKY)
    pygame.draw.rect(screen, GRASS, (0, HEIGHT - 80, WIDTH, 80))
    title = font.render("Catch the Stars — Bước 1: Nền game", True, (255, 255, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
