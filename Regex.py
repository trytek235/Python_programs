import re

txt = 'freeCodeCamp'
regex1 = '^freecodecamp$'

res = re.match(regex1, txt, re.IGNORECASE)

print(res)