#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker1():
    pub = rospy.Publisher('std_codeNumber', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        std_codeNumber = "6352500463"
        rospy.loginfo(std_codeNumber)
        pub.publish(std_codeNumber)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass
