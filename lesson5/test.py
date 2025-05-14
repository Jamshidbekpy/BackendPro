# import socket

# host = 'localhost'
# port = 8000

# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_server.bind((host, port))
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# socket_server.listen()
# print(f'Listening on port {host}:{port}...')

# socket_client, address = socket_server.accept()
# print(f'Connected by {address}')

# data = socket_client.recv(1024)
# print(f'Received data {data.decode('utf-8')}')

# socket_client.close()

import socket

host = 'localhost'
port = 8000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

socket_server.listen()
print(f'Listening on port {host}:{port}...')

socket_client, address = socket_server.accept()
print(f'Connected by {address}')

data = socket_client.recv(1024)
socket_client.sendall(data)

socket_client.close()