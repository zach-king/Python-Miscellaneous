"""
Note: this does not use actual CAN sockets, but rather
demonstrates the format of a packet to be sent in a CAN.
"""

import struct
import socket

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

print('CAN Initialized and Listening for connections...')

can_fmt = "=IB3xBBBBBBBB"
PACKET_SIZE = 16

while True:
    conn, addr = s.accept()
    print('CAN connected by', addr)
    while True:
        raw_data = conn.recv(PACKET_SIZE)
        if not raw_data: break
        conn.send(b'Packet Received!')

        _id, dlc, d0, d1, d2, d3, d4, d5, d6, d7 = struct.unpack(can_fmt, raw_data)
        print("-- Received Packet: --")
        print("\tPID: 0x%X" % _id)
        print("\tDLC: 0x%X" % dlc)
        data = [d0, d1, d2, d3, d4, d5, d6, d7]
        print("\tData: " + str(data))
        print("------------------------------------\n")

    conn.close()
