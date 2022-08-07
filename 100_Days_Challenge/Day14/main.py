# Higher or Lower game

import game_data
import art
import random
import os

DATA_LEN = len(game_data.data)

exitFlag = False
playerScore = 0


def game():
    global exitFlag
    global playerScore

    firstPerson = {}

    while(not exitFlag):
        # clear the screen, reprint the logo and show the player score each turn
        printLogo()
        print(f"Score: {playerScore}")

        # Initialize the new turn choices and show them on screen
        if playerScore == 0:
            firstPerson = game_data.data[random.randint(0, DATA_LEN - 1)]

        secondPerson = chooseSecond(firstPerson)

        print("\n" + personInfo(firstPerson))
        print(f"{art.vs}")
        print(personInfo(secondPerson)+"\n")

        # get the choice from the player and call the function to check if the choice is right.
        # if the input is anything else than the given inputs, forcefully exit the game.
        playerResponse = input(
            f"Make your choice!\nInput 1 for {firstPerson['name']}, 2 for {secondPerson['name']}: ").lower()

        if playerResponse == "1":
            firstPerson = isHigher(firstPerson, secondPerson)

        elif playerResponse == "2":
            firstPerson = isHigher(secondPerson, firstPerson)
        else:
            exitFlag = True
            print("You terminated the game.")
            playAgain()


def personInfo(person):
    """Get's a dictionary as input and returs a formatted string
    with the object values

    Args:
        person (obj): The obj to describe

    Returns:
        string: Formatted string showing info on the person
    """
    return f"{person['name']}, a {person['description']} from {person['country']}"


# function to chech if the chosen answer is the right one
def isHigher(firstPerson, secondPerson):
    global playerScore
    global exitFlag

    if firstPerson['follower_count'] > secondPerson['follower_count']:
        print("That's Right!")
        playerScore += 1
        return firstPerson
    else:
        printLogo()
        print("That's wrong. You lose...")
        print(f"\nYour final score was: {playerScore} points")
        exitFlag = True
        playAgain()


def chooseSecond(firstPerson):
    # initialize a first second choice
    secondChoice = game_data.data[random.randint(0, DATA_LEN - 1)]

    # if the second choice is the same first choice then pick another one until they differ
    while secondChoice == firstPerson:
        secondChoice = game_data.data[random.randint(0, DATA_LEN - 1)]

    return secondChoice

# ask the player to restart the game


def playAgain():
    """Ask the player if it wants to restart the game"""

    global exitFlag
    global playerScore
    playerResponse = input("Do you want to play again? [y/n]: ").lower()

    if(playerResponse == "y" or playerResponse == ""):
        exitFlag = False
        playerScore = 0
    else:
        print("Goodbye!")

# function to clear the screen and print the logo


def printLogo():
    """Clears the screen and prints the game logo"""
    os.system("clear")
    print(art.logo)

# initialize the screen, print the logo, welcome message and brief info on the game


def main():
    printLogo()
    print("Welcome to the Higher or Lower Game!")
    print("You have to guess which between the two choices has the most followers and keep increasing your score!")
    startResponse = input("Do you want to play? [y/n]: ").lower()

    if (startResponse == "y" or startResponse == ""):
        game()
    else:
        print("Goodbye!")


main()
