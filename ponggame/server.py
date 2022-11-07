import socket
import threading
import pickle
import time
from game import *

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

gameData = [Paddle(width - width/10, height/2, 20, 100, black, height), Paddle(width/10, height/2, 20, 100, black, height), Ball(20, 20, black, width, height), ScoreBoard(black, width, height,)]
currentPlayers = 0
    

def handleClient(conn, player):
    conn.send(pickle.dumps((gameData[player], player)))
    gamePause = False
    pScore = 0
    p2Score = 0
    reply = ''
    while True:

        while gamePause:

            try:
                data = pickle.loads(conn.recv(2048))
                gameData[player] = data

                if not gameData:
                    print('disconnected')
                    break

                else:

                    if time.time() - startTime >= 3:
                        gamePause = False
    
                    if player == 0:
                        reply = (gameData[1], gameData[2], gameData[3])

                    else:
                        reply = (gameData[0], gameData[2], gameData[3])
        
                conn.sendall(pickle.dumps(reply))

            except Exception as e:
                print(e)
                break

        try:
            data = pickle.loads(conn.recv(2048))
            gameData[player] = data

            if not gameData:
                print('disconnected')
                break

            else:

                if player == 0:

                    if currentPlayers == 2:

                        if gameData[2].x <= 0:
                            startTime = time.time()
                            gameData[2].respawnBall()
                            gameData[3].p2Score += 1
                            gamePause = True

                        elif gameData[2].x >= width:
                            startTime = time.time()
                            gameData[2].respawnBall()
                            gameData[3].pScore += 1
                            gamePause = True

                        else:
                            gameData[2].gamePlay((gameData[0], gameData[1]))

                    else:
                        gameData[2].gameWaiting((gameData[0], gameData[1]))
                        
                    reply = (gameData[1], gameData[2], gameData[3])

                else:
                    reply = (gameData[0], gameData[2], gameData[3])

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