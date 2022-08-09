# We already know that we can type strings using single or double quotes
# A problem arises when we have multiple quotes in a single sting
# that can lead to incorrect syntax. 

 # Example:
 print('This is Alices' cat') 
       
# To solve this problem we can use the escape character "\"
# We follow the \ with the character we want to escape, eg: '

print('This is Alices\'s  cat')

# we can see how know python recognises the single quote as a simple char
# and not as a end of string indicator

# Another way is using a raw string, preceeding the quotes with an "r"
print(r"This is Alcie\'s cat")
# a raw string treats every char in the sting as a raw char, so the escape char does not work

# for multiline strings we can use triple double or single quotes: """ or '''
# (usefult for creating docstrings in a function)

 