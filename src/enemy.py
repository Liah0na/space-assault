import pygame

from bullet import Bullet
from settings import (
    WIDTH,
    ENEMY_WIDTH,
    ENEMY_HEIGHT,
    ENEMY_HORIZONTAL_GAP,
    ENEMY_VERTICAL_GAP,
    ENEMY_ROWS,
    ENEMY_COLUMNS,
    ENEMY_SPEED,
    ENEMY_DROP,
    ENEMY_BULLET_WIDTH,
    ENEMY_BULLET_HEIGHT,
    ENEMY_BULLET_SPEED,
)


class Enemy:

    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (220, 70, 70),
            self.rect,
        )


class EnemyFormation:

    def __init__(self):
      self.enemies = []
      self.direction = 1
      self.shoot_timer = 0

      self._create_formation()

    def _create_formation(self):
        formation_width = (
            ENEMY_COLUMNS * ENEMY_WIDTH
            + (ENEMY_COLUMNS - 1) * ENEMY_HORIZONTAL_GAP
        )

        formation_start_x = (WIDTH - formation_width) // 2
        formation_start_y = 80

        for row in range(ENEMY_ROWS):
            for column in range(ENEMY_COLUMNS):

                enemy_x = (
                    formation_start_x
                    + column * (ENEMY_WIDTH + ENEMY_HORIZONTAL_GAP)
                )

                enemy_y = (
                    formation_start_y
                    + row * (ENEMY_HEIGHT + ENEMY_VERTICAL_GAP)
                )

                enemy = Enemy(
                    enemy_x,
                    enemy_y,
                )

                self.enemies.append(enemy)

    def update(self):
        for enemy in self.enemies:
            enemy.rect.x += ENEMY_SPEED * self.direction

        self._check_edges()

    def _check_edges(self):
        if not self.enemies:
            return

        formation_left = min(
            enemy.rect.left
            for enemy in self.enemies
        )

        formation_right = max(
            enemy.rect.right
            for enemy in self.enemies
        )

        if formation_right >= WIDTH:
            self.direction = -1

            for enemy in self.enemies:
                enemy.rect.right = min(
                    enemy.rect.right,
                    WIDTH,
                )

                enemy.rect.y += ENEMY_DROP

        elif formation_left <= 0:
            self.direction = 1

            for enemy in self.enemies:
                enemy.rect.left = max(
                    enemy.rect.left,
                    0,
                )

                enemy.rect.y += ENEMY_DROP

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def shoot(self):
        self.shoot_timer += 1

        if self.shoot_timer < 60:
            return None

        self.shoot_timer = 0

        if not self.enemies:
            return None

        shooter = self.enemies[-1]

        bullet = Bullet(
            shooter.rect.centerx - ENEMY_BULLET_WIDTH // 2,
            shooter.rect.bottom,
            ENEMY_BULLET_WIDTH,
            ENEMY_BULLET_HEIGHT,
            ENEMY_BULLET_SPEED,
        )

        return bullet