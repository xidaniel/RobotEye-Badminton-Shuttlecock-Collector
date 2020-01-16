# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import RPi.GPIO as GPIO
import time

class UL:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        self.Trig = 3
        self.Echo = 5
        GPIO.setup(self.Trig, GPIO.OUT)
        GPIO.setup(self.Echo, GPIO.IN)
    
    def dist(self):
        GPIO.output(self.Trig,True)
        time.sleep(0.00001)
        GPIO.output(self.Trig,False)

        while GPIO.input(self.Echo) == 0:
            pass
        start = time.time()

        while GPIO.input(self.Echo) == 1:
            pass
        end = time.time()
        return round(((end - start)*17150),2)
    