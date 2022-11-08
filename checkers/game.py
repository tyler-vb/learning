import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

class Board():
    def __init__(self, spaces, boardSize):
        self.spaces = spaces
        self.boardSize = boardSize
        self.spaceSize = int(boardSize / spaces)
        self.spawnBoard()

    def spawnBoard(self):
        self.spaceList = []

        for i in range(0, self.boardSize, self.spaceSize):
            spaceRow = []
            for j in range(0, self.boardSize, self.spaceSize):
                space = pygame.rect.Rect(i, j, self.spaceSize, self.spaceSize)
                spaceRow.append([space, False])
            self.spaceList.append(spaceRow)
    
    def draw(self, screen):

        for i in range(0, self.spaces):
            if i % 2 == 0:
                for j in range(0, self.spaces):
                    if j % 2 == 0:
                        pygame.draw.rect(screen, black, self.spaceList[j][i][0])
                    else:
                        pygame.draw.rect(screen, red, self.spaceList[j][i][0])

            else:
                for j in range(0, self.spaces):
                    if j % 2 == 0:
                        pygame.draw.rect(screen, red, self.spaceList[j][i][0])
                    else:
                        pygame.draw.rect(screen, black, self.spaceList[j][i][0])

class Piece():
    def __init__(self, color, boardSpaces):
        self.color = color
        self.boardSpaces = boardSpaces 
        self.pickedUp = False
        self.column = 0
        self. row = 0

    def draw(self, screen):

        for i in range(0, len(self.boardSpaces[0])):
            for j in range(0, len(self.boardSpaces[0])):
                if self.boardSpaces[j][i][1] == True:
                    pygame.draw.circle(screen, self.color, (self.boardSpaces[j][i][0].centerx, self.boardSpaces[j][i][0].centery), self.boardSpaces[0][0][0].width*4/10)
            
    def spawn(self, row, column):
        self.boardSpaces[row][column][1] = True

    def move(self, mousex, mousey):
        if self.pickedUp == False:
            for i in range(0, len(self.boardSpaces[0])):
                for j in range(0, len(self.boardSpaces[0])):
                        if self.boardSpaces[j][i][1] == True and self.boardSpaces[j][i][0].collidepoint((mousex, mousey)):
                            self.boardSpaces[j][i][1] = False
                            self.row = i
                            self.column = j
                            self.pickedUp = True
        
        else:              
            print(self.boardSpaces[self.column][self.row - 1][0].center)
            if self.boardSpaces[self.column][self.row - 1][1] == False and self.boardSpaces[self.column][self.row - 1][0].collidepoint((mousex, mousey)):
                self.boardSpaces[self.column][self.row - 1][1] = True
                self.pickedUp = False
        
        print(self.pickedUp)



        
        

