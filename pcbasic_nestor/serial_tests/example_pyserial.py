import serial
from serial.serialutil import *
from SerialBrewer import SerialBrewer
import serial.serialutil as serialutil
from serial import win32
import time

s = SerialBrewer('COM8',
         baudrate=1200,        # baudrate
         bytesize=FIVEBITS,    # number of databits
         parity=PARITY_NONE,    # enable parity checking
         stopbits=STOPBITS_ONE_POINT_FIVE, # number of stopbits
         timeout=5,             # set a timeout value, None for waiting forever
         xonxoff=0,             # enable software flow control
         rtscts=0,              # enable RTS/CTS flow control
    )

s = SerialBrewer('COM2',
         baudrate=1200,        # baudrate
         bytesize=FIVEBITS,    # number of databits
         parity=PARITY_NONE,    # enable parity checking
         stopbits=STOPBITS_ONE_POINT_FIVE, # number of stopbits
         timeout=5,             # set a timeout value, None for waiting forever
         xonxoff=0,             # enable software flow control
         rtscts=0,              # enable RTS/CTS flow control
    )

while True:
    if s.in_waiting:
        c = s.read(1)
        print hex(ord(c)), "(", c, ")",

    time.sleep(0.5)

# s.setRTS(0)
# s.setDTR(0)
# s.timeout = 5
# s.reset_input_buffer()
# s.reset_output_buffer()
# s.write('hello')
# sys.stdio.write('%r\n' % s.read(5))
# sys.stdio.write('%s\n' % s.in_waiting())
# s.write('Hola')

# while (True):
#     print "Hola"