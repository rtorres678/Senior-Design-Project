#!/usr/bin/env python

import os
import serial
import subprocess
import signal
port = "/dev/ttyACM0"

ser = serial.Serial(port, 9600)
ser.flushInput()

count = 0
PID = 0

def func2(p):
    p.kill()

def func1():
    #p = subprocess.Popen('. ~/Senior-Design-Project/src/test/sound_recording/start.sh', shell=True)
    p = subprocess.Popen("exec " + '~/Senior-Design-Project/src/test/sound_recording/start.sh', stdout=subprocess.PIPE, shell=True)
    print(p.pid)
    return p
    #if bit == 0:
    #    p.kill();

while True:
    #input = ser.read().decode("utf-8")
    val = ser.read().decode("utf-8")
    if val == 'a':
        if count != 1:
            count = 1
            PID = func1()
            #print(1)
    if val == 'z':
        if count != 0:
            count = 0
            #print('2')
            func2(PID)
