import pyautogui
import time

# Buggy on Linux Sway WM.

while True:
        
    pyautogui.moveTo(720, 100, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds
    time.sleep(3) # Breathing room for errors
    pyautogui.moveTo(720, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds

