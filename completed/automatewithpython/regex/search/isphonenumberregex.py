#!/bin/zsh

import re

phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mtob = phone_number_regex.search('my number is 415-555-4242.')

print("Phone number found: " + mtob.group())