#! python3
import pyautogui, time
time.sleep(5)
f = open("C:\\Users\\Flores\\Joey-vscode-workspaces\\General-Python-Repository\\.desktopapps\\.completed\\spambot\\navyspamtext.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")


