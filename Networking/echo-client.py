# Echo client program
import socket
import sys

serverHost = '127.0.0.1'
serverPort = 50007

message = [b'Hello network world'] # default text to send to server

if len(sys.argv) > 1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverHost, serverPort))

for line in message:
    s.send(line)
    data = s.recv(1024)
    print('Received:', data)
