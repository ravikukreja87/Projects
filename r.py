import pygame


pygame.init()


screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My first game screen")


BG_COLOR = (0, 0, 0)
RECT_COLOR = (0, 128, 255) 


rect_w, rect_h = 120, 120
center_x = (screen_width // 2) - (rect_w // 2)
center_y = (screen_height // 2) - (rect_h // 2)
central_rect = pygame.Rect(center_x, center_y, rect_w, rect_h)


font = pygame.font.SysFont("Verdana", 28)
text_surface = font.render("Pygame is running!", True, (255, 255, 255))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BG_COLOR)
    
    
    pygame.draw.rect(screen, RECT_COLOR, central_rect)
    

    screen.blit(text_surface, (20, 20))
    
    pygame.display.flip()

pygame.quit()