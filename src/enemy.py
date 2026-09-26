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
    ENEMY_SHOOT_INTERVAL,
)


class Enemy:

    def __init__(self, x, y):
        self.rect = pygame.Rect(
            x,
            y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
        )

        # Current logical position inside the formation
        self.formation_x = x
        self.formation_y = y

        # Attack state
        self.attacking = False
        self.returning = False

        # Position where the current attack started
        self.attack_start_y = y

    def start_attack(self):
        self.attacking = True
        self.returning = False

        self.attack_start_y = self.rect.y

    def update_attack(self):

        if self.attacking:

            self.rect.y += 3

            if self.rect.y >= self.attack_start_y + 180:
                self.attacking = False
                self.returning = True

        elif self.returning:

            self._return_to_formation()

    def _return_to_formation(self):

        return_speed = 4

        # Move toward current formation X
        if self.rect.x < self.formation_x:
            self.rect.x += return_speed

        elif self.rect.x > self.formation_x:
            self.rect.x -= return_speed

        # Move toward current formation Y
        if self.rect.y < self.formation_y:
            self.rect.y += return_speed

        elif self.rect.y > self.formation_y:
            self.rect.y -= return_speed

        # Check if the enemy reached the formation
        if (
            abs(self.rect.x - self.formation_x) <= return_speed
            and abs(self.rect.y - self.formation_y) <= return_speed
        ):
            self.rect.x = self.formation_x
            self.rect.y = self.formation_y

            self.returning = False

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

                # Temporary attack test
                if row == 0 and column == 2:
                    enemy.start_attack()

    def update(self):

        for enemy in self.enemies:

            # Keep the logical formation position moving.
            enemy.formation_x += ENEMY_SPEED * self.direction

            if enemy.attacking or enemy.returning:
                enemy.update_attack()

            else:
                # Normal enemies follow the formation.
                enemy.rect.x = enemy.formation_x

        self._check_edges()

    def _check_edges(self):

        active_enemies = [
            enemy
            for enemy in self.enemies
            if not enemy.attacking and not enemy.returning
        ]

        if not active_enemies:
            return

        formation_left = min(
            enemy.formation_x
            for enemy in active_enemies
        )

        formation_right = max(
            enemy.formation_x + ENEMY_WIDTH
            for enemy in active_enemies
        )

        if formation_right >= WIDTH:

            self.direction = -1

            for enemy in self.enemies:

                enemy.formation_x = min(
                    enemy.formation_x,
                    WIDTH - ENEMY_WIDTH,
                )

                enemy.formation_y += ENEMY_DROP

                if not enemy.attacking and not enemy.returning:
                    enemy.rect.x = enemy.formation_x
                    enemy.rect.y = enemy.formation_y

        elif formation_left <= 0:

            self.direction = 1

            for enemy in self.enemies:

                enemy.formation_x = max(
                    enemy.formation_x,
                    0,
                )

                enemy.formation_y += ENEMY_DROP

                if not enemy.attacking and not enemy.returning:
                    enemy.rect.x = enemy.formation_x
                    enemy.rect.y = enemy.formation_y

    def shoot(self):

        self.shoot_timer += 1

        if self.shoot_timer < ENEMY_SHOOT_INTERVAL:
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

    def draw(self, screen):

        for enemy in self.enemies:
            enemy.draw(screen)