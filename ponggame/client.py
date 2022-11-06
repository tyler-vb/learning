import sys
import pygame
from player import *
from network import *

pygame.init()

height = 768
width = 1366

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pong by Buffa Deez Nutz')

def redrawWindow(screen, paddleA, paddleB, ball):
    screen.fill(white)
    paddleA.draw(screen)
    paddleB.draw(screen)
    ball.draw(screen)
    pygame.display.update()

def mainLoop():

    run = True

    clock = pygame.time.Clock()

    n = Network()

    player = n.id[0]

    print(f'connected to {n.host}:{n.port}, running game as player {n.id[1] + 1}')
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit

        player.move(height)
        data = n.send(player)

        player2, ball = data[0], data[1]

        redrawWindow(screen, player, player2, ball)
    
    pygame.quit
    sys.exit

mainLoop()