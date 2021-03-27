#! python3
# source: youtube.com/watch?v=jBxRGcDmfWA


import pyautogui, time

time.sleep(1) # Lowered because of lower text filesize.
while True:
    f = open(r"C:\Users\Flores\Joey-Repositories\Python-Projects\completed\spambot\simplespam.txt", "r")

    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")

    if KeyboardInterrupt:
        False
