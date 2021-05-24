#! python3
# source: youtube.com/watch?v=jBxRGcDmfWA

# pain.txt
# C:\Users\Flores\Joey-Repositories\Python-Projects\completed\spambot\pain.txt

# navyspam.txt
# C:\Users\Flores\Joey-Repositories\Python-Projects\completed\spambot\navyspamtext.txt

import pyautogui, time
time.sleep(5)
f = open(r"C:\Users\Flores\Joey-Repositories\Python-Projects\completed\spambot\navyspamtext.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


