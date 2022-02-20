#!/bin/bash
# Source: https://pythonguides.com/python-tkinter-todo-list/

# code a simple ui that schedules tasks;
from tkinter import *
from tkinter import messagebox

# In this function, we have stored the value of the entry box in the task variable
# get() method is used to pull the value provided by the user in the entry box.
# If-else condition is applied to avoid black space entry in the Listbox.
# if the task does not have blank space then only it will allow it to store the information in the Listbox otherwise it will display a warning message box informing the user that the entry box can’t be empty.
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

# Here ANCHOR refers to the selected item in the Listbox.
# lb variable assigned to Listbox
# delete is a built-in function to delete Listbox item.
# User will select the item in the Listbox and then to trigger this function he/she will click on the deleteTask button. Immediately the item will disappear from the Listbox.
def deleteTask():
    lb.delete(ANCHOR)
    
# parent window
ws = Tk()

# the width refers to the horizontal space of the window.
# height refers to the vertical space of the window.
# x-position refers to the position of the window on the display over the x-axis.
# y-position refers to the position of the window on the display over the y-axis.
ws.geometry('500x450+500+200') 

ws.title('Todo App')

# background color to the window
ws.config(bg='#223441')

# false for both height and width that means the window can’t be resized.
ws.resizable(width=False, height=False)

# Frame widgets are used to hold other widgets.
# They help in keeping & maintaining user interface (UI) & user experience (UX) clean & organized.


# Another benefit of placing a frame is now we will add scrollbars to the frame and that solves our purpose.
# Scrollbars are no easy to place but using frames we can do it in no time.
# pady=10 means we have added extra padding around the frame from outside.

frame = Frame(ws)
frame.pack(pady=10)


# place Listbox, scrollbars & buttons inside the frame.
# So in this way frame will act as an additional window over the parent window.

# lb is the variable name for storing Listbox.
# Listbox is placed on the frame window.
# width: Horizontal space provided is 25.
# height: 8 rows in the vertical position are provided.
# font: Times New Roman font is provided with 14 sizes.
# bd = 0 refers to the border is zero
# fg is the foreground color or the text color.
# highlightthickness=0 every time the focus is moved to any item then it should not show any movement that is value 0 value is provided. by default it has some value.
# selectbackground it decides the color of the focused item in the Listbox.
# activestyle=”none” removes the underline that appears when the item is selected or focused.
# geometry manager used is pack()
# side=LEFTthis will keep the Listbox to the left side of the frame. We did this on purpose so that we can assign the right position to scrollbars.
# fill=BOTH this will fill the blank space in both the directions that are x and y
lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

# We have added dummy data so that the application is ready to view. You add or delete whatever data you want.
# the data is in a list format and is stored in a variable named task_list.
task_list = [
    'Eat apple',
    'drink water',
    'go gym',
    'write software',
    'write documentation',
    'take a nap',
    'Learn something',
    'paint canvas'
    ]

# for loop is used to insert data in the Listbox.
# every time loop runs it adds an item to the Listbox & this process keeps on going until all the items in the task_list are inserted.
# lb.insert(END, item) this command stacks the items in Listbox.
# lb is the variable used for Listbox
# insert is a built-in method of Listbox to insert data.
# END signifies that a new item will be added in the end. If END is replaced with 0 then new data will be added at the top.
# item is the list item from task_list
for item in task_list:
    lb.insert(END, item)

# Scrollbars are used so that users can scroll the information that is placed in a limited size on the window.
# In this scrollbars are placed on a frame and the variable assigned is sb
# The geometry method used is a pack() so that everything remains dynamic and in a sequence.
# side=RIGHT we have placed scrollbars on the right side of the frame.
# In the above code, we have provided side=LEFT to Listbox. So in this way, both the widgets are assigned paralleled.
# fill=BOTH this will fill the blank space in both the directions that are x and y
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

# lb.config(yscrollcommand=sb.set) here we have assigned a purpose to the scrollbar. In other words, we have bind Listbox with scrollbar
# sb.config(command=lb.yview), here yview means scrollbar will go in the vertical direction. If it would have been xview then the scrollbar would have worked in the horizontal direction.
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

# Entry box is used to take input from the user.
# ws: entry box is placed on the parent window
# font: provides font name i.e ‘Times New Roman’ and size is 14
# Geometry manager used is pack with padding of 20 outside the widget
my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)


# Frames are used to organise the widgets. We have used separate frame for buttons.
button_frame = Frame(ws)
button_frame.pack(pady=20)

# Buttons are placed to trigger some action when pressed.
# Here we have created two button (addTask & deleteTask). Both of them have same features and look accept the background color and command.
# Command: When button is clicked the the function mentioned in command is called. In this case if user clicks on addTask_btn button then newTask function is called & when user clicks on the delTask_btn Button then delTask function is called.
addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()