#!/bin/zsh
# Description: Script for appearing active while idling.

import time
import pyautogui

while True:
    pyautogui.press('shift')
    time.sleep(5)
    print("pressing shift in 5 sec intervals")
    pyautogui.press('shift')
    time.sleep(5)