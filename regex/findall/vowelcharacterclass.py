#!/bin/zsh
# Automate the Boring Stuff with Python

import re

vowelregex = re.compile(r'[aeiouAEIOU]')

mtob1 = vowelregex.findall("Roboop eats baby food. BABY FOOD.")

print(mtob1)
