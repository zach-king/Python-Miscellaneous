import struct
import socket

serverHost = '127.0.0.1'
serverPort = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverHost, serverPort))

print('Packet Submission Form:')
_id = int(input('PID: '), 0)
dlc = int(input('dlc: '), 0)
data = []
for i in range(8):
    data.append(int(input('D' + str(i) + ': '), 0))

print('\nWhat You Entered:')
print("PID: " + str(_id))
print("dlc: " + str(dlc))
print("Data: " + str(data))

can_fmt = "=IB3xBBBBBBBB"
packet = struct.pack(can_fmt, _id, dlc, data[0],
    data[1], data[2], data[3], data[4], data[5], data[6], data[7])
s.send(packet)
reply = s.recv(1024)
print('\n%s' % repr(reply))

s.close()
