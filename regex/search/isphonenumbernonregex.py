#!/bin/zsh
# Automate the Boring Stuff with Python

def isphonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
             return False
    return True


'''
print('415-555-4242 is a phone number: ')
print(isphonenumber('415-555-4242'))

print('moshi moshi is not a phone number: ')
print(isphonenumber('moshi moshi'))
'''

message = 'call me at 415-555-1011 tomorrow 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isphonenumber(chunk):
        print('Phone number found: ' + chunk)
        print('Done')
