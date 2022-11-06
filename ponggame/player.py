import pygame

class Paddle():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (self.x, self.y)
        self.vel = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, screenHeight):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y >= 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y <= screenHeight:
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
        self.rect.center = (self.x, self.y)
        self.xVel = 10
        self.yVel = 10
        self.baseSpeed = 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def gamePlay(self, paddleList, screenHeight):

        for x in paddleList:
            if pygame.Rect.colliderect(self.rect, x):
                self.yVel = self.baseSpeed*(self.rect.centery - x.rect.centery)*(1.2/self.height)
                self.xVel = -self.xVel

        if self.rect.top <= 0 or self.rect.bottom >= screenHeight:
            self.yVel = -self.yVel

        self.x += self.xVel
        self.y += self.yVel

        self.rect.center = (self.x, self.y)
    
    def gamePause(self, screenWidth, screenHeight, pause):

        if pause == True:
            self.x = -100
            self.y = -100
            self.xVel = 0
            self.yVel = 0

        else:
            self.x = screenWidth/2
            self.y = screenHeight/2
            self.xVel = 10
            self.yVel = 10

        self.rect.center = (self.x, self.y)

        print('test')

    def gameWaiting(self, paddleList, screenWidth, screenHeight):

        for x in paddleList:
            if pygame.Rect.colliderect(self.rect, x):
                self.yVel = self.baseSpeed*(self.rect.centery - x.rect.centery)*(1.2/self.height)
                self.xVel = -self.xVel

        if self.rect.top <= 0 or self.rect.bottom >= screenHeight:
            self.yVel = -self.yVel

        elif self.rect.left <= 0 or self.rect.right >= screenWidth:
            self.xVel = -self.xVel

        self.x += self.xVel
        self.y += self.yVel

        self.rect.center = (self.x, self.y)