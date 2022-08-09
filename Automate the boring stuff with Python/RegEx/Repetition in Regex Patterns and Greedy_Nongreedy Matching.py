import re

# the "?" says to the regex 
# <match the preceding group 0 or 1 times each>

batRegex = re.compile(r"Bat(wo)?man") #the group (wo) can appear 0 or 1 times to match the pattern
mo = batRegex.search("The adventures of Batman")
print(mo.group())
mo = batRegex.search("The adventures of Batwoman")
print(mo.group())

phoneRegex = re.compile(r"(\d\d\d)?\d\d\d-\d\d\d\d") # the area code is optional
mo = phoneRegex.search("555-4789")
print(mo.group())


# the star char "*" means <match zero or more times>

batRegex = re.compile(r"Bat(wo)*man") # matches for zero or more repetitions of the (wo)
mo = batRegex.search("The adventures of Batwowowowoman")
print(mo.group())

# the star char "+" means <match one or more times>

batRegex = re.compile(r"Bat(wo)+man") # matches for one or more repetitions of the (wo)
mo = batRegex.search("The adventures of Batwowowowoman")
print(mo.group())
mo = batRegex.search("The adventures of Batman") #will not match anything


# the {number} grants us to match for a finite number of times

haRegex = re.compile(r"(ha){3}")
mo = haRegex.search("He said: hahahaha")
print(mo.group())

# this way we can match more things in a row

phoneRegex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(,| )?){3}") 
mo = phoneRegex.search("My numbers are: 555-4789,338-391-1254 368-578-1045")
print(mo.group())

# we can also add another number to the braces, to match from a min to a max
haRegex = re.compile(r"(ha){3,5}")
mo = haRegex.search("He said: hahahaha")
print(mo.group())

# by default RegEx does greedy matches, tries to match the maximum possible
digitRegex = re.compile(r"(\d){3,5}")
mo = digitRegex.search("1234567890")
print(mo.group()) # shows us the first match and with 5 digits: 12345

# we can do NON greedy matching by specifying a ? after the curly braces
digitRegex = re.compile(r"(\d){3,5}?")
mo = digitRegex.search("1234567890")
print(mo.group()) # shows us: 123