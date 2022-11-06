import socket
import threading
import pickle
import pygame
from player import *

pygame.init()

height = 768
width = 1366

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

host = '192.168.0.83'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    str(e)

s.listen(2)
print('server started, waiting for an connection...')

gameData = [Paddle(width - width/10, height/2, 20, 100, black), Paddle(width/10, height/2, 20, 100, black), Ball(width/2, height/2, 30, 30, black)]
currentPlayers = 0

def handleClient(conn, player):
    conn.send(pickle.dumps((gameData[player], player)))
    timer = 3
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    pause = False
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            gameData[player] = data

            if not gameData:
                print('disconnected')
                break

            else:

                if player == 0:

                    if currentPlayers == 2:

                        # gotta be a better way to do this
                    
                        if gameData[2].rect.left <= 0 or gameData[2].rect.right >= width:
                            for event in pygame.event.get():
                                if event.type == pygame.USEREVENT+1:
                                    timer - 1
                                    pause = True
                                
                                if timer <= 0:
                                    pause = False

                            gameData[2].gamePause(width, height, pause)

                        else:
                            gameData[2].gamePlay((gameData[0], gameData[1]), height)

                    else:
                        gameData[2].gameWaiting((gameData[0], gameData[1]), width, height)
                        
                    reply = (gameData[1], gameData[2])

                else:
                    reply = (gameData[0], gameData[2])

            conn.sendall(pickle.dumps(reply))
            
        except Exception as e:
            print(e)
            break

    print('connection lost')
    conn.close()

while True:
    conn, addr = s.accept()

    print(f'connected to: {addr}')
    print(f'connections: {threading.active_count()}')

    thread = threading.Thread(target=handleClient, args=(conn, currentPlayers))
    thread.start()

    currentPlayers += 1