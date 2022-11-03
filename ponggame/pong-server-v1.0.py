import socket
import threading
import pickle
import pygame

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

host = '127.0.0.1'
port = 5555



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    str(e)

s.listen(2)
print('server started, waiting for an connection...')

serverData = [Paddle(0, 0, 0, 0, (0, 0, 0)), Paddle(0, 0, 0, 0, (0, 0, 0))]

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

currentPlayer = 0
while True:
    conn, addr = s.accept()

    print(f'connected to: {addr}')
    print(f'connections: {threading.active_count()}')

    thread = threading.Thread(target=handleClient, args=(conn, currentPlayer))
    thread.start()

    currentPlayer += 1