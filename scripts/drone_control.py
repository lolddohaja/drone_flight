#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Drone control using MAVLink
'''

from pymavlink import mavutil
import keyboard
import time

val = [
    # x, y, z, r
    # x: pitch-related value of the drone, forward and backward movement related value.
    # y: roll-related value of the drone, left and right movement related value.
    # z: thrust-related value of the drone, up and down movement related value.
    # r: Yaw-related value of the drone, clockwise/counterclockwise rotation related value.
    [0, 0, 0, 0],  # land 0
    [250, 0, 500, 0],  # front 1
    [-250, 0, 500, 0],  # back 2
    [0, 250, 500, 0],  # right 3
    [0, -250, 500, 0],  # left 4
    [0, 0, 1000, 0],  # up 5
    [0, 0, 250, 0],  # down 6
    [0, 0, 500, 0]  # hold 7
]

master = mavutil.mavlink_connection('/dev/ttyS0', baud=57600)
master.wait_heartbeat()

print('Drone is connected!')

while True:
    if keyboard.is_pressed('d'):
        print('Start!')
        master.mav.command_long_send(master.target_system, master.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)
        print("Waiting for the vehicle to arm")
        master.motors_armed_wait()
        print('Armed!')
    if keyboard.is_pressed('f'):
        print('Stop!')
        master.mav.command_long_send(master.target_system, master.target_component, mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 0, 0, 0, 0, 0, 0, 0)
        master.motors_disarmed_wait()
    if keyboard.is_pressed('left'):
        print('Press Left!')
        master.mav.manual_control_send(master.target_system, val[4][0], val[4][1], val[4][2], val[4][3])
    if keyboard.is_pressed('right'):
        print('Press Right!')
        master.mav.manual_control_send(master.target_system, val[3][0], val[3][1], val[3][2], val[3][3])
    if keyboard.is_pressed('up'):
        print('Press Front!')
        master.mav.manual_control_send(master.target_system, val[1][0], val[1][1], val[1][2], val[1][3])
    if keyboard.is_pressed('down'):
        print('Press Back!')
        master.mav.manual_control_send(master.target_system, val[2][0], val[2][1], val[2][2], val[2][3])
    if keyboard.is_pressed('space'):
        print('Press Space bar!')
        master.mav.manual_control_send(master.target_system, val[6][0], val[6][1], val[6][2], val[6][3])
    if keyboard.is_pressed('ctrl'):
        print('Press Control!')
        master.mav.manual_control_send(master.target_system, val[7][0], val[7][1], val[7][2], val[7][3])
    time.sleep(0.085)
