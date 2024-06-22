#!/bin/zsh
# Automate the Boring Stuff with Python

import re

wholestringisnum = re.compile(r'^]d+$')

mtob1 = wholestringisnum.search("1234567890")
mtob2 = wholestringisnum.search("12345xyz67890")


print(mtob1)
print(mtob2)
