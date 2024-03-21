#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymavlink import mavutil

def print_rc_channels_raw():
    master = mavutil.mavlink_connection('/dev/ttyS0', baud=57600)
    while True:
        try:
            msg = master.recv_match()
            if msg is not None and msg.get_type() == 'RC_CHANNELS_RAW':
                print(msg)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print_rc_channels_raw()