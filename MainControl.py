# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import os, sys , time
import Motor as mo
import Shuttlecocks as shu
import Ultrasonic as ul
import threading

def run():
    print("The car start running...")

    ultra = ul.UL()
    shuttle = shu.SHU()
    f, r = shuttle.find();

    print(len(f), len(f[0]))
    shuttle.show(f,[])
    try:
        while True:
            frame, rect = shuttle.find()
            dist = ultra.dist()
            shuttle.show(frame, rect)
            print('Distance: {}cm'.format(dist), ". Found: {} units".format(len(rect)))
            print(rect)
            if dist <= 20:
                print('Run into blank wall')
                mo.backward()
                mo.belt()
                time.sleep(0.06)
            else:
                if len(rect):
                    mo.setmode()
                    mo.forward()
                    mo.brush()
                    mo.belt()
                    time.sleep(2)
                    mo.stop_wheels()
                    mo.stop_brush()
                    print('Finish collect!')
                    time.sleep(2)
                    mo.stop_belt()
                    print('Finish transmit!')
                else:
                    mo.setmode()
                    mo.stop_all()
                    #print('I could not find shuttlecocks!')
                    

    except KeyboardInterrupt:
        GPIO.cleanup()

    shuttle.close()
          
