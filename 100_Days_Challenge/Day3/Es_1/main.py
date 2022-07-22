from typing import final


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

CHILD_TICKET = 5
TEEN_TICKET = 7
ADULT_TICKET = 12

final_Price = 0
is_MiddleAge = 0

if height >= 120:
    print("You can purchase a ticket")
    age = int(input("What's your age? "))
    
    if age <= 12:
        print(f"The ticket for a child costs: {CHILD_TICKET}$")
        final_Price = CHILD_TICKET
    elif age > 12 and age <= 18:
        print(f"The ticket for a teen costs: {TEEN_TICKET}$")
        final_Price = TEEN_TICKET
    else:
              
        if age >= 45 and age <= 55:
            print("The ticket is free!")
            final_Price = 0
            is_MiddleAge = 1
        else:
            print(f"The ticket for an adult costs: {ADULT_TICKET}$")
            final_Price = ADULT_TICKET             
    
    if is_MiddleAge == 0 and (input("Do you want a photo, it will cost and additional 3$ (Yes/No)? ")).lower() == "yes":
        final_Price +=3
    
    print(f"The final price of the ticket is: {final_Price}$")
    
else:
    print("Sorry you can't ride the rollercoaster")
    

