#!/usr/bin/env python3
"""
Author: Adrian Falke
Email: <adrian.falke[at]gmail.com>
Credits: http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
License: Creative Commons Attribution 3.0
"""

import rospy
from std_msgs.msg import String
import serial
import ultimaker_schedule_planning as usp
import ultimaker_support_functions as usf

ser = serial.Serial()  # define class


def callback(data):  # logging user input data, defining path planning
    rospy.loginfo(rospy.get_caller_id())
    print('I heard ' + data.data)

    if data.data == 's1':  # check user input against predefined schedule matching words
        usp.schedule_1()
    elif data.data == 's2':
        usp.schedule_2()
    elif data.data == 'disable':
        usf.disable()
    elif data.data == 'off':
        usf.printer_off()
    else:
        print('Wrong schedule name.')


def listener():
    rospy.init_node('ultimaker_listener', anonymous=True)  # initialize listener node
    rospy.Subscriber('ultimaker_chatter', String, callback)  # subscribe to topic
    print('Hello there, I am listening!')
    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped


if __name__ == '__main__':
    listener()
    # callback('s1')
