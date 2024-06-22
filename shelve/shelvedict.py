#!/bin/zsh
# Automate the Boring Stuff with Python

import shelve

shelffile = shelve.open('mydata')

print(list(shelffile.keys()))
print(list(shelffile.values()))

shelffile.close()
