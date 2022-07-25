#def div42by(divideBy):
#    return 42 / divideBy

#if we pass 0 to the function we get a divide by zero error
# we can handle the error by using a try except statement


def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("You tried to divide by zero")
        
div42by(0)


numCats = input("How many cats do you have? ")

# if int(numCats) >= 4: 
#     print("That's a lot of cats")
# else:
#     print("That's not that many cats")
    
#in the input statement we can input anything not just integers, so we will
#probably get an error if we type something else

try:
    if int(numCats) >= 4: 
        print("That's a lot of cats")
    else:
        print("That's not that many cats")   
except ValueError:
    print("You did not enter a number")
