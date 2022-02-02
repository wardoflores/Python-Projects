#!/bin/zsh
# Description: Script for appearing active while idling.

import time
import pyautogui

while True:
    pyautogui.press('F13')
    time.sleep(5)
    pyautogui.press('F13')
    time.sleep(5)