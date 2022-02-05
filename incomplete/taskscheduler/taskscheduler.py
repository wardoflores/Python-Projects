# code a simple ui that schedules tasks;
from tkinter import *
from tkinter import ttk
# code a database to store those tasks;
import sqlite3
# organize the database to accomodate the various data types needed in the application
# import sqlalchemy

root = Tk()
root.title("Task Scheduler")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

titleframe = ttk.Frame(mainframe).grid(column=1, row=1, sticky=(N))
label = ttk.Label(titleframe, text='Task Scheduler').grid()

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()





root.mainloop()