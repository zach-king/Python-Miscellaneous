import socket

HOST = '127.0.0.1'
PORT = 9000

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)

ecu1, addr1 = s.accept()
ecu2, addr2 = s.accept()

print('Both ECUs connected successfully')

while True:
    data = ecu1.recv(1024)
    if data:
        print(data)
        ecu1.send(b'hey there!')
        