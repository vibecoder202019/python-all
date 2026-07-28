"""
Module 11 — Dự án Bước 6: Game hoàn chỉnh với Menu

Chạy: python project/step06_final.py

═══════════════════════════════════════════════════════════════════════════
YÊU CẦU ĐỀ BÀI:
  1. Màn hình menu: SPACE bắt đầu, hiển thị kỷ lục high score.
  2. Gameplay đầy đủ: điểm, mạng, level, Game Over.
  3. ESC về menu; R chơi lại khi Game Over.

KẾT QUẢ MONG ĐỢI (trên màn hình):
  - Menu: "⭐ Catch the Stars" + "Nhấn SPACE để bắt đầu".
  - Chơi: HUD điểm/mạng/level; Game Over hiện điểm + kỷ lục.
  - R → chơi lại; ESC → menu.
═══════════════════════════════════════════════════════════════════════════
"""
import random
import pygame
import sys
from common import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⭐ Catch the Stars — Game Hoàn chỉnh")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22, bold=True)
title_font = pygame.font.SysFont("Arial", 52, bold=True)


class Game:
    """Quản lý state machine: menu → playing → gameover."""
    def __init__(self):
        self.reset()
        self.state = "menu"  # menu | playing | gameover

    def reset(self):
        self.player = pygame.Rect(WIDTH // 2 - PLAYER_W // 2, HEIGHT - 100, PLAYER_W, PLAYER_H)
        self.stars: list[pygame.Rect] = []
        self.rocks: list[pygame.Rect] = []
        self.score = 0
        self.lives = 3
        self.level = 1
        self.spawn_timer = 0
        self.high_score = getattr(self, "high_score", 0)

    def start(self):
        self.reset()
        self.state = "playing"

    def spawn(self):
        self.spawn_timer += 1
        interval = max(15, 40 - self.level * 3)
        if self.spawn_timer > interval:
            self.spawn_timer = 0
            if random.random() < 0.75:
                self.stars.append(pygame.Rect(random.randint(0, WIDTH - STAR_SIZE), -STAR_SIZE, STAR_SIZE, STAR_SIZE))
            else:
                self.rocks.append(pygame.Rect(random.randint(0, WIDTH - ROCK_SIZE), -ROCK_SIZE, ROCK_SIZE, ROCK_SIZE))

    def update(self, keys):
        if self.state != "playing":
            return
        self.spawn()
        speed = 7
        if keys[pygame.K_LEFT]:
            self.player.x = max(0, self.player.x - speed)
        if keys[pygame.K_RIGHT]:
            self.player.x = min(WIDTH - PLAYER_W, self.player.x + speed)

        for star in self.stars[:]:
            star.y += 3 + self.level
            if self.player.colliderect(star):
                self.score += 10
                if self.score % 50 == 0:
                    self.level += 1
                self.stars.remove(star)
            elif star.top > HEIGHT:
                self.stars.remove(star)

        for rock in self.rocks[:]:
            rock.y += 4 + self.level
            if self.player.colliderect(rock):
                self.lives -= 1
                self.rocks.remove(rock)
                if self.lives <= 0:
                    self.high_score = max(self.high_score, self.score)
                    self.state = "gameover"
            elif rock.top > HEIGHT:
                self.rocks.remove(rock)

    def draw(self):
        screen.fill(SKY)
        pygame.draw.rect(screen, GRASS, (0, HEIGHT - 80, WIDTH, 80))

        if self.state == "menu":
            title = title_font.render("⭐ Catch the Stars", True, (255, 220, 0))
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 180))
            sub = font.render("Nhấn SPACE để bắt đầu | ← → di chuyển", True, (255, 255, 255))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 280))
            hs = font.render(f"Kỷ lục: {self.high_score}", True, (255, 255, 200))
            screen.blit(hs, (WIDTH // 2 - hs.get_width() // 2, 330))
            return

        pygame.draw.rect(screen, PLAYER_COLOR, self.player, border_radius=10)
        pygame.draw.circle(screen, (255, 255, 255), (self.player.centerx, self.player.top + 15), 12)
        for star in self.stars:
            pygame.draw.circle(screen, STAR_COLOR, star.center, STAR_SIZE // 2)
        for rock in self.rocks:
            pygame.draw.rect(screen, ROCK_COLOR, rock, border_radius=5)

        screen.blit(font.render(f"Điểm: {self.score}  Level: {self.level}", True, (255, 255, 255)), (20, 20))
        screen.blit(font.render(f"{'❤️' * self.lives}", True, (255, 100, 100)), (20, 50))

        if self.state == "gameover":
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))
            msg = title_font.render("Game Over!", True, (255, 100, 100))
            screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - 80))
            sub = font.render(f"Điểm: {self.score} | Kỷ lục: {self.high_score}", True, (255, 255, 255))
            screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, HEIGHT // 2))
            sub2 = font.render("R: Chơi lại | ESC: Menu", True, (200, 200, 200))
            screen.blit(sub2, (WIDTH // 2 - sub2.get_width() // 2, HEIGHT // 2 + 40))


game = Game()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game.state = "menu"
            elif event.key == pygame.K_SPACE and game.state == "menu":
                game.start()
            elif event.key == pygame.K_r and game.state == "gameover":
                game.start()

    game.update(pygame.key.get_pressed())
    game.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
