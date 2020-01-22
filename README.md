# Robot-for-collecting-badminton-shuttlecock
# Abstract 
More and more people choose professional gymnasiums to practice badminton. The main way to collect and sort badminton shuttlecocks are by hand or mechanical machines. In order to improve the efficiency of collecting and sorting and save the salary paid for staff in gyms, we began the research of a semi-automatic robot, it can see, collect and sort the shuttlecocks much more quickly and help people relax themselves during playing badmintons. With Robot, professional gymnasiums can decrease workload to save money. Robot consists of several components and is controlled by software. People can control the Bot by laptop or cell phone via Wi-Fi connection. There are a chassis with move all around wheels, Raspberry Pi 3 B+ board, a brush and pulley system in Robot. With designed structure, Robot can collect and sort shuttlecocks in order in containers.

# Overview of robot
<img src="/i/eg_tulip.jpg"  alt="上海鲜花港 - 郁金香" />

## Project Files Description
- MainControl.py: Distance meansure, contral logic. 
- Shuttlecocks.py: Detect objects with bbox.
- Motor.py: Init and set up GPIO of raspberry Pi for moving.
- Ultrasonic.py: To avoid obstacles by using ultrasonic sensor.
- cascade.xml: Cascade classifier model by loading OpenCV framework.
