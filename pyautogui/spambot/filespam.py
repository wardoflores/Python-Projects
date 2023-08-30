#!/bin/zsh
# source: youtube.com/watch?v=jBxRGcDmfWA

# pain.txt
# /home/joey/coalemus/Python-Projects/spambot/pain.txt

# navyspam.txt
# /home/joey/coalemus/Python-Projects/spambot/navyspamtext.txt

import pyautogui, time
time.sleep(5)
f = open("/home/joey/coalemus/Python-Projects/spambot/pain.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")