#!/bin/zsh

# Moves cursor focus around on linux but the cursor icon doesn't move along.

import pyautogui
import time

while True:
        
    pyautogui.moveTo(720, 100, 7)   # moves mouse to X of 100, Y of 200 over 2 seconds
    time.sleep(3) # Breathing room for errors
    pyautogui.moveTo(480, 500, 7)   # moves mouse to X of 100, Y of 200 over 2 seconds