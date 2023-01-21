# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

from random import randint

array_Length = len(names)

randomPerson = randint(0, array_Length-1)

print(f"{names[randomPerson]} is going to pay the bill today!")