#Step 1 
import random


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

#choose random word from the list
randNum = random.randint(0, len(word_list)-1)
randWord = word_list[randNum]

#Guess a letter and assign it to the var and make it lowercase
guessChar = input("Guess a letter: ").lower()

for letter in randWord:
    if guessChar == letter:
        print("Right")
    else:
        print("Wrong")
