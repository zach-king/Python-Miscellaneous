from canard import can
from canard.hw import peak
from canard.hw import socketcan
import sys, time
from random import randrange

if len(sys.argv) != 2:
    print('Usage:\n\tpython3 auth-test.py <can-dev-name>')
    sys.exit(1)

#dev = peak.PcanDev()
dev = socketcan.SocketCanDev(sys.argv[1])

dev.start()

auth_frame = can.Frame(id=0x0, dlc=0x8, data=[0x4f, 0x12, 0xc1, 0x15, 0x43, 0xff, 0x0c, 0x95])

while True:
    rand_frame = can.Frame(randrange(0x7FF))
    rand_frame.dlc = randrange(9)
    d = []
    for i in range(rand_frame.dlc):
        d.append(randrange(0xFF))
    rand_frame.data = d

    dev.send(auth_frame)
    dev.send(rand_frame)
    time.sleep(0.1) # delay half a second
