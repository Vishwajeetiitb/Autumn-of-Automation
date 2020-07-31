#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import math
import os
from turtlesim.msg import Pose
import time
os.system("rosrun")  
def callback(msg):
    global current_angle
    current_angle = msg.theta
    # print(msg)
def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("turtle1/pose",Pose,callback)
    time.sleep(1)
    vel_msg = Twist()
    speed = 2
    distance = 4
    angle = math.pi/3
    angular_ve1 = 1
    vel_msg.angular.z = 0
    current_distance = 0
    t0 = rospy.Time.now().to_sec()
    # t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = 0
    vel_msg.angular.z = angular_ve1
    while current_angle < angle:
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        print(current_angle)
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0        
    velocity_publisher.publish(vel_msg)    


    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = speed
    vel_msg.angular.z =0
    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)
    
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0        
    velocity_publisher.publish(vel_msg) 

    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = -speed
    vel_msg.angular.z =0
    current_distance = 0
    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)
    
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0        
    velocity_publisher.publish(vel_msg) 

    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = 0
    vel_msg.angular.z = angular_ve1
    while current_angle < 2*angle:
        velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
        t1=rospy.Time.now().to_sec()
        print(current_angle)
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0        
    velocity_publisher.publish(vel_msg) 


    t0 = rospy.Time.now().to_sec()
    vel_msg.linear.x = speed
    vel_msg.angular.z =0
    current_distance = 0
    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        t1=rospy.Time.now().to_sec()
        current_distance = speed*(t1-t0)
    
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0        
    velocity_publisher.publish(vel_msg) 



if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass