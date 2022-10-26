import sys
import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

width = 600
height = 600

x1 = 0

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pong? by Tyler Buffa')

clock = pygame.time.Clock()

game_close = False

while not game_close:

    screen.fill(red)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True

    if keys[pygame.K_LEFT]:
        x1 -= 10
    if keys[pygame.K_RIGHT]:
        x1 += 10

    pygame.draw.rect(screen, black, [x1, 400, 50, 10])

    screen.fill(white)

    clock.tick(60)

    pygame.display.update

pygame.quit
sys.exit

