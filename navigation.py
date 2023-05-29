#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
from std_msgs.msg import String

def server_callback(req):
    print("Doing something..")
    return EmptyResponse()

def server_go_home(req):
    go_home = "Going to home"
    rospy.loginfo(go_home)
    rate = rospy.Rate(120)
    Arrieved_home = "Arrieved"
    rospy.loginfo(Arrieved_home)
    rate.sleep()
    return EmptyResponse()

def server_left(req):
    left_ = "Turn left"
    rospy.loginfo(left_)
    return EmptyResponse()
    
def server_right(req):
    right_ = "Turn right"
    rospy.loginfo(right_)
    return EmptyResponse()

def server_go_to_kitcken(req):
    go_kitcken = "Going to kitcken."
    rospy.loginfo(go_kitcken)
    rate = rospy.Rate(120)
    Arrieved_kitcken = "Arrieved"
    rospy.loginfo(Arrieved_kitcken)
    rate.sleep()
    return EmptyResponse()

def server_stop(req):
    stop_p = "Stop!"
    rospy.loginfo(stop_p)
    return EmptyResponse()

def trigger_server():
    rospy.init_node('trigger_server')
    s = rospy.Service('chayanin', Empty, server_callback)
    s = rospy.Service('trigger_go_home', Empty, server_go_home)
    s = rospy.Service('trigger_go_kitcken', Empty, server_go_to_kitcken)
    s = rospy.Service('trigger_stop', Empty, server_stop)
    s = rospy.Service('trigger_left', Empty, server_left)
    s = rospy.Service('trigger_right', Empty, server_right)
    print("Ready to do something.")
    rospy.spin()

if __name__ == "__main__": 
    trigger_server()
