# code a simple ui that schedules tasks;
from tkinter import *
from tkinter import ttk
# code a database to store those tasks;
import sqlite3
# organize the database to accomodate the various data types needed in the application
import sqlalchemy

root = Tk()
root.title("Task Scheduler")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding="100 100 100 100")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))