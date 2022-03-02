import re

haregex = re.compile(r'(Ha){3,5}')
mtob1 = haregex.search("HaHaHaHaHa")

haregexnon = re.compile(r'(Ha){3,5}?')
mtob2 = haregexnon.search("HaHaHaHaHa")

print(mtob1.group())
print(mtob2.group())