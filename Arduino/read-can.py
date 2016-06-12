import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.readline() # 'Press 1 to LED ON...'

while True:
    _id = str(ser.readline(), 'utf-8').rstrip() 
    _dlc = str(ser.readline(), 'utf-8').rstrip()
    ser.readline()
    _data = str(ser.readline(), 'utf-8').rstrip()
    ser.readline()
    ser.readline()

    print(_id)
    print(_dlc)
    print(_data)
    print("------------------")

