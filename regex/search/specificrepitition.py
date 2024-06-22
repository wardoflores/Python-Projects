#!/bin/zsh
# Automate the Boring Stuff with Python

import re

haregex = re.compile(r'(Ha){3}')

mtob1 = haregex.search("HaHaHa")
mtob2 = haregex.search("Ha")


print(mtob1.group())
print(mtob2.group())
