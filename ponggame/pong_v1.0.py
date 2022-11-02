import sys
import pygame

pygame.init()

height = 500
width = 500

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption('pong by Buffa Deez Nutz')

clientNumber = 0

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

    paddleA = Paddle(width/10, height/2, 20, 100, black)
    paddleB = Paddle(width - width/10, height/2, 20, 100, black)

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit
        
        paddleA.move()
        paddleB.move()

        redrawWindow(screen, paddleA, paddleB)

    pygame.quit
    sys.exit

mainLoop()
            

