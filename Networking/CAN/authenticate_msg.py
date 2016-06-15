"""
An example of creating the authentication message(s)
"""

from fnvhash import fnv1a_64
import datetime

def get_timestamp():
    stamp = '{:%H:%M:%S}'.format(datetime.datetime.now())
    stamp = stamp.split(':')
    hour = bin(int(stamp[0]))[2:]
    minute = bin(int(stamp[1]))[2:]
    return pad(hour, 5) + pad(minute, 6) + pad(bin(int(stamp[2]))[2:], 6)


def pad(string, n):
    return string + ('0' * (n - len(string)))


def parse_timestamp(stamp, milTime=True):
    hour = int(stamp[:5], 2)
    minute = int(stamp[5:11], 2)
    second = int(stamp[11:], 2)
    if not milTime:
        hour = hour % 12
    return (hour, minute, second)


def make_digest(msg, key):
    if isinstance(key, bytes):
        msg = msg.encode()
    digest = hex(fnv1a_64(key + msg))
    return digest



stamp = get_timestamp()
print(stamp)
print(parse_timestamp(stamp, False))
print(make_digest('dogs are cool', 'shared key'))