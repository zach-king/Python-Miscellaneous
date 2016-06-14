import serial
import time
import datetime
import can_hash

fname = 'logs/' + datetime.datetime.now().strftime("%Y-%m-%d---%H:%M.log")
log = open(fname, 'w')

ser = serial.Serial('/dev/ttyACM0', 9600)
driver_door_lock = 0
engine_rpm = 0
vehicle_speed = 0

def main():
    while True:
        time.sleep(1)
        data_avail = ser.inWaiting()
        #print(str(data_avail))
        msg_str = str(ser.readline(), 'utf-8').rstrip() 
        print('msg:', msg_str)
        log.write('msg: %s\n' % msg_str)
        _id, msg_str = msg_str.split('#')
        _dlc = msg_str[:2]
        _data = msg_str[2:]

        _id = int('0' + _id, 16)
        _dlc = int(_dlc, 16)
        _data = [_data[i:i+2] for i in range(0, len(_data), 2)]
        _data = [int(i, 16) for i in _data]

        print('ID:',_id)
        log.write('ID: %i\n' % _id)
        print('dlc:', _dlc)
        log.write('dlc: %i\n' % _dlc)
        print('data:', _data)
        log.write('data: %s\n' % _data)

        Respond(_id, _dlc, _data)
        print('--------------------------------------\n')
        log.write('--------------------------------------\n')



def Respond(pid, dlc, data):
    if pid == 291:
        DoorControl(dlc, data)
    elif pid == 2015:   # request information
        RequestInfo(dlc, data)
    elif pid == 256:    # set engine rpm
        EngineRPMControl(dlc, data)
    elif pid == 266:
        VehicleSpeedControl(dlc, data)

def RequestInfo(dlc, data):
    if data[0] == 1:
        ShowCurrentInfo(data[1])

def ShowCurrentInfo(service):
    print('Request for Current Info:', end='\n\t')
    log.write('Request for Current Info:\n\t')
    if service == 1:
        print('Engine RPM:', engine_rpm)
        log.write('Engine RPM: %i\n' % engine_rpm)
    elif service == 13:
        print('Vehicle Speed:', vehicle_speed)
        log.write('Vehicle Speed: %i\n' % vehicle_speed)
    elif service == 15:
        print('Driver Door Lock:', driver_door_lock)
        log.write('Driver Door Lock: %i\n' % driver_door_lock)

def EngineRPMControl(dlc, data):
    global engine_rpm
    if dlc == 0 or dlc > 2:
        return
    engine_rpm = data[0]
    engine_rpm = engine_rpm << 8
    engine_rpm += data[1]
    print('Set Engine RPM to', engine_rpm)
    log.write('Set Engine RPM to %i\n' % engine_rpm)

def VehicleSpeedControl(dlc, data):
    global vehicle_speed
    if dlc != 1:
        return 0
    vehicle_speed = data[0]
    print('Set Vehicle Speed value to', vehicle_speed)
    log.write('Set Vehicle Speed value to %i\n' %  vehicle_speed)

def DoorControl(dlc, data):
    global driver_door_lock
    if dlc == 0:
        return
    
    if data[0] == 0:
        driver_door_lock = 0
        print('Unlocked Driver Door')
        log.write('Unlocked Driver Door\n')
    else:
        driver_door_lock = 1
        print('Locked Driver Door')
        log.write('Locked Driver Door\n')



if __name__ == '__main__':
    main()
