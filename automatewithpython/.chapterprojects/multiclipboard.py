#!/bin/zsh

'''
Say you have the boring task of filling out many forms in a web page or
software with several text fields. 
The clipboard saves you from typing the same text over and over again. 
But only one thing can be on the clipboard at a time. 
If you have several different pieces of text that you need to copy and paste,
you have to keep highlighting and copying the same few things over and over again.

You can write a Python program to keep track of multiple pieces of text. 
This “multiclipboard” will be named mcb.pyw 
(since “mcb” is shorter to type than “multiclipboard”).
The .pyw extension means that Python won’t show a Terminal window when it runs this program. 
(See Appendix B for more details.)

The program will save each piece of clipboard text under a keyword. 
For example, when you run py mcb.pyw save spam, the current contents of the clipboard
will be saved with the keyword spam. 
This text can later be loaded to the clipboard again by running py mcb.pyw spam. 
And if the user forgets what keywords they have, they can run py mcb.pyw list
to copy a list of all keywords to the clipboard.

Here’s what the program does:

The command line argument for the keyword is checked.
If the argument is save
, then the clipboard contents are saved to the keyword.
If the argument is list
, then all the keywords are copied to the clipboard.
Otherwise, the text for the keyword is copied to the keyboard.

This means the code will need to do the following:

Read the command line arguments from sys.argv
.
Read and write to the clipboard.
Save and load to a shelf file.

If you use Windows, you can easily run this script from the Run... window 
by creating a batch file named mcb.bat with the following content:

@pyw.exe C:\Python34\mcb.pyw %*

Step 1: Comments and Shelf Setup

Let’s start by making a skeleton script with some comments and basic setup. 
Make your code look like the following:

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
➊ # Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
   #        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
   #        py.exe mcb.pyw list - Loads all keywords to clipboard.

➋ import shelve, pyperclip, sys

➌ mcbShelf = shelve.open('mcb')

   # TODO: Save clipboard content.

   # TODO: List keywords and load content.

   mcbShelf.close()

It’s common practice to put general usage information in comments at the top of the file ➊.
If you ever forget how to run your script, you can always look at these comments for a reminder.
Then you import your modules ➋. Copying and pasting will require the pyperclip module,
and reading the command line arguments will require the sys module. 
The shelve module will also come in handy: 
Whenever the user wants to save a new piece of clipboard text, you’ll save it to a shelf file.
Then, when the user wants to paste the text back to their clipboard,
you’ll open the shelf file and load it back into your program. 
The shelf file will be named with the prefix mcb ➌.

Step 2: Save Clipboard Content with a Keyword

The program does different things depending on whether the user wants to save text to a keyword,
load text into the clipboard, or list all the existing keywords. 
Let’s deal with that first case. Make your code look like the following:

   #! python3
   # mcb.pyw - Saves and loads pieces of text to the clipboard.
   --snip--

   # Save clipboard content.
➊ if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
➋         mcbShelf[sys.argv[2]] = pyperclip.paste()
   elif len(sys.argv) == 2:
➌    # TODO: List keywords and load content.

   mcbShelf.close()

If the first command line argument (which will always be at index 1
of the sys.argvlist) is 'save'➊, the second command line argument is the keyword for
the current content of the clipboard.

The keyword will be used as the key for mcbShelf, and the value will be
the text currently on the clipboard ➋.

If there is only one command line argument, you will assume it is either 'list'
or a keyword to load content onto the clipboard. You will implement that code later.
For now, just put a TODO comment there ➌.
'''