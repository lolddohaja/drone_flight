#!/usr/bin/env python3
'''
Check bandwidth of link
'''
from pymavlink import mavutil


# Create a MAVLink serial instance
master = mavutil.mavlink_connection('/dev/ttyS0', baud=57600)

# Wait for the first heartbeat
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

# Once connected, you can use 'connection' to get and send messages
