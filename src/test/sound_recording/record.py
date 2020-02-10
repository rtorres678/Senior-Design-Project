#!/usr/bin/env python

import os
import serial
import subprocess

port = "/dev/ttyACM0"

ser = serial.Serial(port, 9600)
ser.flushInput()

count = 0

def func(bit):
    p = subprocess.Popen('. ~/Senior-Design-Project/src/test/sound_recording/start.sh', shell=True)
    if bit == 0:
        p.kill();

while True:
    #input = ser.read().decode("utf-8")
    val = ser.read().decode("utf-8")
    if val == 'a':
        if count != 1:
            count = 1
            os.system("lxterminal -e ~/Senior-Design-Project/src/test/sound_recording/start.sh -t killMe")
            #subprocess.Popen('. ~/Senior-Design-Project/src/test/sound_recording/start.sh', shell=True)
            #func(1)
    if val == 'z':
        if count != 0:
            count = 0
            print('2')
            #func(0)
