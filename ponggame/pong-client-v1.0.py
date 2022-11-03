import sys
import pygame
import socket
import pickle

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
        self.host = '127.0.0.1'
        self.port = 5555
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

class Paddle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 5

    def draw(self, screen):
        rect = pygame.Rect(self.rect)
        rect.center = (self.x, self.y)
        pygame.draw.rect(screen, self.color, rect)
  
    def move(self):

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(screen, paddleA, paddleB):
    screen.fill(white)
    paddleA.draw(screen)
    paddleB.draw(screen)
    pygame.display.update()

def mainLoop():

    run = True
    playersConnected = False

    paddleA = Paddle(width - width/10, height/2, 20, 100, black)
    paddleB = Paddle(width/10, height/2, 20, 100, black)

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

        redrawWindow(screen, paddleA, paddleB)

    pygame.quit
    sys.exit

mainLoop()