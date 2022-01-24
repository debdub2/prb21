#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class Turtle:
    PSTATE = 10
    ISTATE = 0.01
    DSTATE = 0
    TURN_ANGLE = math.radians(90)
    MOVING_TIME = rospy.Duration(3)

    def __init__(self):
        rospy.init_node('turtle_controller', anonymous=True)
        self.vel_pub_topic = '/turtle1/cmd_vel'
        self.velocity_pub = rospy.Publisher(self.vel_pub_topic, Twist, queue_size=10)
        self.pose_sub_topic = '/turtle1/pose'
        self.pose_sub = rospy.Subscriber(self.pose_sub_topic, Pose, self.current_angle)

        self.com_vel = Twist()
        self.current_pose = Pose()
        self.current_ang = self.current_pose.theta
        self.com_vel.linear.x = 1
        self.angle_destination = 0
        self.rate = rospy.Rate(10)

    def current_angle(self, data):
        self.current_ang = data.theta

    def move_turtle(self):
        pidIState = 0
        old_angle = 0
        time = rospy.get_rostime()
        while not rospy.is_shutdown():
            if rospy.get_rostime() > time + self.MOVING_TIME:
                time = rospy.get_rostime()
                self.angle_destination = self.angle_destination + self.TURN_ANGLE
                if self.angle_destination > math.radians(180):
                    self.angle_destination -= math.radians(360)
                if self.angle_destination < math.radians(-180):
                    self.angle_destination += math.radians(360)

            err = self.angle_destination - self.current_ang
            if err > math.radians(180):
                err -= math.radians(360)
            if err < math.radians(-180):
                err += math.radians(360)

            pTerm = self.PSTATE * err
            pidIState += err
            iTerm = self.ISTATE * pidIState
            dTerm = self.DSTATE * (self.current_ang - old_angle)
            old_angle = self.current_ang

            self.com_vel.angular.z = pTerm + iTerm - dTerm
            
            self.velocity_pub.publish(self.com_vel)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        a = Turtle()
        a.move_turtle()
    except rospy.ROSInterruptException:
        pass
