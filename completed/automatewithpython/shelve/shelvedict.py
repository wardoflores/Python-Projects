#!/bin/zsh

import shelve

shelffile = shelve.open('mydata')

print(list(shelffile.keys()))
print(list(shelffile.values()))

shelffile.close()