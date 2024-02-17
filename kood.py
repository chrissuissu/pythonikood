import pygame

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("jkPf")
# load background image
bg_image = pygame.image.load('assets/background.jpg').convert_alpha()


class Background(pygame.sprite.Sprite):
    def init(self, image_file, location):
        pygame.sprite.Sprite.init(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


# function for drawing background
def draw_bg():
    screen.blit(bg_image, (0, 0))


# game loop
run = True
while run:
    # draw background
    draw_bg()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # uptade display
    pygame.display.update()


def draw_bg():
    pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


screen.blit(bg_image, (0, 0))

run = True
while run:
    # draw background
    def draw_bg():
        screen.blit(bg_image, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.display.update()

pygame.display.update()

pygame.quit()
