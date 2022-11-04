import pygame

class Paddle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.vel = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect.center = (self.x, self.y)


class Ball():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.xVel = 5
        self.yVel = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collide(self, paddleList, screenHeight, screenWidth):

        for x in paddleList:
            if self.rect.colliderect(x):
                self.xVel = -self.xVel

        if self.rect.top <= 0 or self.rect.bottom >= screenHeight:
            self.yVel = -self.yVel

        self.x += self.xVel
        self.y += self.yVel

        self.rect.center = (self.x, self.y)