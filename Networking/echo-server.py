# Echo server program
import socket

HOST = ''
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Server connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        conn.send(b'Echo=>' + data)
    conn.close()
