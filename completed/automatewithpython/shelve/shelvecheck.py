#!/bin/zsh

import shelve

shelffile = shelve.open('mydata')

print(type(shelffile))
print(shelffile['cats'])

shelffile.close()