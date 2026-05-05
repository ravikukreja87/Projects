import pygame


pygame.init()


SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
COLOR_BLUE = (0, 102, 204)
COLOR_ORANGE = (255, 165, 0)
COLOR_WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Sprites & Movement")


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change


player = Sprite(COLOR_BLUE, 50, 50, 100, 100)

static_block = Sprite(COLOR_ORANGE, 50, 50, 300, 300)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(static_block)


running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]:
        player.move(5, 0)
    if keys[pygame.K_UP]:
        player.move(0, -5)
    if keys[pygame.K_DOWN]:
        player.move(0, 5)

   
    screen.fill(COLOR_WHITE)  
    all_sprites.draw(screen)  
    
    pygame.display.flip()

   
    clock.tick(60)

pygame.quit()
