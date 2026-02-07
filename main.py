import pygame
import random
from agent import snkagent
import threading

pygame.init()
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Snake game")
t2 = threading.Thread(target=snkagent, args=(("Introduce yourself " ,10,0,(45,55),(100,200))))
t2.start()

# sounds
# load bg music
pygame.mixer.music.load(r'Sounds\bg.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1,0.0)
# load sound
eating_effect = pygame.mixer.Sound(r'Sounds\eating.mp3')
hiss_effect = pygame.mixer.Sound(r'Sounds\hiss-effect.mp3')
game_over_effect = pygame.mixer.Sound(r'Sounds\game_over.mp3')

# image
bg_img = pygame.image.load(r"Image\bg-img.jpg")
background = pygame.transform.scale(bg_img, (screen_width, screen_height))
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
    speed = 2
    snake_x = 45
    snake_y = 55
    velocity_x =speed
    velocity_y =0
    velocity_dir ="r"
    snake_size = 12

    # food
    food_x=random.randint(20,880)
    food_y=random.randint(20,580)

    # fps and clock
    fps = 90
    clock = pygame.time.Clock()

    # snake length
    snk_list = []
    snk_length = 10

    
    def snake_ai(evt,percent):
        if random.random()<(percent/100):
            t2 = threading.Thread(target=snkagent, args=((evt,len(snk_list),score,(snake_x,snake_y),(food_x,food_y))))
            t2.start()


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
                if event.key == pygame.K_SPACE:
                    game_over=False
                    pygame.mixer.music.play()
                    game_loop()
        else:
            screen.fill(bg)
            # screen.blit(background,(0,0))
            text(f"Score: {score}",black,40,20,20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                # movement
                keys = pygame.key.get_pressed()
                # sprint
                if keys[pygame.K_SPACE] and len(snk_list)>=11:
                    
                    if velocity_dir=='u':
                        hiss_effect.play()
                        snake_ai("Snake started sprinting",10)
                        velocity_y =-2*speed
                        velocity_x =0
                        snk_length = max(10,snk_length-1)
                    if velocity_dir=='d':
                        hiss_effect.play()
                        snake_ai("Snake started sprinting",10)
                        velocity_y =2*speed
                        velocity_x =0
                        snk_length = max(10,snk_length-1)
                    if velocity_dir=='l':
                        hiss_effect.play()
                        snake_ai("Snake started sprinting",10)
                        velocity_y =0
                        velocity_x =-2*speed
                        snk_length = max(10,snk_length-1)
                    if velocity_dir=='r':
                        hiss_effect.play()
                        snake_ai("Snake started sprinting",10)
                        velocity_y =0
                        velocity_x =2*speed
                        snk_length = max(10,snk_length-1)
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
                # normal
                if keys[pygame.K_w]:
                    if velocity_dir =='d':
                        pass
                    else:
                        velocity_y =-speed
                        velocity_x =0
                        velocity_dir='u'
                if keys[pygame.K_s]:
                    if velocity_dir =='u':
                        pass
                    else:
                        velocity_y =speed
                        velocity_x =0
                        velocity_dir='d'
                if keys[pygame.K_a]:
                    if velocity_dir =='r':
                        pass
                    else:
                        velocity_y =0
                        velocity_x =-speed
                        velocity_dir='l'
                if keys[pygame.K_d]:
                    if velocity_dir =='l':
                        pass
                    else:
                        velocity_y =0
                        velocity_x =speed
                        velocity_dir='r'
                
            # position increment
            snake_x+=velocity_x    
            snake_y+=velocity_y 
            # len of snake
            # print(len(snk_list))

            # food collision
            if abs(snake_x-food_x)<11 and abs(snake_y-food_y)<11:
                eating_effect.play()
                score +=10
                food_x=random.randint(20,880)
                food_y=random.randint(20,580)
                snk_length+=8
                snake_ai(" Snake ate food",22)        
            # snake length increment
            snk_list.append([snake_x,snake_y])
            
            # snake length decrement
            if len(snk_list)>snk_length:
                snk_list = snk_list[-snk_length:]

            # snake collide itself condition
            if [snake_x,snake_y] in snk_list[:-1]:
                game_over_effect.play()
                pygame.mixer.music.pause()
                snake_ai("Game over, Reason : Snake ate itself due to the user",100)
                game_over =True
            # snake collide outside the boundary 
            if snake_x< 0 or snake_x > screen_width or snake_y<0 or snake_y>screen_height :
                game_over_effect.play()
                pygame.mixer.music.pause()
                snake_ai("Game over, Reason: Snake goes outside the boundary due to the user",100)
                game_over =True

            # plot snake
            plot_snake(screen,black,snk_list,snake_size)
            # plot food
            pygame.draw.circle(screen,red,[food_x,food_y],6)
    
        pygame.display.update()
        clock.tick(fps)
game_loop()
pygame.quit()