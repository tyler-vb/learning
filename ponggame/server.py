import socket
import threading
import pickle
import pygame
from player import *

host = '192.168.0.83'
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    str(e)

s.listen(2)
print('server started, waiting for an connection...')

serverData = [Paddle(0, 0, 0, 0, (0, 0, 0)), Paddle(0, 0, 0, 0, (0, 0, 0))]

currentPlayer = 0

def handleClient(conn, player):
    conn.send(pickle.dumps(player))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            serverData[player] = data

            if not serverData:
                print('disconnected')
                break
            else:
                if player == 0:
                    reply = serverData[1]
                elif player == 1:
                    reply = serverData[0]

            conn.sendall(pickle.dumps(reply))
            
        except:
            break

    print('connection lost')
    conn.close()

while True:
    conn, addr = s.accept()

    print(f'connected to: {addr}')
    print(f'connections: {threading.active_count()}')

    thread = threading.Thread(target=handleClient, args=(conn, currentPlayer))
    thread.start()

    currentPlayer += 1