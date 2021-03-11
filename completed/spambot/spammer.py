#! python3
import pyautogui, time
time.sleep(5)
f = open(r"C:\Users\Flores\Joey-vscode-workspaces\Python-Projects\.completed\spambot\navyspamtext.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


