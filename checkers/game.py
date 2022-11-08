import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

class Board():
    def __init__(self, spaces, boardSize):
        self.spaces = spaces
        self.boardSize = boardSize
        self.spaceSize = int(boardSize / spaces)
        self.board()

    def board(self):
        self.spaceList = []

        for i in range(0, self.boardSize, self.spaceSize):
            spaceRow = []
            for j in range(0, self.boardSize, self.spaceSize):
                space = pygame.rect.Rect(i, j, self.spaceSize, self.spaceSize)
                spaceRow.append(space)
            self.spaceList.append(spaceRow)
    
    def draw(self, screen):

        for i in range(0, self.spaces):
            if i % 2 == 0:
                for j in range(0, self.spaces):
                    if j % 2 == 0:
                        pygame.draw.rect(screen, black, self.spaceList[j][i])
                    else:
                        pygame.draw.rect(screen, red, self.spaceList[j][i])

            else:
                for j in range(0, self.spaces):
                    if j % 2 == 0:
                        pygame.draw.rect(screen, red, self.spaceList[j][i])
                    else:
                        pygame.draw.rect(screen, black, self.spaceList[j][i])

class Piece():
    def __init__(self, color, spaces, spaceList):
        self.color = color
        self.spaces = spaces
        self.spaceList = spaceList
        self.pieces()

        self.pickedUp = False
        self.pieceY = 0
        self.pieceX = 0

    def pieces(self):
        self.pieceList = []

        for i in range(0, self.spaces):
            pieceRow = []
            for j in range(0, self.spaces):
                pieceRow.append(False)
            self.pieceList.append(pieceRow)
    
    def draw(self, screen):
        for i in range(0, self.spaces):
            for j in range(0, self.spaces):
                if self.pieceList[j][i] == True:
                    pygame.draw.circle(screen, self.color, (self.spaceList[j][i].centerx, self.spaceList[j][i].centery), self.spaceList[0][0].width*4/10)

    def diagonalLeftCounter(self, row, column):

        counter = 0

        for i in range(1, self.spaces):
            if self.pieceList[row - i][column - i] == True:
                counter += 1
            else:
                break

        return counter
    
    def diagonalRightCounter(self, row, column):

        counter = 0

        for i in range(1, self.spaces):
            if self.pieceList[row + i][column - i] == True:
                counter += 1
            else:
                break
        
        return counter

    def playerMove(self, mousex, mousey):

        if self.pickedUp == False:
            for i in range(0, self.spaces):
                for j in range(0, self.spaces):
                        if self.pieceList[j][i] == True and self.spaceList[j][i].collidepoint((mousex, mousey)):
                            self.pieceList[j][i] = False
                            self.pieceX = j
                            self.pieceY = i
                            self.pickedUp = True
        
        else:              
            if self.pieceList[self.pieceX][self.pieceY - 1] == False and self.spaceList[self.pieceX][self.pieceY - 1].collidepoint((mousex, mousey)):
                self.pieceList[self.pieceX][self.pieceY - 1] = True
                self.pickedUp = False

            elif self.spaceList[self.pieceX - 1 - self.diagonalLeftCounter(self.pieceX, self.pieceY)][self.pieceY - 1 - self.diagonalLeftCounter(self.pieceX, self.pieceY)].collidepoint((mousex, mousey)):
                self.pieceList[self.pieceX - 1 - self.diagonalLeftCounter(self.pieceX, self.pieceY)][self.pieceY - 1 - self.diagonalLeftCounter(self.pieceX, self.pieceY)] = True
                for i in range(0, self.diagonalLeftCounter(self.pieceX, self.pieceY)):
                    self.pieceList[self.pieceX - i][self.pieceY - i] = False
                    self.pickedUp = False

            elif self.spaceList[self.pieceX + 1 + self.diagonalRightCounter(self.pieceX, self.pieceY)][self.pieceY - 1 - self.diagonalRightCounter(self.pieceX, self.pieceY)].collidepoint((mousex, mousey)):
                self.pieceList[self.pieceX + 1 + self.diagonalRightCounter(self.pieceX, self.pieceY)][self.pieceY - 1 - self.diagonalRightCounter(self.pieceX, self.pieceY)] = True
                for i in range(0, self.diagonalRightCounter(self.pieceX, self.pieceY)):
                    self.pieceList[self.pieceX + i][self.pieceY - i] = False
                    self.pickedUp = False




