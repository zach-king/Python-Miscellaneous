from canard import can, bus
from canard.file import jsondb
from canard.hw import socketcan
from fnvhash import fnv1a_64
import sys

if len(sys.argv) != 2:
    print('Usage:\n\tpython3 auth-decode.py <can-dev-name>')
    sys.exit(1)

passphrase = input('Enter the passphrase: ').encode()
auth_hash = fnv1a_64(passphrase)
print('expecting hex:', hex(auth_hash))
print('(equivalent value):', auth_hash, '\n')

parser = jsondb.JsonDbParser()
b = parser.parse('auth-db.json')

dev = socketcan.SocketCanDev(sys.argv[1])
dev.start()

gate_locked = False

while True:
    frame = dev.recv()
    signals = b.parse_frame(frame)
    if signals:
        if frame.id == 0x0:
            if gate_locked and signals[0].value == auth_hash:
                gate_locked = False
                print('GATE UNLOCKED')
            elif signals[0].value != auth_hash:
                gate_locked = True
                print('GATE LOCKED')
            print('hash:', hex(signals[0].value))
        else:
            if gate_locked:
                print('GATE LOCKED -- FRAME IGNORED')
                continue

            for s in signals:
                print(s)
        print('------------------------------------------')
    else:
        if not gate_locked:
            print('Error: unkown message')
        else:
            print('GATE LOCKED -- FRAME IGNORED')

