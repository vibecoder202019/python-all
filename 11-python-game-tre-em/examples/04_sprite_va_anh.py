"""
Module 11 — Ví dụ 4: Sprite và animation

Chạy: python examples/04_sprite_va_anh.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Tạo class Star kế thừa pygame.sprite.Sprite.
  2. Vẽ hình ngôi sao 5 cánh bằng polygon trên Surface trong suốt.
  3. Dùng sprite.Group quản lý 8 ngôi sao; update mỗi frame.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - 8 ngôi sao vàng xếp ngang giữa màn hình trên nền tím đậm.
  - Counter "Frame: N" tăng liên tục — animation đang chạy.
═══════════════════════════════════════════════════════════════════════════
"""
import math
import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Module 11 — Bước 4: Sprite & Animation")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)


class Star(pygame.sprite.Sprite):
    """Sprite ngôi sao — vẽ lại image mỗi frame để tạo hiệu ứng."""
    def __init__(self, x: int, y: int):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self._draw_star()
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def _draw_star(self):
        cx, cy, r = 15, 15, 12
        points = []
        for i in range(10):
            angle = math.radians(i * 36 - 90)
            radius = r if i % 2 == 0 else r // 2
            points.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
        pygame.draw.polygon(self.image, (255, 220, 0), points)

    def update(self):
        self.angle = (self.angle + 2) % 360
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        self._draw_star()


stars = pygame.sprite.Group()
for i in range(8):
    stars.add(Star(100 + i * 80, 300))

running = True
frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    frame += 1
    stars.update()

    screen.fill((20, 10, 50))
    stars.draw(screen)

    text = font.render(f"Sprite animation — Frame: {frame}", True, (255, 255, 255))
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
