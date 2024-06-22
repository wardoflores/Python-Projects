#!/bin/zsh
# Automate the Boring Stuff with Python

import re

phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mtob1 = phonenumregex.search("Cell: 415-555-9999 Work: 212-555-0000") # Search method
mtob2 = phonenumregex.findall("Cell: 415-555-9999 Work: 212-555-0000") # Findallllll method

print(mtob1.group())
print(mtob2) # group method returns Error. Even if pattern has groups.
