# opening , reading, and writing to files

import os

# the open() functions opens the file in the specified path
# it defaults to read only mode
print(os.getcwd())
helloFile = open("./Hello.txt")

# the .read() method reads the raw content of the text file
contents = helloFile.read()

# after reading we have to close the file
helloFile.close()

print(contents)

# the .readlines() method returns a list of the strings
# contained in the file

helloFile = open("./Hello.txt")
contents = helloFile.readlines()
helloFile.close()
print(contents)

# we can open a file in write mode passing as an arguemnt "w"
# everything in the file will be deleted and start blank

# or we can open a file in append mode by passing "a"
# exerything we write in the file will be appended at the end of the file

helloFile = open("./hello2.txt", "a") 
helloFile.write("Appended line\n")
helloFile.close()

# THe shelve module can store Python values ina binary file
# import shelve
# shelve.open() returns a dictionary like object

# shelveFile = shelve.open("MyData")
# shelveFile["Cats"] = ["Sophie", "Tails"]
# shelveFile.close()

# we can open it and read the data contents:
# shelveFile["cats"] => returns a list
# we can use methods like .keys() and .values()