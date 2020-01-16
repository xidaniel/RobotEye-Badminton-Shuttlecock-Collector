# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np
import os
import sys
import Motor as Mo

class SHU:
    def __init__(self):
        self.Shuttlecocks = cv2.CascadeClassifier("cascade.xml")
        self.Shuttlecocks.load('/home/pi/Desktop/X-Bot Project/cascade.xml')
        self.cap = cv2.VideoCapture(0)
    
    def find(self):
        ret, frame = self.cap.read()
        if frame is None:
            return frame, []
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rect = self.Shuttlecocks.detectMultiScale(
            gray,
            scaleFactor= 1.03,
            minNeighbors= 20,
            minSize=(3,3),
            flags = cv2.IMREAD_GRAYSCALE
        )

        return frame, np.array(rect)
    
    def show(self, frame, rect):
        if frame is None:
            return
        font = cv2.FONT_HERSHEY_SIMPLEX
        for (x, y, w, h) in rect:
            cv2.putText(frame, 'Shuttlecock', (x , y-3), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow('Shuttlecocks detecting', frame)
        cv2.waitKey(1)
        
    def close(self):
        print("close shuttle")
        self.cap.release()
        cv2.destroyAllWindows()


