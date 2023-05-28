#!/usr/bin/env python3
from std_srvs.srv import Empty, EmptyResponse
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("std_codeNumber", String, callback)
    rospy.Subscriber("NameSurname", String, callback)
    rospy.spin()
    
def user_trigger():
    rospy.wait_for_service('chayanin')
    try:
        trigger = rospy.ServiceProxy('chayanin', Empty)
        print("Please do something.")
        resp1 = trigger()
        listener()
        print("Information is Done!!!!!!!")
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
        
if __name__ == "__main__":
    user_trigger()
    
    
