rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

from random import randint
choices = [rock, paper, scissors]

def cpuSymbolChoice():
    return randint(0, len(choices)-1)

playerChoice = int(input("Rock, Paper or Scissors? For rock type 1, for paper type 2, for scissors type 3: ")) - 1 

if playerChoice >=3 or playerChoice < 0:
    print("You entered an invalid input")
else:
    print(f"You chose:\n {choices[playerChoice]}")
    cpuChoice = cpuSymbolChoice()
    print(f"The CPU chose:\n {choices[cpuChoice]}")
    
    if playerChoice == 0 and cpuChoice == 1:
        print("You Lose")
    elif playerChoice == 1 and cpuChoice == 2:
        print("You Lose")
    elif playerChoice == 2 and cpuChoice == 0:
        print("You Lose")
    elif playerChoice == cpuChoice:
        print("It's a Tie!")
    else:
        print("You Win!")