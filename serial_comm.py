import serial
import serial.tools.list_ports
import time

#"""
def get_arduino_port():
    ports_list = list(serial.tools.list_ports.comports())
    if ports_list:
        for p in ports_list:
            print(p)
            device = str(p.description)
            if device=="Generic CDC": #MAC Specific
                return p.device
            elif "ACM" in device: #Linux Specific
                return ("/dev/" + device)
            else:
                print("Arduino not found.\n")
    else:
        print("No device found.\n")
#"""

#"""
print("\n")
port = get_arduino_port()
print("Arduino found in " + port)
print("connecting")
#"""

ser = serial.Serial(port, 9600)

while True:

    s=0
    end_time = time.time()+5
    while time.time()<end_time:
        s+=int(ser.readline().decode())

    print(s)