import sys
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

width = 600
height = 600

paddle_width = 100
paddle_height = 10

ball_width = 20
ball_height = 20

paddle_x = width/2
paddle_y = height * 4/5

ball_xchange = 0
ball_ychange = 0

ball_speed = 5

paddle_speed = 10

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pong? by Tyler Buffa')

# create ball hit box
paddle_rect = pygame.Rect(0, 0, paddle_width, paddle_height)

# create paddle hit box
ball_rect = pygame.Rect(0, 0, ball_width, ball_height)

clock = pygame.time.Clock()

game_close = False
game_start = False

while not game_close:


    while not game_start:
        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

        if keys[pygame.K_LEFT] and paddle_x > paddle_width/2:
            paddle_x -= paddle_speed


        if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width/2:
            paddle_x += paddle_speed  

        if keys[pygame.K_SPACE]:
            ball_ychange = -ball_speed
            ball_xchange = 0
            game_start = True 

        ball_x = paddle_x
        ball_y = paddle_y - paddle_height/2 - ball_height/2

        screen.fill(white)

        # draw paddle
        paddle_rect.center = (paddle_x, paddle_y)
        pygame.draw.rect(screen, black, paddle_rect)

        # draw ball
        ball_rect.center = (ball_x, ball_y)
        pygame.draw.rect(screen, red, ball_rect)

        clock.tick(60)

        pygame.display.update()

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True

    if keys[pygame.K_LEFT] and paddle_x > paddle_width/2:
        paddle_x -= paddle_speed

    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width/2:
        paddle_x += paddle_speed

    # ball physics
    if pygame.Rect.colliderect(ball_rect, paddle_rect):
        ball_xchange = 2 * ball_speed * (ball_x - paddle_x)/paddle_width
        ball_ychange = -ball_speed - ball_speed*abs((ball_x - paddle_x)/paddle_width)
        
        if keys[pygame.K_LEFT]:
            ball_xchange = -abs(ball_xchange)

        if keys[pygame.K_RIGHT]:
            ball_xchange = abs(ball_xchange)


    if ball_rect.top <= 0:
        ball_ychange = -ball_ychange
        ball_xchange = ball_xchange
    
    elif ball_rect.left <= 0:
        ball_ychange = ball_ychange
        ball_xchange = -ball_xchange

    elif ball_rect.right >= width:
        ball_ychange = ball_ychange
        ball_xchange = -ball_xchange

    elif ball_rect.bottom >= height:
        game_start = False
        



    ball_y += ball_ychange

    ball_x += ball_xchange

    screen.fill(white)

    # draw paddle
    paddle_rect.center = (paddle_x, paddle_y)
    pygame.draw.rect(screen, black, paddle_rect)

    # draw ball
    ball_rect.center = (ball_x, ball_y)
    pygame.draw.rect(screen, red, ball_rect)
    
    clock.tick(60)

    pygame.display.update()

pygame.quit
sys.exit

