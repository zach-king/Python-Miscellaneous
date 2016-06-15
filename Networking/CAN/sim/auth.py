"""
Authenticator Module for simulative CAN messages
"""

import hmac, hashlib
import datetime
import struct

def sign_message(key, message):
    _id = message[:3]
    _dlc = message[4:6]
    _data = message[6:]
    digest = hmac.new(key, message.encode(), hashlib.sha1).digest()
    bites = struct.unpack('=20B', digest) # list of the int values for each byte in hash
    bites = [hex(i)[2:] for i in bites] # convert to str version of hex
    auth_messages = [bites[:8], bites[8:16], bites[16:]] # 2.5 messages; the other half is for timestamp
    auth_messages[0] = _id + '#08' + ''.join(auth_messages[0])
    auth_messages[1] = _id + '#08' + ''.join(auth_messages[1])
    auth_messages[2] = _id + '#04' + ''.join(auth_messages[2])
    return auth_messages # note this returns a list of 3 messages to be sent




