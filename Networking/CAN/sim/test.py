import ecu
import sim_can as sc

bus = sc.Bus()
ecu1 = ecu.ECU(0, 'Engine Control Unit')
ecu2 = ecu.ECU(1, 'Transmission Control Unit')

# Set correct files to detect which message IDs to handle
ecu1.SetHandleFile('EngineMessages.dat')
ecu2.SetHandleFile('TransmissionMessages.dat')

bus.AddECU(ecu1)
bus.AddECU(ecu2)
bus.Init() # set each ecu to connect to this bus

while True:
    msg = input('Enter msg: ')
    if msg == 'exit':
        break
    bus.Send(msg)
    print('-' * 30)

