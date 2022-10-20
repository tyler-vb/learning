# import modules
from curses import KEY_DOWN, KEY_LEFT
import pygame
import sys

# initialize pygame
pygame.init()

# color pallette
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# create game window
dis = pygame.display.set_mode((600, 600))
pygame.display.set_caption("snake by Tyler Buffa")
dis.fill((white))

#initialize position of snake
x1 = 0
y1 = 0


game_over = False

while not game_over:
    # get keystrokes
    for event in pygame.event.get():
        print(event)
        # close window if press close button
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.type = pygame.KEY_LEFT
                x1

    # draw out snake segment
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        
    pygame.display.update()

pygame.quit()
sys.exit()
