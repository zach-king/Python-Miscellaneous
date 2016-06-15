import secure_hardware_module as shm
import auth
import socket
import time

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
        self._sock = socket.socket()

    def SetBus(self, bus):
        self._canbus = bus
        self._sock.connect(('127.0.0.1', 50000))
        self.Operate()

    def Operate(self):
        while True:
            self.Receive()
        
    def TakeMessage(self, msg):
        print(self._name + ' RX: ' + str(msg))
        self.msg_list.append(msg)
        if self.HandlesMessage(msg):
            self.HandleMessage(msg)

    def Send(self, msg):
        if self._canbus != None:
            auth_msg = self.Sign(msg)
            if msg == -1:
                print('Failed to sign message')
                return
            for m in auth_msg:
                self._canbus.Send(m)
            self._canbus.Send(msg)

    def Receive(self):
        msg = self._sock.recv(1024)
        print('Received', str(msg))

    def SetHandleFile(self, fname):
        self.handled_file = fname

    def HandlesMessage(self, msg):
        with open(self.handled_file, 'r') as f:
            ids = f.read().splitlines()
            return msg[:3] in ids

    def HandleMessage(self, msg):
        #print(self._name + ' handled ' + msg)
        pass

    def Sign(self, msg):
        _key = shm.get_key(self._id)
        if _key == -1:
            return -1
        return auth.sign_message(_key, msg)

    def __str__(self):
        return self._name
