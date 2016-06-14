from fnvhash import fnv1a_32
import shm  # secure hardware module
import sys
import hmac

def sign_msg(orig_msg):
    msg = orig_msg
    _id = msg[:3]
    _dlc = msg[4:6]
    msg = msg[6:]
    _key = shm.get_key(_id)
    if _key == -1:      # no stored key for that msg_id
        print('No key for that message ID')
        sys.exit(1)

    signature = get_signature(_key, msg[6:].encode())
    if len(signature) != 8:
        signature = pad_signature(signature)

    msg = signature + msg[6:]
    return _id + '#' + _dlc + msg + orig_msg[6:]
    
def pad_signature(signature):
    l = len(signature)
    padding = '0' * (8 - l)
    return padding + signature

def get_signature(_key, data):
    return hex(fnv1a_32(_key + data))[2:]

if __name__ == '__main__':
    print(sign_msg('100#020338'))
    print(sign_msg('123#0101'))
