#!/usr/bin/env python

import serial
import time
import sys

usb_port = sys.argv[1]
# Open grbl serial port
s = serial.Serial(str(usb_port),115200)
wakeup_message = "\r\n\r\n"
s.write(wakeup_message.encode()) # Wake up grbl
time.sleep(2)   # Wait for grbl to initialize
s.flushInput()  # Flush startup text in serial input
 
# Stream g-code to grbl
try:
    while True:
        gcode_to_send = input("Please type your gcode.")
        l = gcode_to_send.strip() # Strip all EOL characters for streaming
        l = l + '\n'
        l = l.encode()
        print('Sending: ' + str(l))
        s.write(l) # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print(grbl_out.strip())
except KeyboardInterrupt:
    s.close()