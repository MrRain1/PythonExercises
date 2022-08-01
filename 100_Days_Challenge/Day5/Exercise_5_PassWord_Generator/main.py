#Password Generator Project
from mimetypes import init
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easyPass = []

for countLetters in range(1, nr_letters+1):
    easyPass.append(letters[random.randint(0, len(letters)-1)])

for countSymbols in range(1, nr_symbols+1):
    easyPass.append(symbols[random.randint(0, len(symbols)-1)])

for countNumbers in range(1, nr_numbers+1):
    easyPass.append(numbers[random.randint(0, len(numbers)-1)])
    
print("Easy Password: "+ "".join(easyPass))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


#Generate an "ordered password"
initPass = []
for countLetters in range(1, nr_letters+1):
    initPass.append(letters[random.randint(0, len(letters)-1)])

for countSymbols in range(1, nr_symbols+1):
    initPass.append(symbols[random.randint(0, len(symbols)-1)])

for countNumbers in range(1, nr_numbers+1):
    initPass.append(numbers[random.randint(0, len(numbers)-1)])
    
hardPass = []
#print(f"Init pass before: {initPass}")
#print(f"Hard pass before: {hardPass}")

#randomly append an element of the easy pass and remove it from the list 
#in order to not pick it again

for length in range(-1, len(initPass) -1):
    rand = random.randint(0, len(initPass) - 1)
    hardPass.append(initPass[rand])
    initPass.remove(initPass[rand])
    #print(f"Init pass after: {initPass}")
    #print(f"Hard pass after: {hardPass}")

print("Hard Password: "+ "".join(hardPass))