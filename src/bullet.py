import pygame

class Bullet:

    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(
            x,
            y,
            width,
            height,
        )

        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def is_off_screen(self, height):
        return self.rect.bottom < 0 or self.rect.top > height

    def draw(self, screen, color):
        pygame.draw.rect(
            screen,
            color,
            self.rect,
        )