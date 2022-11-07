import pygame
import random
import math

class Paddle():
    def __init__(self, x, y, width, height, color, screenHeight):
        self.x = x
        self.y = y
        self.screenHeight = screenHeight
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (self.x, self.y)
        self.vel = 25

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= self.height/2:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y <= self.screenHeight - self.height/2:
            self.y += self.vel
        
        self.rect.center = (self.x, self.y)

class Ball():
    def __init__(self, width, height, color, screenWidth, screenHeight):

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.width = width
        self.height = height
        self.color = color
        self.baseSpeed = 20

        self.respawnBall()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def respawnBall(self):
        self.x = self.screenWidth/2
        self.y = random.randint(self.height/2, self.screenHeight - self.height/2)
        self.xVel = random.choice((1, -1)) * 10
        self.yVel = random.randint(0, 10)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect.center = (self.x, self.y)

    def gamePlay(self, paddleList):

        for x in paddleList:
            if pygame.Rect.colliderect(self.rect, x):
                self.yVel = self.baseSpeed*(self.rect.centery - x.rect.centery)*(0.3/self.height)
                self.xVel = -self.xVel

        if self.rect.top <= 0 or self.rect.bottom >= self.screenHeight:
            self.yVel = -self.yVel


        self.x += self.xVel
        self.y += self.yVel

        self.rect.center = (self.x, self.y)

    def gameWaiting(self, paddleList):

        for x in paddleList:
            if pygame.Rect.colliderect(self.rect, x):
                self.yVel = self.baseSpeed*(self.rect.centery - x.rect.centery)*(0.3/self.height)
                self.xVel = -self.xVel

        if self.rect.top <= 0 or self.rect.bottom >= self.screenHeight:
            self.yVel = -self.yVel

        elif self.rect.left <= 0 or self.rect.right >= self.screenWidth:
            self.xVel = -self.xVel

        self.x += self.xVel
        self.y += self.yVel

        self.rect.center = (self.x, self.y)

class ScoreBoard():
    def __init__(self, color, screenWidth, screenHeight):
        self.color = color
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.pScore = 0
        self.p2Score = 0

    def draw(self, screen, font):

        self.text = font.render(str(self.pScore), True, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.screenWidth/4, self.screenHeight/8)

        self.text2 = font.render(str(self.p2Score), True, self.color)
        self.textRect2 = self.text2.get_rect()
        self.textRect2.center = (self.screenWidth*3/4, self.screenHeight/8)

        screen.blit(self.text, self.textRect)
        screen.blit(self.text2, self.textRect2)

        
        