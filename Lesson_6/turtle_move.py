#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math


class PID:
    PSTATE = 10
    ISTATE = 0.01
    DSTATE = 0

    def __init__(self):
        self.pidIState = 0
        self.old_err = 0

    def count_err(self, angdest, currang):
        err = angdest - currang
        if err > math.radians(180):
            err -= math.radians(360)
        if err < math.radians(-180):
            err += math.radians(360)
        return err

    def count_angular(self, err, currang):
        pTerm = self.PSTATE * err
        self.pidIState += err
        iTerm = self.ISTATE * self.pidIState
        dTerm = self.DSTATE * (err - self.old_err)
        self.old_err = err
        return pTerm + iTerm - dTerm


class Turtle(PID):
    TURN_ANGLE = math.radians(90)
    MOVING_TIME = rospy.Duration(3)

    def __init__(self, x):
        PID.__init__(self)
        rospy.init_node('turtle_controller', anonymous=True)
        self.vel_pub_topic = '/turtle1/cmd_vel'
        self.velocity_pub = rospy.Publisher(self.vel_pub_topic, Twist, queue_size=10)
        self.pose_sub_topic = '/turtle1/pose'
        self.pose_sub = rospy.Subscriber(self.pose_sub_topic, Pose, self.current_angle)

        self.com_vel = Twist()
        self.current_pose = Pose()
        self.current_ang = self.current_pose.theta
        self.com_vel.linear.x = x
        self.angle_destination = 0
        self.rate = rospy.Rate(10)

    def current_angle(self, data):
        self.current_ang = data.theta

    def correct_dest(self, ang):
        if ang > math.radians(180):
            ang -= math.radians(360)
        if ang < math.radians(-180):
            ang += math.radians(360)
        return ang

    def move_turtle(self):
        time = rospy.get_rostime()
        while not rospy.is_shutdown():

            if rospy.get_rostime() > time + self.MOVING_TIME:
                time = rospy.get_rostime()
                self.angle_destination = self.angle_destination + self.TURN_ANGLE
                self.angle_destination = self.correct_dest(self.angle_destination)
                

            self.com_vel.angular.z = self.count_angular(self.count_err(self.angle_destination,
                                                                       self.current_ang), self.current_ang)

            self.velocity_pub.publish(self.com_vel)
            self.rate.sleep()


if __name__ == '__main__':
    try:
        a = Turtle(1)
        a.move_turtle()
    except rospy.ROSInterruptException:
        pass
