# import modules
import pygame
import sys
import random
import json

# initialize pygame
pygame.init()

# color pallette
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# fonts
game_font = pygame.font.SysFont('Comic Sans MS', 30)
    
# size of window
width = 500
length = 500

# snake speed
max_snake_speed = 18

# create game window
dis = pygame.display.set_mode((width, length))
pygame.display.set_caption("snake by Tyler Buffa")

# initialize snake parameters
block_size = 25

# initialize clock
clock = pygame.time.Clock()

# function to draw out each piece of snake
def snake(segment_list, segment_size):
    for x in segment_list:
        pygame.draw.rect(dis, black, [x[0], x[1], segment_size, segment_size])

def retry_screen():
        dis.fill(red)
        text = game_font.render('Press C to Retry or Q to Quit', 1, white)
        text_rect = text.get_rect(center = (width/2, length/2))
        dis.blit(text, text_rect)


def score(a, b):
        text = game_font.render(('score: ' + str(a) + ' | high score: ' + str(b)), 1, blue)
        text_rect = text.get_rect(center = (width/2, length/10))
        dis.blit(text, text_rect)

def game_loop():
    
    game_over = False
    game_close = False

    x1 = width/2
    y1 = length/2
    x2 = random.randrange(0, width, block_size)
    y2 = random.randrange(0, length, block_size)
    x1_change = 0
    y1_change = 0
    segment_list = []
    snake_length = 1
    snake_speed = 10

    with open(r'C:\Users\tyler\Documents\learning\snakegame\snake.json', 'r') as openfile:
        json_data = json.load(openfile)

    high_score = json_data['highscore']

    while not game_close:

        if high_score < snake_length - 1:

            high_score += 1

            json_data['highscore'] = high_score
            with open('snake.json', 'w') as outfile:
                json.dump(json_data, outfile)

        keystroke = False

        while game_over == True:
                retry_screen()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = False
                        game_close = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = False
                            game_close = True
                        elif event.key == pygame.K_c:
                            game_over = False
                            game_loop()


        # get keystrokes
        for event in pygame.event.get():
            print(event)

            # close window if press close button
            if event.type == pygame.QUIT:
                game_close = True

            # player movement
            if event.type == pygame.KEYDOWN and keystroke == False:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -block_size
                    y1_change = 0
                    keystroke = True
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = block_size
                    y1_change = 0
                    keystroke = True
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = block_size
                    keystroke = True
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -block_size
                    keystroke = True

        # update snake head position
        x1 += x1_change
        y1 += y1_change

        # add snake segment and increase snake speed if snake eats food
        if x1 == x2 and y1 == y2:
            on_snake = True
            while on_snake:
                x2 = random.randrange(0, width, block_size)
                y2 = random.randrange(0, length, block_size)
                if [x2, y2] not in segment_list:
                    on_snake = False
            if snake_speed < max_snake_speed:
                snake_speed += 1
            snake_length += 1

        # clear the game space
        dis.fill(white)

        # update snake list with new head position
        segment_list.append([x1, y1])

        # remove old parts of snake from snake list
        if len(segment_list) > snake_length:
            del segment_list[0]

        # draw out snake
        snake(segment_list, block_size)

        # draw out food
        pygame.draw.rect(dis, red, [x2, y2, block_size, block_size])

        # score
        score(snake_length - 1, high_score)

        # gameover if snake crosses self
        if [x1, y1] in segment_list[:-1]:
            game_over = True

        # gameover if snake crosses boundry
        if x1 >= width or x1 <= 0 or y1 >= length or y1 <= 0:   
            game_over = True
        
        # update the screen
        pygame.display.update()

        clock.tick(snake_speed)
        
    pygame.quit()
    sys.exit()

game_loop()



