from bluetooth import *

sock = BluetoothSocket(L2CAP)

bd_addr = "2C:BE:08:E6:8E:51"
port = 0x1001

sock.connect((bd_addr, port))

sock.send("Hello!")
sock.close()
