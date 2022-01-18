#!/usr/bin/env python
import math

import rospy
from geometry_msgs.msg import Twist


def move(dist):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel = Twist()
    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    speed = 1
    vel.linear.x = speed
    

    while current_distance < dist:
        velocity_publisher.publish(vel)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)
    vel.linear.x = 0
    velocity_publisher.publish(vel)


def rotate(ang):
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed_ang = 30
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed_ang

    t0 = rospy.Time.now().to_sec()
    current_distance = 0
    while current_distance < ang:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed_ang * (t1 - t0)
    vel_msg.angular.x = 0
    velocity_publisher.publish(vel_msg)


def turt(linear_vel, angular_vel):
    rospy.init_node('turtle1', anonymous=True)
    rate = rospy.Rate(10)

    while True:
        move(linear_vel)
        rate.sleep()
        rotate(math.radians(angular_vel))
        rate.sleep()


if __name__ == '__main__':
    try:
        turt(3, 90)
    except rospy.ROSInterruptException:
        pass
