#!/usr/bin/env python

# Must be run from the examples folder
import sys
sys.path.append('..')

import time

import liquidtap

# Add a logging handler so we can see the raw communication data
import logging
root = logging.getLogger()
root.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
root.addHandler(ch)

global tap

def update_callback(data):
    print(data)

if __name__ == '__main__':


    tap = liquidtap.Client(821826, '+RJdKszJ/kWOAMhZKvAWzMJ3sWvuZduygBkH/h04pzzye8QeP81BwfKDkLR7egNOHvn5jwm1Jm6sbwmUhKT7fw==')
    tap.pusher.connect()

    channel = tap.subscribe("product_cash_usdjpy_5")

    channel.bind('my_event', update_callback)

    while True:
        time.sleep(1)
