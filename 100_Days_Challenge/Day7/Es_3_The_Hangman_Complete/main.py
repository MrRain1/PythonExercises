import random

word_list = ["aardvark", "baboon", "camel"]
display = []
numOfLives = 6


def initializeDisplay(word):
    for count in range(0, len(word)):
        display.append("_")


def printDisplay():
    print("\n"+"".join(display))

#choose random word from the list
randNum = random.randint(0, len(word_list)-1)
randWord = word_list[randNum]

initializeDisplay(randWord)
printDisplay()
print(f"Number of lives: {numOfLives}")

while numOfLives and ("_" in display):
    #Guess a letter and assign it to the var and make it lowercase
    guessChar = input("Guess a letter: ").lower()
    
    if guessChar in display:
        print("\nYou already guessed this letter")
    
    if guessChar in randWord:
        for index in range(0, len(randWord)):
            if guessChar == randWord[index]:
                display[index] = guessChar
    else:
        print(f"\nThere aren't {guessChar}'s in the word to guess")
        numOfLives -=1
    printDisplay()
    print(f"Number of lives: {numOfLives}")

if numOfLives and ("_" not in display):
    print("\nYou guessed all the letters! Congratulations!")
else:
    print("\nYou lose...")

