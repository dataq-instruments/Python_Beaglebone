import serial
import time
import sys

#This sample program will start DATAQ Instrument (11xx/2108/4108/4208/4718) usb data acquisition products
#Please make sure the device is in CDC mode (blinking yellow when conntected)

CONST_SER_PORT = '/dev/ttyACM0'   

serDataq = serial.Serial(CONST_SER_PORT)
serDataq.set_buffer_size=60000

# the default ASCII string format in Python is not the 8-bit ASCII, which our devices use, 
# so one need to tell Python to construct ASCII in 8-bit format by inserting b in front 
# of the string, such as b"stop\r" instead of "stop/r"

serDataq.write(b"stop\r")        #stop in case device was left scanning
serDataq.write(b"eol 1\r") 
serDataq.write(b"encode 1\r")    #set up the device for ascii mode
serDataq.write(b"slist 0 0\r")   #scan list position 0 channel 0 thru channel 7
serDataq.write(b"slist 1 1\r")
serDataq.write(b"slist 2 2\r")
serDataq.write(b"slist 3 3\r")
serDataq.write(b"slist 4 4\r")
serDataq.write(b"slist 5 5\r")
serDataq.write(b"slist 6 6\r")
serDataq.write(b"slist 7 7\r")
serDataq.write(b"srate 6000\r") 
serDataq.write(b"dec 100\r")    
serDataq.write(b"deca 10\r")    
time.sleep(1)  
serDataq.read_all()              #flush all command responses
serDataq.write(b"start\r")           #start scanning

while True:
    try:
            i= serDataq.inWaiting()
            if i>0:
                print(serDataq.readline())
    except:
        pass
