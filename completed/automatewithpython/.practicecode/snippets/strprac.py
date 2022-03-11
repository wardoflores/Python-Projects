#!/bin/zsh

b = "Hello, World!"
print(b[2:5]) # shows the chars 2 to 5 # Outputs llo

b = "Hello, World!"
print(b[-5:-2]) # Outputs orl

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" and strips unused whitespaces

a = "Hello, World!"
print(a.upper()) #  Returns the string in upper case

a = "Hello, World!"
print(a.replace("H", "J")) # Replaces a string with another string

a = ("Hello, World!")
print(a.split(",")) # Splits the string in to 2 strings with a "," comma to separate them

