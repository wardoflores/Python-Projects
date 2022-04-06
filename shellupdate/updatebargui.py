#!/bin/zsh

# Cant update config file, tkinter cant connect to display when running in sudo.

from tkinter import *
from tkinter import ttk

import os
import sys

disp = os.environ['DISPLAY'] # :0 # Works in non sudo
os.environ['DISPLAY'] = '' + disp


root = Tk()
root.title("Waybar message")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="100 20 100 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainframe, text="Write new phrase here (Reset Window Manager to display after): ").grid(column=1, row=0, sticky=W)

modifyword = StringVar()
modifyword_entry = ttk.Entry(mainframe, width=25, textvariable=modifyword)
modifyword_entry.grid(column=1, row=1, sticky=(W, E))

def modifywordfunc(*args):
    try:
        phrase = str(modifyword.get())
        barpath = "/home/joey/example.txt"
        assert(os.path.isfile(barpath))

        with open(barpath, "r", encoding="utf-8") as barconfig:
            customword = barconfig.readlines()
        
        prefix = "        \"format-alt\": "

        customword = (prefix + phrase + ",\n")

        with open(barpath, 'w', encoding='utf-8') as barconfig:
            barconfig.writelines(customword)

            newword.set("Phrase updated to: | " + phrase + " | successfully, restart Window Manager.")

            print("Successful, restart Window Manager.")

    except IOError:
        sys.stderr.write('Error: Failed to open file %s' % (barpath))

    except ValueError:
        pass

newword = StringVar()

ttk.Label(mainframe, textvariable=newword).grid(column=1, row=5, sticky=(W, E))

ttk.Button(mainframe, text="Modify", command=modifywordfunc).grid(column=1, row=4, sticky=W)

for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        modifyword_entry.focus()
        root.bind("<Return>", modifywordfunc) # executes 2nd arg if Return is pressed.

root.mainloop()
