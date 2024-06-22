#!/bin/zsh
# Automate the Boring Stuff with Python

import re

nameregex = re.compile(r'First name: (.*) Last name: (.*)') # Greedy pattern.

mtob1 = nameregex.search("First name: Eduardo Last name: Flores")

print(mtob1.group(1))
print(mtob1.group(2))

nongreedyregex = re.compile(r'<.*?>')

mtob2 = nongreedyregex.search("<To serve man> for dinner.>")

print(mtob2.group())

 
greedyregex = re.compile(r'<.*>')

mtob3 = greedyregex.search("<To serve man> for dinner.>")

print(mtob3.group())

nonewlineregex = re.compile(r'.*')

print(nonewlineregex.search(
    "Serve the public trust. \nProtect the innocent. \nUphold the Law."
    ).group()) # Only prints the first line.

newlineregex = re.compile(r'.*', re.DOTALL)

print(newlineregex.search(
    "Serve the public trust. \nProtect the innocent. \nUphold the Law."
    ).group()) # Prints all Lines.
