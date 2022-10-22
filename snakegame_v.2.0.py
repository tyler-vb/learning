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
width = 500
length = 500

# snake speed
snake_speed = 8
max_snake_speed = 15

# create game window
dis = pygame.display.set_mode((width, length))
pygame.display.set_caption("snake by Tyler Buffa")

# initialize snake parameters
block_size = 25
x1 = width/2
y1 = length/2
x2 = random.randrange(0, width, block_size)
y2 = random.randrange(0, length, block_size)
x1_change = 0
y1_change = 0
segment_list = []
snake_length = 1

# initialize clock
clock = pygame.time.Clock()

# function to draw out each piece of snake
def snake(segment_list, segment_size):
    for x in segment_list:
        pygame.draw.rect(dis, black, [x[0], x[1], segment_size, segment_size])

game_over = False

while not game_over:

    # get keystrokes
    for event in pygame.event.get():
        print(event)

        # close window if press close button
        if event.type == pygame.QUIT:
            game_over = True

        # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x1_change == 0:
                x1_change = -block_size
                y1_change = 0
            elif event.key == pygame.K_RIGHT and x1_change == 0:
                x1_change = block_size
                y1_change = 0
            elif event.key == pygame.K_DOWN and y1_change == 0:
                x1_change = 0
                y1_change = block_size
            elif event.key == pygame.K_UP and y1_change == 0:
                x1_change = 0
                y1_change = -block_size

    # update snake head position

    print('test')

    x1 += x1_change
    y1 += y1_change

    print(x1_change, y1_change)


    # add snake segment and increase snake speed if snake eats food

    if x1 == x2 and y1 == y2:
        on_snake = True
        while on_snake:
            x2 = random.randrange(0, width, block_size)
            y2 = random.randrange(0, length, block_size)
            if [x2, y2] not in segment_list:
                on_snake = False
        if snake_speed < max_snake_speed:
            snake_speed += 0.5
        snake_length += 1

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

    # gameover if snake crosses self
    if [x1, y1] in segment_list[:-1]:
        game_over = True

    # gameover if snake crosses boundry
    if x1 >= width or x1 <= 0 or y1 >= length or y1 <= 0:   
        game_over = True

    # update the screen
    pygame.display.update()

    clock.tick(20)

pygame.quit()
sys.exit()


