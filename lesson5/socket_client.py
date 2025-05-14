# client.py
import socket
import time
import threading

def connect_client(i):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 9000))
        print(f"Client {i} connected.")
        msg = s.recv(1024)
        print(f"Client {i} got: {msg.decode().strip()}")
        s.close()
    except Exception as e:
        print(f"Client {i} failed: {e}")

for i in range(7): 
    t = threading.Thread(target=connect_client,args=(i,))
    t.start()
