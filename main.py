#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('main')
    rospy.wait_for_service('trigger_go_kitcken')  
    rospy.wait_for_service('trigger_stop')  
    rospy.wait_for_service('trigger_left')  
    rospy.wait_for_service('trigger_right')  
    rospy.wait_for_service('trigger_go_home') 
    rospy.wait_for_service('trigger_stop')   
    try:
        kitchen_go = rospy.ServiceProxy('trigger_go_kitcken', Empty)  
        resp_kitchen = kitchen_go()
        stop_st = rospy.ServiceProxy('trigger_stop', Empty)  
        resp_stop = stop_st()
        left_go = rospy.ServiceProxy('trigger_left', Empty)  
        resp_left = left_go()
        right_go = rospy.ServiceProxy('trigger_right', Empty)  
        resp_right = right_go()
        home_go = rospy.ServiceProxy('trigger_go_home', Empty)  
        resp_home = home_go()
        stop_st2 = rospy.ServiceProxy('trigger_stop', Empty)  
        resp_stop2 = stop_st2()
        home_go = rospy.ServiceProxy('trigger_go_home', Empty)  
        resp_home = home_go()
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
if __name__ == "__main__": 
    main()
