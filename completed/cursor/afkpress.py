#!/bin/zsh
# Description: Script for appearing active while idling.

import time
import pyautogui

while True:
    pyautogui.press('shift')
    time.sleep(5)
    print("pressing shift")
    pyautogui.press('shift')
    time.sleep(5)