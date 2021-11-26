import pyautogui
import time

# Only works in Code editor window when using Sway WM.

while True:
        
    pyautogui.scroll(10)   # scroll up 10 "clicks"
    time.sleep(3)
    pyautogui.scroll(-10)  # scroll down 10 "clicks"