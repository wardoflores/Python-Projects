#!/bin/zsh
# Description: Prints Download speed and Upload speed.

import speedtest as speedtest
import time
import datetime

if __name__ == '__main__':

    try:
        s = speedtest.Speedtest()

    except ConfigRetrievalError:
        print("No connection.")

    time_now = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)


        print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
     