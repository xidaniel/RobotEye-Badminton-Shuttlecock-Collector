# Robot-for-Collecting-Badminton-Shuttlecock
## About The Project 
More and more people choose professional gymnasiums to practice badminton. The main way to collect and sort badminton shuttlecocks are by hand or mechanical machines. In order to improve the efficiency of collecting and sorting and save the salary paid for staff in gyms, we began the research of a semi-automatic robot, it can see, collect and sort the shuttlecocks much more quickly and help people relax themselves during playing badmintons. With Robot, professional gymnasiums can decrease workload to save money. Robot consists of several components and is controlled by software. People can control the Bot by laptop or cell phone via Wi-Fi connection. There are a chassis with move all around wheels, Raspberry Pi 3 B+ board, a brush and pulley system in Robot. With designed structure, Robot can collect and sort shuttlecocks in order in containers.

## Overview of the robot
<img src="https://github.com/xidaniel/Robot-for-collecting-badminton-shuttlecock/blob/master/x-bot.png" width=600 alt="robot" />

## Contributing
- Built a unique physical robot from scratch and developed a software control system to automatically handle the logic among detection results, motion planning, and obstacle avoidance utilizing **Python and OpenCV**.
- Developed an Android mobile application for the user to control robot activity via Bluetooth connection utilizing Java.
- Design a dynamic website to present the robot’s development stages using HTML/JavaScript/CSS with a **Tomcat web server**.
- Trained a badminton shuttlecock detection model utilizing a **Faster R-CNN** framework to achieve 97% average precision.
- Optimized Frame per Second (FPS) from **3.68 to 34.4** perform real-time object detection on Raspberry Pi using **Tensorflow Lite**.

## Project Files Description
- MainControl.py: Distance meansure, contral logic. 
- Shuttlecocks.py: Detect objects with bbox.
- Motor.py: Init and set up GPIO of raspberry Pi for moving.
- Ultrasonic.py: To avoid obstacles by using ultrasonic sensor.
- cascade.xml: Cascade classifier model by loading OpenCV framework.

## Contact
Xi Wang xiwang3317@gmail.com
