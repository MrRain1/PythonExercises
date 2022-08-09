from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

exitFlag = False

while (not exitFlag):
    userChoice = input(f"\nWhat would you like? ({menu.get_items()}): ")
    
    if(userChoice == "off"):
        exitFlag = True
    elif(userChoice == "report"):
        coffeeMaker.report()
        moneyMachine.report()
    elif (menu.find_drink(userChoice)):
        menuItem = menu.find_drink(userChoice)
        if coffeeMaker.is_resource_sufficient(menuItem):
            print(f"A {menuItem.name} costs: {menuItem.cost}$")
            if moneyMachine.make_payment(menuItem.cost):
                coffeeMaker.make_coffee(menuItem)