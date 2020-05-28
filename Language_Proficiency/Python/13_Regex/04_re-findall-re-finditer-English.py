import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
# look behind for consonant, find 2 or more vowels, lookahead for consonant, case insensitive
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))