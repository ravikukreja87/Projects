import pygame


pygame.init()


width, height = 500, 500
screen = pygame.display.set_mode((width, height))


pygame.display.set_caption("My first game screen")


BG_COLOR = (58, 58, 58)


image_ready = False
try:
    
    img = pygame.image.load('image.png')
    img = pygame.transform.scale(img, (300, 300))
    
    
    img_rect = img.get_rect(center=(width // 2, height // 2))
    image_ready = True
except:
    print("No image found. Displaying background only.")


running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            running = False

   
    screen.fill(BG_COLOR)

    if image_ready:
        screen.blit(img, img_rect)

    
    pygame.display.flip()

pygame.quit()