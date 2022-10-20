# import modules
import pygame
import sys

# initialize pygame
pygame.init()

# color pallette
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# size of window
width = 600
length = 600

# FPS
fps = 10

# create game window
dis = pygame.display.set_mode((width, length))
pygame.display.set_caption("snake by Tyler Buffa")

# initialize snake parameters
xsnake = 300
ysnake = 300
xsnakechange = 0
ysnakechange = 0

# speed of the game
clock = pygame.time.Clock()

game_over = False

while not game_over:

    # gameover if snake crosses boundry
    if xsnake >= width or xsnake <= 0 or ysnake >= length or ysnake <= 0:   
        game_over = True

    # get keystrokes
    for event in pygame.event.get():
        print(event)

        # close window if press close button
        if event.type == pygame.QUIT:
            game_over = True

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xsnakechange = -10
                ysnakechange = 0
            elif event.key == pygame.K_RIGHT:
                xsnakechange = 10
                ysnakechange = 0
            elif event.key == pygame.K_DOWN:
                xsnakechange = 0
                ysnakechange = 10
            elif event.key == pygame.K_UP:
                xsnakechange = 0
                ysnakechange = -10
    
    print(xsnake,ysnake)

    xsnake += xsnakechange
    ysnake += ysnakechange

    dis.fill((white))

    # draw out snake segment
    pygame.draw.rect(dis, black, [xsnake, ysnake, 10, 10])

    # update the screen
    pygame.display.update()

    clock.tick(fps)

pygame.quit()
sys.exit()


def snake(segements):
    for x in segements:
        pygame.draw.rect(dis, black, [x[0], x[1], 10, 10])




    