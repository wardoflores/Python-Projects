#!/bin/zsh
# Automate the Boring Stuff with Python

import re

heroregex = re.compile(r'Batman|Tina Fey')

mtob1 = heroregex.search('Batman and Tina Fey.')

print(mtob1.group())

mtob2 = heroregex.search('Tina Fey and Batman.')

print(mtob2.group())

batregex = re.compile(r'Bat(man|mobile|copter|bat)')

mtob3 = batregex.search('Batmobile lost a wheel')

print(mtob3.group())
