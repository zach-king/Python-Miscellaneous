"""
Interface for different packet formats.
"""

import struct
import time

class CANPacket(object):
    """Packet for data sent in a Controlled Area Network (CAN)"""
    packing_format = "=IB3xBBBBBBBB"

    def __init__(self, pid=0, dlc=0, data=b''):
        self._pid = pid
        self._dlc = dlc
        self._data = data
        self._pad_data()

    # NEEDS UPDATING since self._data is now a bytes string, not list!
    def _pad_data(self):
        self._data.extend([0] * (8 - len(self._data)))

    def Packed(self):
        return struct.pack(CANPacket.packing_format, self._pid,
            self._dlc, self._data)

    def Unpacked(self, packet, should_store=False):
        pid, dlc, d0, d1, d2, d3, d4, d5, d6, d7 = struct.unpack(CANPacket.packing_format, packet)
        data = [d0, d1, d2, d3, d4, d5, d6, d7]
        if should_store:
            self._pid = pid
            self._dlc = dlc
            self._data = data
        return (pid, dlc, data)

    def __str__(self):
        s = 'PID:  0x%X\n' % self._pid
        s += 'DLC:  0x%X\n' % self._dlc
        s += 'Data: ['
        for i in range(7):
            s += '0x%X, ' % self._data[i]
        s += '0x%X]\n' % self._data[7]
        return s
