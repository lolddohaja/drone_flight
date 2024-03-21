#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymavlink import mavutil

def print_vfr_hud():
    master = mavutil.mavlink_connection('/dev/ttyS0', baud=57600)
    while True:
        try:
            msg = master.recv_match()
            if msg is not None and msg.get_type() == 'VFR_HUD':
                print(msg)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    print_vfr_hud()
