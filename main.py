import pygame
import random

pygame.init()
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")

# colors
bg = (50, 205, 50)
red = (255,0,0)
black = (0,0,0)

# utility functions
def text(text,color,size,x,y):
    font = pygame.font.SysFont(None,size)
    txt = font.render(text,True,color)
    screen.blit(txt,[x,y])
def plot_snake(screen,black,snake_list,snake_size):
    for x , y in snake_list:
        pygame.draw.rect(screen,black,[x,y,snake_size,snake_size])


# game loop
def game_loop():
    # game variable
    score =0
    running = True
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x =0
    velocity_y =0
    velocity_dir ="r"
    speed = 2
    snake_size = 12
    # food
    food_x=random.randint(20,880)
    food_y=random.randint(20,580)

    # fps and clock
    fps = 90
    clock = pygame.time.Clock()

    # snake length
    snk_list = []
    snk_length = 1

    while running:
        if game_over:
            screen.fill("red")
            text("Game over! Press Enter to continue","black",60,100,270)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_over=False
                    game_loop()
        else:
            screen.fill(bg)
            text(f"Score: {score}",black,40,20,20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                # movement
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    if velocity_dir=='u':
                        velocity_y =-2*speed
                        velocity_x =0
                    if velocity_dir=='d':
                        velocity_y =2*speed
                        velocity_x =0
                    if velocity_dir=='l':
                        velocity_y =0
                        velocity_x =-2*speed
                    if velocity_dir=='r':
                        velocity_y =0
                        velocity_x =2*speed
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if velocity_dir=='u':
                            velocity_y =-speed
                            velocity_x =0
                        if velocity_dir=='d':
                            velocity_y =speed
                            velocity_x =0
                        if velocity_dir=='l':
                            velocity_y =0
                            velocity_x =-speed
                        if velocity_dir=='r':
                            velocity_y =0
                            velocity_x =speed
                    
                if keys[pygame.K_w]:
                    velocity_y =-speed
                    velocity_x =0
                    velocity_dir='u'
                if keys[pygame.K_s]:
                    velocity_y =speed
                    velocity_x =0
                    velocity_dir='d'
                if keys[pygame.K_a]:
                    velocity_y =0
                    velocity_x =-speed
                    velocity_dir='l'
                if keys[pygame.K_d]:
                    velocity_y =0
                    velocity_x =speed
                    velocity_dir='r'
                

            snake_x+=velocity_x    
            snake_y+=velocity_y 

            if abs(snake_x-food_x)<11 and abs(snake_y-food_y)<11:
                score +=10
                food_x=random.randint(20,880)
                food_y=random.randint(20,580)
                snk_length+=5
            print("append ",[snake_x,snake_y])
            snk_list.append([snake_x,snake_y])
            print(snk_list)
            if len(snk_list)>snk_length:
                print("deleted",snk_list[0])
                del snk_list[0]
            if [snake_x,snake_y] in snk_list[:-1]:
                game_over =True

            if snake_x< 0 or snake_x > screen_width or snake_y<0 or snake_y>screen_height :
                game_over =True



            plot_snake(screen,black,snk_list,snake_size)
            
            
            pygame.draw.circle(screen,red,[food_x,food_y],6)
    
        pygame.display.update()
        clock.tick(fps)
game_loop()
pygame.quit()