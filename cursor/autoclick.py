#!/bin/zsh
# Description: Auto Clicker. Press '=' For start and stop and '-' for exit.
# Edit 'delay' variable for Click rate.
# Only works in Code editor window when using Sway WM.

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

 
delay = 0.001 # Edit for rate of clicks
button = Button.left
start_stop_key = KeyCode(char='=')
exit_key = KeyCode(char='-')

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True
 
    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_run = False
 
    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)
 
def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()

if __name__ == "__main__":
    with Listener(on_press=on_press) as listener:
        listener.join()