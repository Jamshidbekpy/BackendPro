# 1)
# import socket
# import threading

# host = 'localhost'
# port = 8000


# # AF_INET >> IPv4,  SOCK_STREAM >> TCP
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# # Port ni qayta ishlatish uchun, socket.SOL_SOCKET >> opisanya, socket.SO_REUSEADDR >>> bir xil raqam ,True >> Buni yoqish
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# # IP berib qo'yish // IP ga ulash
# socket_server.bind((host, port))
# # clientlar soni /// navbat
# socket_server.listen()

# clients = []
# clients_lock = threading.Lock()


# def handle_client(client: socket.socket, address: tuple):
#     print(f"[+] Client connected: {address}")
#     try:
#         data = client.recv(1024)
#         print(f"[{address}] Received: {data}")
#     except Exception as e:
#         print(f"[!] Error receiving data from {address}: {e}")
#         data = b""
#     finally:
#         with clients_lock:
#             if client in clients:
#                 clients.remove(client)
#         client.close()

        
#         with clients_lock:
#             for c in clients:
#                 try:
#                     c:socket.socket
#                     c.sendall(data)
#                 except Exception as e:
#                     print(e)
#                 finally:
#                     c.close()
#             clients.clear()


# while True:
#     client, address = socket_server.accept()
#     with clients_lock:
#         clients.append(client)
#     thread = threading.Thread(target=handle_client, args=(client, address))
#     thread.start()
    

# import socket
# import threading

# host = 'localhost'
# port = 8000


# # AF_INET >> IPv4,  SOCK_STREAM >> TCP
# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# # Port ni qayta ishlatish uchun, socket.SOL_SOCKET >> opisanya, socket.SO_REUSEADDR >>> bir xil raqam ,True >> Buni yoqish
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# # IP berib qo'yish // IP ga ulash
# socket_server.bind((host, port))
# # clientlar soni /// navbat
# socket_server.listen()

# clients = []
# clients_lock = threading.Lock()


# def handle_client(client: socket.socket, address: tuple):
#     print(f"[+] Client connected: {address}")
#     try:
#         data = client.recv(1024)
#         print(f"[{address}] Received: {data}")
#     except Exception as e:
#         print(f"[!] Error receiving data from {address}: {e}")
#         data = b""
        
#     finally:
#         with clients_lock:
#             for c in clients:
#                 if c != client:
#                     try:
#                         c:socket.socket
#                         c.sendall(data)
#                     except Exception as e:
#                         print(e)
#                     # finally:
#                     #     c.close()


# while True:
#     client, address = socket_server.accept()
#     with clients_lock:
#         if not client in clients:
#             clients.append(client)
#     thread = threading.Thread(target=handle_client, args=(client, address))
#     thread.start()

    

    
    



# # server.py
# import socket
# import threading
# import time

# def handle_client(client_socket, addr):
#     print(f"[+] Client connected: {addr}")
#     client_socket.sendall(b"Welcome!\n")
#     client_socket.close()

# host = 'localhost'
# port = 9000

# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# server_socket.bind((host, port))
# server_socket.listen(7)  # Faqat 2 ta client navbatga olinadi

# print(f"[*] Server listening on {host}:{port}")

# while True:
#     socket_client, address = server_socket.accept()
#     # data = socket_client.recv(1024)
#     thread = threading.Thread(target=handle_client, args=(socket_client, address))
#     thread.start()


# import 