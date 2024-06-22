#!/bin/zsh
# Automate the Boring Stuff with Python

import re

someregexvalue = re.compile(r'foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

mtob1 = someregexvalue.search("foo FOO FOFO FOOFOO peepee FOOFOO")
print(mtob1)
