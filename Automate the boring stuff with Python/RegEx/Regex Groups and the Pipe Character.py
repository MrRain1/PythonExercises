import re #regex library

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is 415-555-4242')
print(matchObject.group())

# suppose we want only the area code or some other group of digits
# we can filter them by grouping them with parenthesis

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 415-555-4242')

print(matchObject.group(1)) #returns the first group of the phone number
print(matchObject.group(2)) #returns the second group, the rest of the number

# in regex parens are used to delimit a group so, if we have parenthesis 
# that are part of our string we have to use the escape char

phoneNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is (415) 555-4242')
print(matchObject.group())

# we can use of the pipe char "|" we can specify the prefix once and 
# group all the possible suffixes with the pipe char

batRegEx = re.compile(r"Bat(man|mobile|copter|bat)")
matchObject = batRegEx.search("Batmobile lost a wheel")
print(matchObject.group())
print(matchObject.group(1)) # since we grouped the suffixes,
                            # we can show what it found
                            
