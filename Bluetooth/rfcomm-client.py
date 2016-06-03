from bluetooth import *

server_address = "2C:BE:08:E6:8E:51"
port = 1

sock = BluetoothSocket(RFCOMM)
sock.connect((server_address, port))

sock.send("Hello!")
sock.close()
