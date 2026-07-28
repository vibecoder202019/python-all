"""
Bước 02 — Vẽ hình và hiển thị chữ
Chạy: python examples/02_hinh_va_text.py
"""
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Bước 2: Hình & Text")
clock = pygame.time.Clock()
title_font = pygame.font.SysFont("Arial", 36, bold=True)
label_font = pygame.font.SysFont("Arial", 22)

SHAPES = [
    ("Hình tròn", "circle", (255, 100, 100), (200, 300)),
    ("Hình vuông", "rect", (100, 200, 255), (400, 300)),
    ("Tam giác", "triangle", (100, 255, 100), (600, 300)),
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill((240, 248, 255))

    title = title_font.render("Các hình cơ bản", True, (30, 30, 80))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 30))

    for name, shape, color, (x, y) in SHAPES:
        if shape == "circle":
            pygame.draw.circle(screen, color, (x, y), 50)
        elif shape == "rect":
            pygame.draw.rect(screen, color, (x - 50, y - 50, 100, 100), border_radius=10)
        elif shape == "triangle":
            points = [(x, y - 55), (x - 50, y + 40), (x + 50, y + 40)]
            pygame.draw.polygon(screen, color, points)

        label = label_font.render(name, True, (50, 50, 50))
        screen.blit(label, (x - label.get_width() // 2, y + 70))

    hint = label_font.render("Nhấn ESC để thoát", True, (100, 100, 100))
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
