"""
Simulates a car's CAN Bus
by generating valid messages every second.
"""

class Bus(object):
    """
    Simulative CAN Bus
    """

    def __init__(self, _id=0, ecu_list=[]):
        self._id = 0
        self._ecu_list = ecu_list

    def AddECU(self, ecu):
        self._ecu_list.append(ecu)

    def Init(self):
        for ecu in self._ecu_list:
            ecu.SetBus(self)

    def Send(self, msg):
        for ecu in self._ecu_list:
            ecu.TakeMessage(msg)

    def ListECUs(self):
        print("ECU's in Bus:")
        for ecu in self._ecu_list:
            print('%i: %s' % (ecu._id, str(ecu)))



