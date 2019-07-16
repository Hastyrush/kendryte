#!/usr/bin/env python

import os
from time import sleep
import serial
import re
objects = ["aeroplane","bicycle","bird","boat","bottle","bus","car","cat","chair","cow","dinging table","dog","horse","motorbike","person","potted plant","sheep","sofa","train","screen"]
cur_object = 0
isProcessing = 0
ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

while 1:
	if isProcessing != 1:
        	x=ser.readline()
		print(x)
	x=re.findall(r'\d+', x)
        if (x == [] or x == cur_object):
       		print("Nothing detected")
        else:
		isProcessing = 1
		cur_object = x
		x=int(x[0])
                print("I think it is " + objects[x])
		os.system("flite -voice slt -t 'I think it is "+objects[x]+"\'")
		sleep(0.5)
		isProcessing = 0



