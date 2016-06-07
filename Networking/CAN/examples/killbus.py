from canard import can
from canard.hw import peak
from canard.hw import socketcan
import sys

#dev = peak.PcanDev()
dev = socketcan.SocketCanDev(sys.argv[1])
dev.start()

frame = can.Frame(0)
frame.dlc = 8

while True:
    dev.send(frame)
