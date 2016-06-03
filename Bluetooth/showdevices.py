from bluetooth import *

nearby_devices = discover_devices()

for device in nearby_devices:
    print("%s - %s" % (lookup_name(device), device))
