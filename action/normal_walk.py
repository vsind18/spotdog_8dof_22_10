#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float64

#init node control
rospy.init_node("8dof_controller")

#define publisher
pub_fr_hip = rospy.Publisher("/spotdog/fr_hip_controller/command", Float64, queue_size= 10)
pub_fr_knee = rospy.Publisher("/spotdog/fr_knee_controller/command", Float64, queue_size= 10)

pub_br_hip = rospy.Publisher("/spotdog/br_hip_controller/command", Float64, queue_size= 10)
pub_br_knee = rospy.Publisher("/spotdog/br_knee_controller/command", Float64, queue_size= 10)

pub_fl_hip = rospy.Publisher("/spotdog/fl_hip_controller/command", Float64, queue_size= 10)
pub_fl_knee = rospy.Publisher("/spotdog/fl_knee_controller/command", Float64, queue_size= 10)

pub_bl_hip = rospy.Publisher("/spotdog/bl_hip_controller/command", Float64, queue_size= 10)
pub_bl_knee = rospy.Publisher("/spotdog/bl_knee_controller/command", Float64, queue_size= 10)


    #flh-flk-frh-frk-blh-blk-brh-brk
motor_fl_hip = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_1.npy")
motor_fl_knee = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_2.npy")
motor_fr_hip = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_3.npy")
motor_fr_knee = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_4.npy")
motor_bl_hip = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_5.npy")
motor_bl_knee = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_6.npy")
motor_br_hip = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_7.npy")
motor_br_knee = np.load("/home/edw/spotdog8/src/spotdog/data/joint_angle_8.npy")

def send_commands(motor_angles):
    pub_fl_hip.publish(Float64(motor_angles[0]))
    pub_fl_knee.publish(Float64(motor_angles[1]))
    pub_fr_hip.publish(Float64(motor_angles[2]))
    pub_fr_knee.publish(Float64(motor_angles[3]))
    pub_bl_hip.publish(Float64(motor_angles[4]))
    pub_bl_knee.publish(Float64(motor_angles[5]))
    pub_br_hip.publish(Float64(motor_angles[6]))
    pub_br_knee.publish(Float64(motor_angles[7]))

rate = rospy.Rate(10)
i = 0

while not rospy.is_shutdown():
    motor_angles = np.array([motor_fl_hip[i], motor_fl_knee[i], motor_fr_hip[i], motor_fr_knee[i], motor_bl_hip[i], motor_bl_knee[i], motor_br_hip[i], motor_br_knee[i]])
    print(motor_angles)
    send_commands(motor_angles)

    i += 1
    rate.sleep()