#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymavlink import mavutil

# 시리얼 포트 또는 UDP 주소 설정
# 여기서는 UDP로 연결하는 예제입니다.
master = mavutil.mavlink_connection('/dev/ttyS0', baud=57600)

while True:
    try:
        # 드론으로부터 메시지 수신
        msg = master.recv_match()
        
        # None 값이 아닌 경우에만 출력
        if msg is not None:
            # 수신한 메시지 출력
            print(msg)
        
    except KeyboardInterrupt:
        # Ctrl+C를 눌러 종료할 때
        break
