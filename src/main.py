import pygame

from player import Player
from enemy import EnemyFormation
from bullet import Bullet

from settings import (
    WIDTH,
    HEIGHT,
    FPS,
    PLAYER_ZONE_HEIGHT,
    BULLET_WIDTH,
    BULLET_HEIGHT,
    BULLET_SPEED,
    ENEMY_SCORE,
    ENEMIES_DEFEATED_MESSAGE,
    GAME_OVER_MESSAGE,
)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Assault")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
victory_font = pygame.font.Font(None, 64)
game_over_font = pygame.font.Font(None, 72)

player = Player()

bullets = []
enemy_bullets = []

score = 0
victory = False
game_over = False

formation = EnemyFormation()
running = True

while running:

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and not victory and not game_over:
                bullet = Bullet(
                    player.rect.centerx - BULLET_WIDTH // 2,
                    player.rect.top - BULLET_HEIGHT,
                    BULLET_WIDTH,
                    BULLET_HEIGHT,
                    -BULLET_SPEED,
                )

                bullets.append(bullet)

    # -------------------------
    # Game updates
    # -------------------------

    if not victory and not game_over:

        # -------------------------
        # Player movement
        # -------------------------

        player.update()

        # -------------------------
        # Enemy formation movement
        # -------------------------

        formation.update()

        # -------------------------
        # Enemy shooting
        # -------------------------

        enemy_bullet = formation.shoot()

        if enemy_bullet is not None:
            enemy_bullets.append(enemy_bullet)

        # -------------------------
        # Bullet movement
        # -------------------------

        for bullet in bullets:
            bullet.update()

        for bullet in enemy_bullets:
            bullet.update()

        bullets = [
            bullet for bullet in bullets
            if not bullet.is_off_screen(HEIGHT)
        ]

        enemy_bullets = [
            bullet for bullet in enemy_bullets
            if not bullet.is_off_screen(HEIGHT)
        ]

        # -------------------------
        # Bullet-enemy collisions
        # -------------------------

        bullets_to_remove = []
        enemies_to_remove = []

        current_time = pygame.time.get_ticks()

        for bullet in bullets:
            for enemy in formation.enemies:

                if bullet.rect.colliderect(enemy.rect):
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)

                    score += ENEMY_SCORE

                    break

        # -------------------------
        # Enemy bullet-player collisions
        # -------------------------

        enemy_bullets_to_remove = []

        if current_time >= player.invulnerable_until:
            for bullet in enemy_bullets:

                if bullet.rect.colliderect(player.rect):
                    enemy_bullets_to_remove.append(bullet)

                    player.take_damage(current_time)

                    if player.lives <= 0:
                        game_over = True

                    break

        # -------------------------
        # Remove bullets
        # -------------------------

        for bullet in bullets_to_remove:
            if bullet in bullets:
                bullets.remove(bullet)

        for bullet in enemy_bullets_to_remove:
            if bullet in enemy_bullets:
                enemy_bullets.remove(bullet)

        # -------------------------
        # Remove enemies
        # -------------------------

        for enemy in enemies_to_remove:
            if enemy in formation.enemies:
                formation.enemies.remove(enemy)

        # -------------------------
        # Victory condition
        # -------------------------

        if not formation.enemies:
            victory = True

        # -------------------------
        # Game over condition
        # -------------------------

        if formation.enemies:
            for enemy in formation.enemies:

                if enemy.rect.bottom >= HEIGHT - PLAYER_ZONE_HEIGHT:
                    game_over = True
                    break

    # -------------------------
    # Drawing
    # -------------------------

    screen.fill((10, 10, 30))

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen, (255, 255, 255))

    for bullet in enemy_bullets:
        bullet.draw(screen, (255, 100, 100))

    formation.draw(screen)

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    lives_text = font.render(
        f"Lives: {player.lives}",
        True,
        (255, 255, 255),
    )

    screen.blit(lives_text, (20, 50))
    screen.blit(score_text, (20, 20))

    # -------------------------
    # Victory message
    # -------------------------

    if victory:
        victory_text = victory_font.render(
            ENEMIES_DEFEATED_MESSAGE,
            True,
            (255, 255, 255),
        )

        victory_rect = victory_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(victory_text, victory_rect)

    # -------------------------
    # Game over message
    # -------------------------

    if game_over:
        game_over_text = game_over_font.render(
            GAME_OVER_MESSAGE,
            True,
            (255, 255, 255),
        )

        game_over_rect = game_over_text.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(game_over_text, game_over_rect)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()