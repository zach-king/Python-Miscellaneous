# Uses the PyBluez package

from bluetooth import *

target_name = "SAMSUNG-SM-G925A"
target_address = None

nearby_devices = discover_devices()

for address in nearby_devices:
    if target_name == lookup_name(address):
        target_address = address
        break
if target_address is not None:
    print("Found target bluetooth device with address ", target_address)
else:
    print("Could not find target bluetooth device nearby")
