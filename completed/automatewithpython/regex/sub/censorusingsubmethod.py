import re

namesregex = re.compile(r'Agent \w+')

print(namesregex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

agentnamesregex = re.compile(r'Agent (\w)\w*')

print(agentnamesregex.sub(
    r'\1****', "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a Double Agent."
))