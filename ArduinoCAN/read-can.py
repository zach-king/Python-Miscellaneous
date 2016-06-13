import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    time.sleep(1)
    data_avail = ser.inWaiting()
    #print(str(data_avail))
    msg_str = str(ser.readline(), 'utf-8').rstrip() 
    print('msg:', msg_str)
    _id, msg_str = msg_str.split('#')
    _dlc = msg_str[:2]
    _data = msg_str[2:]

    _id = int('0' + _id, 16)
    _dlc = int(_dlc, 16)
    _data = [_data[i:i+2] for i in range(0, len(_data), 2)]
    _data = [int(i, 16) for i in _data]

    print('ID:',_id)
    print('dlc:', _dlc)
    print('data:', _data)
    print('-------------------------')

