#!/bin/zsh
# Simple Calculator GUI with Arithmetic features.
# Eduardo Jose Flores III: https://github.com/Coalemus
# Copyright (c) Eduardo Jose Flores III

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator GUI Choose Arithmetic:")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

## Listbox

# choices = ["addition", "subtraction", "multiplication"]
# choicesvar = StringVar(value=choices)
# arithmetics = Listbox(mainframe, listvariable=choicesvar, height=10).grid(column=1, row=1, sticky=(W))
# ...
# choices.append("peach")
# choicesvar.set(choices)

# arithmetics.selection_includes()
# arithmetics.see()

# arithmetics.bind("<<ListboxSelect>>", lambda e: updateDetails(arithmetics.curselection()))
# arithmetics.bind("<Double-1>", lambda e: invokeAction(arithmetics.curselection()))

## Radio

# arithmetics = StringVar()
# Addition = ttk.Radiobutton(mainframe, text='Addition', variable=arithmetics, value='Addition').grid(column=5, row=1, sticky=(W))
# Subtraction = ttk.Radiobutton(mainframe, text='Subtraction', variable=arithmetics, value='Subtraction').grid(column=5, row=2, sticky=(W))
# Multiplication = ttk.Radiobutton(mainframe, text='Multiplication', variable=arithmetics, value='Multiplication').grid(column=5, row=3, sticky=(W))

# if arithmetics == Addition:
#     addition()

def addition():

    def initadd():

        global rootadd
        global subaddframe

        root.title("Addition")

        subaddframe = ttk.Frame(root, padding="3 3 12 12")
        subaddframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(subaddframe, text="This addtion equation").grid(column=1, row=1, sticky=W)
        ttk.Label(subaddframe, text="is equivalent to").grid(column=1, row=3, sticky=E)

    initadd()

    def addcalculate(*args):
        
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
            root.bind("<Return>", addcalculate) # executes 2nd arg if Return is pressed.
        
        # rootadd.mainloop()

    addcalculate()

ToggleAddition = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Addition', 
	    command=addition, variable=ToggleAddition,
	    onvalue='ON', offvalue='OFF').grid(column=5, row=1, sticky=(W))

root.mainloop()

# ---