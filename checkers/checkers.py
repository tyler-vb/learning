import pygame
import sys
from game import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)

screenSize = 600

spaces = 8

screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption('checkers by Bofa Deez Nuts')

board = Board(spaces, screenSize)
whitePieces = Piece(white, spaces, board.spaceList)

whitePieces.pieceList[3][4] = True
whitePieces.pieceList[4][3] = True
whitePieces.pieceList[2][3] = True
whitePieces.pieceList[1][2] = True

def redrawWindow():
    screen.fill(white)
    board.draw(screen)
    whitePieces.draw(screen)
    pygame.display.update()


def mainLoop():

    run = True
    
    while run:

        mouseX, mouseY = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                whitePieces.playerMove(mouseX, mouseY)

        redrawWindow()
    
    pygame.quit()
    sys.exit()

mainLoop()



