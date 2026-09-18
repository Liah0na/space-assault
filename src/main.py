import pygame


WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
PLAYER_SPEED = 5


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(".:[Space Assault]:.")

clock = pygame.time.Clock()

player = pygame.Rect(
    (WIDTH - PLAYER_WIDTH) // 2,
    HEIGHT - PLAYER_HEIGHT - 20,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    screen.fill((10, 10, 30))

    pygame.draw.rect(screen, (50, 150, 255), player)

    pygame.display.flip()

    clock.tick(FPS)


pygame.quit()