#!/bin/zsh
# Automate the Boring Stuff with Python

while True:
    OldmanAge = input()

    def AgetoDays(age):
        result = int(age) * 365
        return result

    print(AgetoDays(OldmanAge))
    break
