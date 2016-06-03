from bluetooth import *

port = 0x1001

server_sock = BluetoothSocket(L2CAP)
server_sock.bind(("",port))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print("Accepted connection from ", address)

data = client_sock.recv(1024)
print("Received [%s]" % data)

client_sock.close()
server_sock.close()
