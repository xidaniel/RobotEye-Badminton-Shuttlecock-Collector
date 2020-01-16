import RPi.GPIO as GPIO
import time, sys
GPIO.setmode(GPIO.BOARD)

def setmode():
    GPIO.setwarnings(False)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT) 
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT) 
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)

def reset():
    GPIO.output(11, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(32, GPIO.LOW)
    GPIO.output(36, GPIO.LOW)     
    GPIO.output(18, GPIO.LOW)
    GPIO.output(33, GPIO.LOW)
    GPIO.output(35, GPIO.LOW)
    GPIO.output(37, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)
    GPIO.output(15, GPIO.LOW) 
    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)

# set front_left_wheel
def fl_forward():
     GPIO.output(11, GPIO.HIGH)
     GPIO.output(13, GPIO.LOW)
def fl_backward():
     GPIO.output(11, GPIO.LOW)
     GPIO.output(13, GPIO.HIGH)
def fl_stop():
     GPIO.output(11, GPIO.LOW)
     GPIO.output(13, GPIO.LOW)
# set front_right_wheel     
def fr_forward():
     GPIO.output(32, GPIO.LOW)
     GPIO.output(36, GPIO.HIGH)
def fr_backward():
     GPIO.output(32, GPIO.HIGH)
     GPIO.output(36, GPIO.LOW)
def fr_stop():
     GPIO.output(32, GPIO.LOW)
     GPIO.output(36, GPIO.LOW)
# set rear_left_wheel    
def rl_forward():
     GPIO.output(18, GPIO.HIGH)
     GPIO.output(33, GPIO.LOW)
def rl_backward():
     GPIO.output(18, GPIO.LOW)
     GPIO.output(33, GPIO.HIGH)
def rl_stop():
     GPIO.output(18, GPIO.LOW)
     GPIO.output(33, GPIO.LOW)
# set rear_right_wheel     
def rr_forward():
     GPIO.output(35, GPIO.LOW)
     GPIO.output(37, GPIO.HIGH)
def rr_backward():
     GPIO.output(35, GPIO.HIGH)
     GPIO.output(37, GPIO.LOW)
def rr_stop():
     GPIO.output(35, GPIO.LOW)
     GPIO.output(37, GPIO.LOW)

def brush():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(12, GPIO.LOW)
    
def stop_brush():
    GPIO.output(15, GPIO.LOW)
    GPIO.output(12, GPIO.LOW)


def belt():
    GPIO.output(29, GPIO.HIGH)
    GPIO.output(31, GPIO.LOW)

def collect(value):
    forward(0.01)
    brush(0.01)
    belt(0.01)
    time.sleep(value)

'''
Set the directions of motion
Twelve: forward,backward,right,left,forward_right,forward_left,
backward_left,backward_right,turning_right,turning_left,lateral_arc
'''
def forward():
    fl_forward()
    fr_forward()
    rl_forward()
    rr_forward()
    
def backward():
    fl_backward()
    fr_backward()
    rl_backward()
    rr_backward()


def left(value):
    fl_backward()
    fr_forward()
    rl_forward()
    rr_backward()
    time.sleep(value)


def right(value):
    fl_forward()
    fr_backward()
    rl_backward()
    rr_forward()
    time.sleep(value)

    
def forward_left(value):
    fr_forward()
    rl_forward()
    time.sleep(value)

 
def forward_right(value):
    fl_forward()
    rr_forward()
    time.sleep(value)

    
def backward_left(value):
    fl_backward()
    rr_backward()
    time.sleep(value)

    
def backward_right(value):
    fr_backward()
    rl_backward()
    time.sleep(value)


def turning_left(value):
    fl_forward()
    fr_backward()
    rl_forward()
    rr_backward()
    time.sleep(value)

    
def turning_right(value):
    fl_backward()
    fr_forward()
    rl_backward()
    rr_forward()
    time.sleep(value)

def lateral_arc(value):
    
    fl_forward()
    fr_backward()
    time.sleep(value)
 
   
def stop_all():
    reset()

def stop_wheels():
    fl_stop()
    fr_stop()
    rl_stop()
    rr_stop()
    
def stop_belt():
    GPIO.output(29, GPIO.LOW)
    GPIO.output(31, GPIO.LOW)