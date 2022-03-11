#!/bin/zsh

import re

phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mtob = phone_number_regex.search('my number is 415-555-4242.')

print(mtob.groups())

areacode, mainnumber = mtob.groups()
print(areacode); print(mainnumber)

print(mtob.group())
print(mtob.group(0))

print(mtob.group(1))
print(mtob.group(2))