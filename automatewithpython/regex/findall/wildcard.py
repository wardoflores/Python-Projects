#!/bin/zsh

import re

atregex = re.compile(r'.at')

mtob1 = atregex.search("The cat in the hat sat on the flat mat.")

print(mtob1)