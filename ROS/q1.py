#! /usr/bin/env python
import rospy
import tf
from umic_test.msg import quaternion
from umic_test.msg import euler

def callback(msg):
	# print(msg)
	angles = euler()
	angles.roll,angles.pitch,angles.yaw= tf.transformations.euler_from_quaternion([msg.x,msg.y,msg.z,msg.w])
	print(angles)
	pub2.publish(angles)



rospy.init_node("quaternions")
quaternions  = quaternion()
quaternions.x = 5
quaternions.y = 5
quaternions.z = 2
quaternions.w = 8

rate = rospy.Rate(1)
pub1  = rospy.Publisher('topic1',quaternion,queue_size = 10)
pub2  = rospy.Publisher('topic2',euler,queue_size = 10)
sub = rospy.Subscriber('/topic1', quaternion, callback) 
while not rospy.is_shutdown():
	print(quaternions)
	pub1.publish(quaternions)
	rate.sleep()