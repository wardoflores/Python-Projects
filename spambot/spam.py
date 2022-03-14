#!/bin/zsh
# source: youtube.com/watch?v=jBxRGcDmfWA
# source: youtube.com/watch?v=-zd1UI2JTuk

import pyautogui, time
from pynput import keyboard 
import sys

text = "Pog"

def on_press(key):
    if '{0}'.format(key) == "Key.esc":
        sys.exit()
    elif '{0}'.format(key) == "Key.enter":
        # for word in f:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        time.sleep(0)        
    
with keyboard.Listener(on_press=on_press) as Listener:
    Listener.join()