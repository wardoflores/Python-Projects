#!/bin/zsh
# Automate the Boring Stuff with Python

import re

batregex = re.compile(r'Bat(wo)?man')

mtob1 = batregex.search("The adventures of Batman.")

print(mtob1.group())

mtob2 = batregex.search("The adventures of Batwoman.")

print(mtob2.group())

