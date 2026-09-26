import pygame

from settings import (
    WIDTH,
    HEIGHT,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
    PLAYER_SPEED,
    PLAYER_LIVES,
    PLAYER_INVULNERABILITY_TIME,
)


class Player:

    def __init__(self):
        self.rect = pygame.Rect(
            (WIDTH - PLAYER_WIDTH) // 2,
            HEIGHT - PLAYER_HEIGHT - 20,
            PLAYER_WIDTH,
            PLAYER_HEIGHT,
        )

        self.lives = PLAYER_LIVES
        self.invulnerable_until = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def take_damage(self, current_time):
        if current_time < self.invulnerable_until:
            return False

        self.lives -= 1

        self.invulnerable_until = current_time + PLAYER_INVULNERABILITY_TIME

        return True

    def draw(self, screen):

        current_time = pygame.time.get_ticks()

        # Parpadea mientras está invulnerable
        if current_time < self.invulnerable_until:

            if (current_time // 100) % 2 == 0:
                return

        pygame.draw.rect(
            screen,
            (50, 150, 255),
            self.rect,
        )
