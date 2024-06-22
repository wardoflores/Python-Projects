#!/bin/zsh
# Automate the Boring Stuff with Python

import re

batregex = re.compile(r'Bat(wo)+man')

mtob1 = batregex.search("The adventure of Batwoman")
mtob2 = batregex.search("The adventure of Batwowowowoman")
mtob3 = batregex.search("The adventure of Batman")


print(mtob1.group())
print(mtob2.group())
print(mtob3.group())
