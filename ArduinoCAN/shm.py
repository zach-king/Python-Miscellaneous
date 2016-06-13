"""
A Simulative 'Secure Hardware Module'
for storing shared keys for hashed
method authentication.
"""

class Keys:
    """Enumerator for storing keys. 
    Pretend this storage is secure."""
    ECU1 = b'secret key 123'        # ECU1 = Engine Control Unit
    ECU2 = b'hackers not allowed'   # ECU2 = Door Control Unit
    ECU3 = b'you CAN not hack me'


def get_key(msg_id):
    # msg_id typically sent from ECU1?
    if msg_id == '100':    # set engine rpm
        return Keys.ECU1
    elif msg_id == '123':  # set driver door lock
        return Keys.ECU2
    print(msg_id)
    return -1
