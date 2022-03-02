import re

phoneregex = re.compile(
    r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)'
    )

phoneregverbose = re.compile(
    r'''((\d{3}|\(\d{3}\))? # Area code 
    (\s|-|\.)? # Separator
    \d{3} # first 3 digits
    (\s|-|\.) # separator
    \d{4} # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension 
    )''', re.VERBOSE
    )