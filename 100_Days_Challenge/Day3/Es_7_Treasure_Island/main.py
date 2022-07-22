print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

firstChoice = input("You're at a crossroad. Where do you want to go? Type left or right:\n").lower()

if firstChoice == "left":
    secondMessage = "You've come to a lake. There is an island in the middle of the lake. Type wait to wait for a boat. Type swim to swim across\n"
    secondChoice = input(secondMessage).lower()
    
    if secondChoice == "wait":
        thirdMessage ="You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n"
        thirdChoice = input(thirdMessage).lower()
        
        if thirdChoice == "yellow":
            print("You Win!")
        elif thirdChoice == "red":
            print("You entered a room full of fire and get burned by it.\nGAME OVER")
        elif thirdChoice == "blue":
            print("There is a beast in the room and you get eaten by it.\nGAME OVER")
        else:
            print("GAME OVER")
        
    else:
        print("You've been attacked by a trout.\nGAME OVER")
    
else:
    print("You fell into a hole.\n GAME OVER")