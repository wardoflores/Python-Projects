#!/bin/zsh

import re

robocop = re.compile(r'robocop', re.I)

print(robocop.search("Robocop is parrt man, machine, all cop.").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
