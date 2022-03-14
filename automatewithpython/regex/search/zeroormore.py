#!/bin/zsh

import re

batregex = re.compile(r' Bat(wo)*man')

mtob1 = batregex.search("The adventures of Batman.")
mtob2 = batregex.search("The adventures of Batwoman")
mtob3 = batregex.search("The adventures of Batwowowowoman")


print(mtob1.group())
print(mtob2.group())
print(mtob3.group())



