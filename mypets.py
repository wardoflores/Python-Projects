#!/bin/zsh
# Automate the Boring Stuff with Python

mypets = ["Susie", "Oreo", "Po"]
print("Enter a pet name: ")
name = input()
if name not in mypets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")
