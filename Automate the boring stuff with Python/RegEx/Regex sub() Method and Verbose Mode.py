import re

namesRegex = re.compile(r"Agent \w+")
mo = namesRegex.findall("Agent Alice gave the secret docs to Agent Bob")
print(mo)

# the sub() method will substitute matches with some other text

mo = namesRegex.sub("REDACTED", "Agent Alice gave the secret docs to Agent Bob")
print(mo)

namesRegex = re.compile(r"Agent (\w)\w*")

mo = namesRegex.findall("Agent Alice gave the secret docs to Agent Bob")
print(mo)

# using \1, \2 etc. will substitute group 1, 2, etc. in the regex pattern

mo = namesRegex.sub(r"Agent \1****", "Agent Alice gave the secret docs to Agent Bob")
print(mo)

# vebose format

phoneRegex = re.compile(r"""
                        (\d\d\d-)|  # area code, whithout parens with dash
                        (\(\d\d\d\) )   # or area code with parens and no dash
                        \d\d\d      # first 3 digits
                        -           # second dash
                        \d\d\d\d    # last 4 digits
                        """, re.VERBOSE)

# if we want to pass multiple args to .compile we can combine them with |:
# .compile("", re.DOTALL | re.I | re.VERBOSE)