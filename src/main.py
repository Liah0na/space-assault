import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
PLAYER_SPEED = 5

PLAYER_ZONE_HEIGHT = 80

BULLET_WIDTH = 4
BULLET_HEIGHT = 12
BULLET_SPEED = 8

ENEMY_WIDTH = 40
ENEMY_HEIGHT = 25
ENEMY_HORIZONTAL_GAP = 20
ENEMY_VERTICAL_GAP = 20
ENEMY_ROWS = 3
ENEMY_COLUMNS = 5

ENEMY_SCORE = 100

ENEMY_SPEED = 2
ENEMY_DROP = 20

ENEMIES_DEFEATED_MESSAGE = "Enemies Defeated!"

GAME_OVER_MESSAGE = "GAME OVER"

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Assault")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 32)
victory_font = pygame.font.Font(None, 64)
game_over_font = pygame.font.Font(None, 72)

player = pygame.Rect(
    (WIDTH - PLAYER_WIDTH) // 2,
    HEIGHT - PLAYER_HEIGHT - 20,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)

bullets = []
enemies = []

score = 0
enemy_direction = 1
victory = False
game_over = False

formation_width = (
    ENEMY_COLUMNS * ENEMY_WIDTH
    + (ENEMY_COLUMNS - 1) * ENEMY_HORIZONTAL_GAP
)

formation_start_x = (WIDTH - formation_width) // 2
formation_start_y = 80

for row in range(ENEMY_ROWS):
    for column in range(ENEMY_COLUMNS):
        enemy_x = formation_start_x + column * (
            ENEMY_WIDTH + ENEMY_HORIZONTAL_GAP
        )

        enemy_y = formation_start_y + row * (
            ENEMY_HEIGHT + ENEMY_VERTICAL_GAP
        )

        enemy = pygame.Rect(
            enemy_x,
            enemy_y,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
        )

        enemies.append(enemy)

running = True

while running:

    # -------------------------
    # Events
    # -------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if (
                event.key == pygame.K_SPACE
                and not victory
                and not game_over
            ):
                bullet = pygame.Rect(
                    player.centerx - BULLET_WIDTH // 2,
                    player.top - BULLET_HEIGHT,
                    BULLET_WIDTH,
                    BULLET_HEIGHT,
                )

                bullets.append(bullet)

    # -------------------------
    # Game updates
    # -------------------------

    if not victory and not game_over:

        # -------------------------
        # Player movement
        # -------------------------

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player.x -= PLAYER_SPEED

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player.x += PLAYER_SPEED

        if player.left < 0:
            player.left = 0

        if player.right > WIDTH:
            player.right = WIDTH

        # -------------------------
        # Bullet movement
        # -------------------------

        for bullet in bullets:
            bullet.y -= BULLET_SPEED

        bullets = [
            bullet
            for bullet in bullets
            if bullet.bottom > 0
        ]

        # -------------------------
        # Enemy movement
        # -------------------------

        for enemy in enemies:
            enemy.x += ENEMY_SPEED * enemy_direction

        if enemies:
            formation_left = min(
                enemy.left for enemy in enemies
            )

            formation_right = max(
                enemy.right for enemy in enemies
            )

            if formation_right >= WIDTH:
                enemy_direction = -1

                for enemy in enemies:
                    enemy.right = min(enemy.right, WIDTH)
                    enemy.y += ENEMY_DROP

            elif formation_left <= 0:
                enemy_direction = 1

                for enemy in enemies:
                    enemy.left = max(enemy.left, 0)
                    enemy.y += ENEMY_DROP

        # -------------------------
        # Bullet-enemy collisions
        # -------------------------

        bullets_to_remove = []
        enemies_to_remove = []

        for bullet in bullets:
            for enemy in enemies:

                if bullet.colliderect(enemy):
                    bullets_to_remove.append(bullet)
                    enemies_to_remove.append(enemy)

                    score += ENEMY_SCORE

                    break

        for bullet in bullets_to_remove:
            if bullet in bullets:
                bullets.remove(bullet)

        for enemy in enemies_to_remove:
            if enemy in enemies:
                enemies.remove(enemy)

        # -------------------------
        # Victory condition
        # -------------------------

        if not enemies:
            victory = True

        # -------------------------
        # Game over condition
        # -------------------------

        if enemies:
            for enemy in enemies:

                if enemy.bottom >= HEIGHT - PLAYER_ZONE_HEIGHT:
                    game_over = True
                    break

    # -------------------------
    # Drawing
    # -------------------------

    screen.fill((10, 10, 30))

    pygame.draw.rect(
        screen,
        (50, 150, 255),
        player,
    )

    for bullet in bullets:
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            bullet,
        )

    for enemy in enemies:
        pygame.draw.rect(
            screen,
            (220, 70, 70),
            enemy,
        )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

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