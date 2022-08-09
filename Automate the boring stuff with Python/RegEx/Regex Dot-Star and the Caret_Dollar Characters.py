import re

# ^ means: has to match the pattern at the start of the string
beginsWithHelloRegex = re.compile(r"^Hello")
mo = beginsWithHelloRegex.search("Hello World")
print(mo.group())

mo = beginsWithHelloRegex.search("He said: Hello World")

# returns true because the strings does not start with Hello 
print(mo == None) 

# $ means: has to match the pattern at the end of the string
endsWithWorldRegex = re.compile(r"World$")
mo = endsWithWorldRegex.search("Hello World")
print(mo.group())

# the . means: every word except newline

atRegex = re.compile(r".at")
mo = atRegex.findall("The cat in the hat sat on the flat mat")
print(mo)

# the combination .* means: match anything
# .*? => non greedy match

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.findall("First Name: Bruno Last Name: dU")
print(mo)

# we can pass re.DOTALL as the second argument to re.compile() to make
# the . match new lines as well

# we can pass re.I as the second argument to re.compile() to make 
# the matching case insensitive