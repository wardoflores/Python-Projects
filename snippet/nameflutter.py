#!/bin/zsh
# Automate the Boring Stuff with Python

name = str(input("what is your name: "))

def process(name):
    print("Oh hey there,")
    for i in name:
        print("* * * " + i + " * * *")

process(name)
