"""
A Simulative Secure Hardware Module
for storing shared keys
"""

class Keys:
    KEY0 = b'shared secret key'
    KEY1 = b'another shared secret key'


def get_key(_id):
    if _id == 0:
        return Keys.KEY0 
    elif _id == 1:
        return Keys.KEY1
    else:
        return -1
