from recipies import MENU

COINS_VALUE = {
    "quarters": {
        "value": 0.25
    },

    "dimes": {
        "value": 0.1
    },

    "nickles": {
        "value": 0.05
    },

    "pennies": {
        "value": 0.01
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

exitFlag = False


def main():
    global exitFlag
    while(not exitFlag):
        userChoice = input(
            "What would you like? (espresso/latte/cappuccino): ").lower()

        if(userChoice == "off"):
            print("Shutting off...")
            exitFlag = True

        elif(userChoice == "report"):
            printResources()

        elif userChoice in MENU:
            if checkResources(userChoice):
                if checkCoins(userChoice):
                    updateReport(userChoice)
                    print(f"Here is your {userChoice}. Enjoy!\n")


#prints the resources in the coffee machine
def printResources():
    print(f"\nResources:")
    symbol = ""
    for index in resources:
        symbol = returnSymbol(index)
        print(f"{index}: ".capitalize() + f"{resources[index]}{symbol}")
    print("\n")


#returns the correct measurment unit for each resource in the coffe machine
def returnSymbol(resource):
    if resource == "water" or resource == "milk":
        return "ml"
    if resource == "coffee":
        return "g"
    if resource == "money":
        return "$"


#checks if there are enough ingredients for a recipie
def checkResources(userChoice):
    for resourceIndex in resources:
        if resources[resourceIndex] < MENU[userChoice]["ingredients"][resourceIndex]:
            print(f"There's not enough {resourceIndex}")
            return False
        else:
            return True


#takes coins from the user and checks if they are enough to pay for the beverage
def checkCoins(userChoice):
    coins = {
        "quarters": {
            "number": 0,
        },

        "dimes": {
            "number": 0,
        },

        "nickles": {
            "number": 0
        },

        "pennies": {
            "number": 0
        }
    }

    recipieCost = MENU[userChoice]["cost"]
    totalInserted = 0

    print(f'Price of a {userChoice}: {recipieCost}')

    for coinsIndex in coins:
        coins[coinsIndex]["number"] = int(input(f"How many {coinsIndex}? "))
        totalInserted += coins[coinsIndex]["number"] * \
            COINS_VALUE[coinsIndex]["value"]

    print(f"\nTotal inserted: {round(totalInserted, 2)}$")

    if totalInserted < recipieCost:
        print("Sorry that's not enough money.\nRefounding money")
        return False
    else:
        if totalInserted > recipieCost:
            print(
                f"Here is {round(totalInserted - recipieCost, 2)}$ in change")
        return True


#if the payment is successfull update the report adding the money and subtracting the ingredients quantity from the resources
def updateReport(recipieChoiced):
    for resourceIndex in resources:
        
        if resourceIndex in MENU[recipieChoiced]["ingredients"]:
            
            if (resourceIndex == "money"):
                resources[resourceIndex] += MENU[recipieChoiced]["cost"]
            else:
                resources[resourceIndex] -= MENU[recipieChoiced]["ingredients"][resourceIndex]


main()
