#!/bin/zsh
# Simple Calculator GUI with Arithmetic features.
# Eduardo Jose Flores III: https://github.com/Coalemus
# Copyright (c) Eduardo Jose Flores III

from tkinter import *
from tkinter import ttk

# def initadd():

#     global rootadd
#     global subaddframe

root = Tk()
root.title("Calculator GUI Choose Arithmetic:")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

window = Toplevel(root)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

def addcalculate(*args):

    rootadd = Tk()
    rootadd.title("Addition")
    rootadd.columnconfigure(0, weight=1)
    rootadd.rowconfigure(0, weight=1)

    subaddframe = ttk.Frame(rootadd, padding="3 3 12 12")
    subaddframe.grid(column=0, row=0, sticky=(N, W, E, S))

    ttk.Label(subaddframe, text="This addtion equation").grid(column=1, row=1, sticky=W)
    ttk.Label(subaddframe, text="is equivalent to").grid(column=1, row=3, sticky=E)

    addequation = StringVar()
    addequation_entry = ttk.Entry(subaddframe, width=7, textvariable=addequation)
    addequation_entry.grid(column=2, row=1, sticky=(W, E))

    addequation2 = StringVar()
    addequation_entry2 = ttk.Entry(subaddframe, width=7, textvariable=addequation2)
    addequation_entry2.grid(column=2, row=2, sticky=(W, E))

    def addcalculated(*args):
        try:
            value = float(addequation.get()) # have prompt for what equation type to get and have prompts to add entries with choice of arithmetic.
            value2 = float(addequation2.get())
            addresult.set(int(value + value2)) # Convert to arithmetic specific to choice.
        except ValueError:
            pass

    addresult = StringVar()

    ttk.Label(subaddframe, textvariable=addresult).grid(column=2, row=3, sticky=(W, E))

    ttk.Button(subaddframe, text="Add", command=addcalculated).grid(column=3, row=3, sticky=W)
    
    for child in subaddframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        addequation_entry.focus()
        rootadd.bind("<Return>", addcalculate) # executes 2nd arg if Return is pressed.
    
    rootadd.mainloop()

ttk.Button(mainframe, text="Add", command=addcalculate).grid(column=3, row=3, sticky=W)

root.mainloop()

# ---