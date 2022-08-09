from random import randint

playerName = input("Hello! What's your name? ")

print(f"Well, {playerName}, I am thinking of a number between 1 and 20.")

guessNumber = randint(1, 20)

for roundCount in range(6): 
    playerGuess = input("Take a guess: ")
    try:
        if int(playerGuess) != guessNumber and roundCount == 5:
            print(f"Nope. The number I was thinking of was {guessNumber}")      
        elif int(playerGuess) > guessNumber:
            print("Your guess is too high")
        elif int(playerGuess) < guessNumber:
            print("Your guess is too low")
        else:
            print(f"Good job, {playerName}! You guessed my number in {roundCount} turns")
    except ValueError:
        print("Please input a number")
        