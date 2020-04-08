#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    print("for Forward, Press f")
    print("for Backward,Press b")
    print("TO exit, Press 0")

    
    speed = 2
    distance = 2
    f = "f" 
    b = "b"

    
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        isForward = input()
        
    
    #Checking if the movement is forward or backwards
        if(isForward== f):
            vel_msg.linear.x = abs(speed)
        if (isForward== b):
            vel_msg.linear.x = -abs(speed)
        if(isForward==0):
            exit()

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)
        return isForward

if __name__ == '__main__':
    try:
        move()
        
    except rospy.ROSInterruptException: pass
