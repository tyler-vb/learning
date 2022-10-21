# import modules
import pygame
import sys
import random

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
block_size = 10
x1 = 300
y1 = 300
x2 = random.randrange(0, width, block_size)
y2 = random.randrange(0, length, block_size)
x1_change = 0
y1_change = 0
segment_list = []
snake_length = 1

# speed of the game
clock = pygame.time.Clock()

# function to draw out each piece of snake
def snake(segment_list, segment_size):
    for x in segment_list:
        pygame.draw.rect(dis, black, [x[0], x[1], segment_size, segment_size])

game_over = False

while not game_over:

    # gameover if snake crosses boundry
    if x1 >= width or x1 <= 0 or y1 >= length or y1 <= 0:   
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
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = block_size
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -block_size

    # update snake head position
    x1 += x1_change
    y1 += y1_change

    if x1 == x2 and y1 == y2:
        x2 = random.randrange(0, width, block_size)
        y2 = random.randrange(0, length, block_size)
        snake_length += 1


    snake_head = [x1, y1]

    # clear the game space
    dis.fill((white))

    # update snake list with new head position
    segment_list.append([x1, y1])

    # remove old parts of snake from snake list
    if len(segment_list) > snake_length:
        del segment_list[0]

    # draw out snake
    snake(segment_list, block_size)

    # draw out food
    pygame.draw.rect(dis, red, [x2, y2, block_size, block_size])


    print('snake', x1, y1)
    print('food', x2, y2)
    # update the screen
    pygame.display.update()

    clock.tick(fps)

pygame.quit()
sys.exit()


