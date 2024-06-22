#!/bin/zsh
# Automate the Boring Stuff with Python

import shelve

shelffile = shelve.open('mydata')

print(type(shelffile))
print(shelffile['cats'])

shelffile.close()
