import re

phoneRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")

# the .search() method returns only the first match
# we can use the .findall() method to find all mathes in a string
# and returns a list of strings with the matches


mo = phoneRegex.findall("""Incredibly long text with several phone numbers
                        555-142-4124 332-123-4142, 123-412-4568""")
print(mo)


# or returns a tuple if the expressions has two or more groups
phoneRegex = re.compile(r"((\d\d\d-)(\d\d\d-)(\d\d\d\d))")
mo = phoneRegex.findall("""Incredibly long text with several phone numbers
                        555-142-4124 332-123-4142, 123-412-4568""")
print(mo)

# Common char classes:
# \d => any numeric digit in [0;9]
# \D => any char that is NOT a digit from [0;9]
# \w => any letter, numeric digit, or the underscore char
# \W => any char that is NOT letter, numeric digit, or the underscore char
# \s => any space, tab, or newline char
# \S => any char that is NOT a space, tab, or newline char

vowelRegex = re.compile(r"[aeiouAEIOU]")
mo = vowelRegex.findall("Robocop eats baby food.")
print(mo) # returs all the vowels

consonantsRegex = re.compile(r"[^aeiouAEIOU]") # with the ^ char we can negate the regex
mo = vowelRegex.findall("Robocop eats baby food.")
print(mo) # returns all the consonants