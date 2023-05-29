#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def talker2():
    pub = rospy.Publisher('NameSurname', String, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        NameSurname = "Chayanin Lawanrattanakul"
        rospy.loginfo(NameSurname)
        pub.publish(NameSurname)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker2()
    except rospy.ROSInterruptException:
        pass
