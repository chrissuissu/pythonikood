import pygame
from fighters import Fighter  # Assuming Fighter class is defined in fighters.py

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("jkPf")

# Load background image
bg_image = pygame.image.load('assets/background.jpg').convert_alpha()

# Load sprite sheet for the fighter
sprite_sheet = pygame.image.load("assets/melee.png").convert_alpha()

# Create an instance of the Fighter class
player1 = Fighter(1, 100, 500, False, (80, 2, (0, 0)), sprite_sheet,
                  [4, 4, 4, 4, 4, 4, 4], None)  # Assuming sound is not provided

# Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player1.update()  # Update player state

    screen.blit(bg_image, (0, 0))  # Draw background
    screen.blit(player1.image, (player1.rect.x, player1.rect.y))  # Draw player

    pygame.display.update()

pygame.quit()
