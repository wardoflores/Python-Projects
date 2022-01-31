#!/bin/zsh
# Simple Calculator GUI with Arithmetic features.
# Eduardo Jose Flores III: https://github.com/Coalemus
# Copyright (c) Eduardo Jose Flores III

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

def addcalculate(*args):
    try:
        value = float(addequation.get()) # have prompt for what equation type to get and have prompts to add entries with choice of arithmetic.
        value2 = float(addequation2.get())
        addresult.set(int(value + value2)) # Convert to arithmetic specific to choice.
    except ValueError:
        pass

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

addequation = StringVar()
addequation_entry = ttk.Entry(mainframe, width=7, textvariable=addequation)
addequation_entry.grid(column=2, row=1, sticky=(W, E))

addequation2 = StringVar()
addequation_entry2 = ttk.Entry(mainframe, width=7, textvariable=addequation2)
addequation_entry2.grid(column=2, row=2, sticky=(W, E))

addresult = StringVar()
ttk.Label(mainframe, textvariable=addresult).grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Add", command=addcalculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="This addtion equation").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="solution").grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
addequation_entry.focus()
root.bind("<Return>", addcalculate)

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

def runtime():

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            # break
            # Add break if you only want to execute code once, 
            # left it off because it auto terminates when initiated in the Terminal.
        else:
            print("Invalid Input")

        end = input("if you want to exit, type 1: ")
        if end == '1':
            return exit()
        else:
            runtime()

runtime()

root.mainloop()