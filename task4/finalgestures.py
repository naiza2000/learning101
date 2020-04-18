#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import cv2 as cv
import numpy as np
PI = 3.1415926535897
def find_direction():
    cap = cv.VideoCapture(0)
    count = 0
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    _, f1 = cap.read()
    hsv1 = cv.cvtColor(f1, cv.COLOR_BGR2HSV)
    mask1 = cv.inRange(hsv1, lower_blue, upper_blue)
    cnts1,_ = cv.findContours(mask1, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    while(1):
    # Take each frame
        _, frame = cap.read()
        count = count + 1
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        cnts,_ = cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        cv.imshow("capturing",mask)
        if(count==100):
            cnts2 = cnts
         
 

            max_cont1 = max(cnts1, key=cv.contourArea)
            max_cont2 = max(cnts2, key=cv.contourArea)

            moment1 = cv.moments(max_cont1)
            if moment1['m00'] != 0:
                x1 = int(moment1['m10'] / moment1['m00'])
                y1 = int(moment1['m01'] / moment1['m00'])
            moment2 = cv.moments(max_cont2)
            if moment1['m00'] != 0:
                x2 = int(moment2['m10'] / moment2['m00'])
                y2 = int(moment2['m01'] / moment2['m00']) 
            if(np.abs(x2-x1)>np.abs(y2-y1)):
                move(x2,x1)
            else:
                rotate(y2,y1)
            count = 1
            cnts1 = cnts2 
        k = cv.waitKey(1)
        if k == 27:
            cv.destroyAllWindows()
        

def move(x2,x1):
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    print("Let's move your robot")
    speed = 1
    distance = 5
    
    
    vel_msg.linear.y = 0
    vel_msg.linear.x = 0
    
   
      
    if(x2<x1):
        print("right")
        vel_msg.linear.x = abs(speed)

    if(x2>x1):
        print("left")
        vel_msg.linear.x = -abs(speed)
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
 
    while not rospy.is_shutdown():
   
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
           
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
           #Force the robot to stop
        velocity_publisher.publish(vel_msg)
def rotate(y2,y1):
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
   
       # Receiveing the user's input
    print("Let's rotate your robot")
    angular_speed = PI/2
    relative_angle = PI/2
  
      #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
  
       # Checking if our movement is CW or CCW
    if(y2<y1):
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
       # Setting the current time for distance calculus
  
    t0 = rospy.Time.now().to_sec()
    current_angle = 0
   
    while(current_angle < relative_angle):
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
   
   
       #Forcing our robot to stop
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()

   
if __name__ == '__main__':
    try:
           #Testing our function
        find_direction()
    except rospy.ROSInterruptException: pass
