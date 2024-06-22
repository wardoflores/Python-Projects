#!/bin/zsh
# bulletpointadder.py - Adds Wikipedia bullet points to the
#  start # of each line of text on the clipboard.
# Automate the Boring Stuff with Python

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)

