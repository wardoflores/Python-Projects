#!/bin/zsh
# Automate the Boring Stuff with Python

import os

print(os.path.join('Users', 'Flores', 'vscode'))

myfiles = ['accounts.txt', 'details.csv', 'invite.docx']

for filename in myfiles:
    print(os.path.join('C:\\Users\\Flores\\', filename))
