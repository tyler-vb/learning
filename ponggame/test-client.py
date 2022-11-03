import socket

format = 'utf-8'
host = '127.0.0.1'
port = 5555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print(f'connected to server - {host}:{port}')

    connected = True
    
    while connected:

        msg = input('> ')
        data = msg.encode(format)
        s.send(data)
        
        data = s.recv(1024)
        print(f'message recieved: {data.decode(format)}')
