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

def addition():

    def initadd():

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

    addcalculate()

def subtraction():

    def initsub():

        global subsubframe

        root.title("Subtraction")

        subsubframe = ttk.Frame(root, padding="3 3 12 12")
        subsubframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(subsubframe, text="This subtraction equation").grid(column=1, row=1, sticky=W)
        ttk.Label(subsubframe, text="is equivalent to").grid(column=1, row=3, sticky=E)

    initsub()

    def subcalculate(*args):
        
        subequation = StringVar()
        subequation_entry = ttk.Entry(subsubframe, width=7, textvariable=subequation)
        subequation_entry.grid(column=2, row=1, sticky=(W, E))

        subequation2 = StringVar()
        subequation_entry2 = ttk.Entry(subsubframe, width=7, textvariable=subequation2)
        subequation_entry2.grid(column=2, row=2, sticky=(W, E))

        def subcalculated(*args):
            try:
                value = float(subequation.get()) # have prompt for what equation type to get and have prompts to sub entries with choice of arithmetic.
                value2 = float(subequation2.get())
                subresult.set(int(value - value2)) # Convert to arithmetic specific to choice.
            except ValueError:
                pass

        subresult = StringVar()

        ttk.Label(subsubframe, textvariable=subresult).grid(column=2, row=3, sticky=(W, E))

        ttk.Button(subsubframe, text="Subtract", command=subcalculated).grid(column=3, row=3, sticky=W)
        
        for child in subsubframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            subequation_entry.focus()
            root.bind("<Return>", subcalculate) # executes 2nd arg if Return is pressed.

    subcalculate()

def multiplication():

    def initmulti():

        global submultiframe

        root.title("multiplication")

        submultiframe = ttk.Frame(root, padding="3 3 12 12")
        submultiframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(submultiframe, text="This multiplication equation").grid(column=1, row=1, sticky=W)
        ttk.Label(submultiframe, text="is equivalent to").grid(column=1, row=3, sticky=E)

    initmulti()

    def multicalculate(*args):
        
        multiequation = StringVar()
        multiequation_entry = ttk.Entry(submultiframe, width=7, textvariable=multiequation)
        multiequation_entry.grid(column=2, row=1, sticky=(W, E))

        multiequation2 = StringVar()
        multiequation_entry2 = ttk.Entry(submultiframe, width=7, textvariable=multiequation2)
        multiequation_entry2.grid(column=2, row=2, sticky=(W, E))

        def multicalculated(*args):
            try:
                value = float(multiequation.get()) # have prompt for what equation type to get and have prompts to multi entries with choice of arithmetic.
                value2 = float(multiequation2.get())
                multiresult.set(int(value * value2)) # Convert to arithmetic specific to choice.
            except ValueError:
                pass

        multiresult = StringVar()

        ttk.Label(submultiframe, textvariable=multiresult).grid(column=2, row=3, sticky=(W, E))

        ttk.Button(submultiframe, text="multitract", command=multicalculated).grid(column=3, row=3, sticky=W)
        
        for child in submultiframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            multiequation_entry.focus()
            root.bind("<Return>", multicalculate) # executes 2nd arg if Return is pressed.

    multicalculate()

def division():

    def initdiv():

        global subdivframe

        root.title("division")

        subdivframe = ttk.Frame(root, padding="3 3 12 12")
        subdivframe.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(subdivframe, text="This division equation").grid(column=1, row=1, sticky=W)
        ttk.Label(subdivframe, text="is equivalent to").grid(column=1, row=3, sticky=E)

    initdiv()

    def divcalculate(*args):
        
        divequation = StringVar()
        divequation_entry = ttk.Entry(subdivframe, width=7, textvariable=divequation)
        divequation_entry.grid(column=2, row=1, sticky=(W, E))

        divequation2 = StringVar()
        divequation_entry2 = ttk.Entry(subdivframe, width=7, textvariable=divequation2)
        divequation_entry2.grid(column=2, row=2, sticky=(W, E))

        def divcalculated(*args):
            try:
                value = float(divequation.get()) # have prompt for what equation type to get and have prompts to div entries with choice of arithmetic.
                value2 = float(divequation2.get())
                divresult.set(int(value / value2)) # Convert to arithmetic specific to choice.
            except ValueError:
                pass

        divresult = StringVar()

        ttk.Label(subdivframe, textvariable=divresult).grid(column=2, row=3, sticky=(W, E))

        ttk.Button(subdivframe, text="divtract", command=divcalculated).grid(column=3, row=3, sticky=W)
        
        for child in subdivframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
            divequation_entry.focus()
            root.bind("<Return>", divcalculate) # executes 2nd arg if Return is pressed.

    divcalculate()

ToggleAddition = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Addition', 
	    command=addition, variable=ToggleAddition,
	    onvalue='ON', offvalue='OFF').grid(column=5, row=6, sticky=(W))

ToggleSubtraction = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Subtraction', 
	    command=subtraction, variable=ToggleSubtraction,
	    onvalue='ON', offvalue='OFF').grid(column=5, row=7, sticky=(W))

ToggleMultiplication = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Multiplication', 
	    command=multiplication, variable=ToggleMultiplication,
	    onvalue='ON', offvalue='OFF').grid(column=5, row=8, sticky=(W))

ToggleDivision = StringVar()
check = ttk.Checkbutton(mainframe, text='Use Division', 
	    command=division, variable=ToggleDivision,
	    onvalue='ON', offvalue='OFF').grid(column=5, row=9, sticky=(W))

root.mainloop()

# ---