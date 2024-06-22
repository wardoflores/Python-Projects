#!/bin/zsh
# pw.py - An insecure password locker program
# Automate the Boring Stuff with Python
import sys, pyperclip


CLIPBOARD = {'email' : 'F7dkioasdkKKjdo23ss9879s8789d8'
                'blog' : 'aowpekfapoeijfosd;kfgnoierw9e87sf986'
                'luggage' : '12345'}  

if en(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name.

if account in CLIPBOARD:
    print('Password for ' + account + 'copied to clipboard.')
else:
    print('There is no account named ' + account)  
