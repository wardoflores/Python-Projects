#! python3
import pyautogui, time

time.sleep(1) # Lowered because of lower text filesize.
f = open(r"C:\Users\Flores\Joey-vscode-workspaces\Python-Projects\.completed\spambot\simplespam.txt", "r")

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
