# useful methods to work with strings

# 1. .upper() => every char in the string to upper case
print("Hello World".upper())

# 2 .lower() => every char in the string to lower case

# 3 .islower() => if every char in the string is lower case returns True
#                 otherwise returns False

# 4 .isupper() => if every char in the string is upper case returns True
#                 otherwise returns False

# 5 .isalpha() => returns true if the string is made only by letters

# 6 .isalnum() => returns ture if the string is made only by numbers and letters

# 7 .isdecimal() => returns true if the string is made only by numbers

# 8 .isspace() => returns true if the string is made only by whitespaces

# 9 .istitle() => returns true if the string is a title case string

# 10 .join() is useful to join togheter a list of strings. Example:
print(','.join(["cats", "bats", "rats"]))

# 11 .split() separates a sting in a list. Example
print("Hello Bruno, how are you?".split()) #splits on whitespaces

# we can pass a char to the split method to split the string on the
# occurrence of the passed character
print("Hello Bruno, how are you?".split("o"))

# 12 the .ljust() and .rjust() are useful to justify a string on the left
# or on the right, and we can pass a number to indicate the number of spaces to insert
# and we can pass an ulterior char as an argument to change the whitespaces with the char passed

print("Hello".rjust(10))
print("Hello".rjust(10, "*"))

# the .center() method works the same way but centers the text instead
print("Hello".center(11, "_"))

# 13 the .strip() [.rstrip() / .lstrip()] method is useful to
# strip whitespaces from a string
print("Hello".rjust(10))
print("Hello".rjust(10).strip())

# we can also pass a string as an argument

print("SpamSpamBaconSpamEggsSpamSpam")
print("SpamSpamBaconSpamEggsSpamSpam".strip("Spam"))

# 14 the .replace() methon is useful to replace chars in a string with others

print("Hello There!")
print("Hello There". replace("e", "XYZ"))