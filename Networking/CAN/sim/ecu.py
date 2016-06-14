
class ECU(object):
    """
    A simulative Electronic Control Unit
    """

    def __init__(self, _id, name):
        self._id = _id
        self._name = name
        self._canbus = None
        self.msg_list = []
        self.handled_file = self._name + '.dat'

    def SetBus(self, bus):
        self._canbus = bus
        
    def TakeMessage(self, msg):
        #print(self._name + ' RX: ' + msg)
        self.msg_list.append(msg)
        if self.HandlesMessage(msg):
            self.HandleMessage(msg)

    def SendMessage(self, msg):
        if self._canbus != None:
            self._canbus.Send(msg)

    def SetHandleFile(self, fname):
        self.handled_file = fname

    def HandlesMessage(self, msg):
        with open(self.handled_file, 'r') as f:
            ids = f.read().splitlines()
            return msg[:3] in ids

    def HandleMessage(self, msg):
        print(self._name + ' handled ' + msg)

    def __str__(self):
        return self._name
