# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:24:23 2020

@author: fidelismwansa
"""

import time

#******************************************
#   Journey Tracking & Logging
#******************************************


def journey_plt(server, my_id):
    trip = {'coordinates': [], 'speed': [], 'time': []}
    crd = []
    spd = []
    tme = []
    # Read power Pin
    power = 0
    # Updates every x seconds to track position of vehicle
    while power != 0:
        # Get the current time
        tme.append(time.time)
        # Read Position Pin
        crd.append(position=[1, 1])
        # Read Position Pin
        spd.append(speed=0)
        # Read Power Pin
        power = 0
        # Update Position to server
        server.myposition(my_id)
        # Wait for x seconds
        time.sleep(0.5)

    # On Exit set trip parameters
    trip['cooridnates'] = crd
    trip['speed'] = spd
    trip['time'] = tme
    # Send Data to server
    server.mylog(my_id, trip)
