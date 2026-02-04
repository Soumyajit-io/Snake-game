import pygame
pygame.init()
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")

# colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# game variable
running = True
game_over = False

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 
    screen.fill(white)
    pygame.display.update()
pygame.quit()