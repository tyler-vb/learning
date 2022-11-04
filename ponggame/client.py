import sys
import pygame
import socket
import pickle
from player import *

pygame.init()

height = 500
width = 500

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('pong by Buffa Deez Nutz')

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = '192.168.0.83'
        self.port = 9999
        self.id = self.connect()

    def connect(self):
        try:
            self.client.connect((self.host, self.port))
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


def redrawWindow(screen, paddleA, paddleB, ball):
    screen.fill(white)
    paddleA.draw(screen)
    paddleB.draw(screen)
    ball.draw(screen)
    pygame.display.update()

def mainLoop():

    run = True

    paddleA = Paddle(width - width/10, height/2, 20, 100, black)
    paddleB = Paddle(width/10, height/2, 20, 100, black)
    ball = Ball(width/2, height/2, 30, 30, black)

    clock = pygame.time.Clock()

    n = Network()
    player = n.id

    print(f'connected to {n.host}:{n.port}, running game as player {player + 1}')
    
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit

        if player == 0:
            paddleA.move()
            paddleB = n.send(paddleA)
        if player == 1:
            paddleB.move()
            paddleA = n.send(paddleB)

        ball.collide([paddleA.rect, paddleB.rect], height, width)

        redrawWindow(screen, paddleA, paddleB, ball)
    
    pygame.quit
    sys.exit

mainLoop()