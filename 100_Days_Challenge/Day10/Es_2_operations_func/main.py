#calculator program

from art import logo
print(logo)
#add
def add(arg1, arg2):
    return arg1 + arg2

#sub
def sub(arg1, arg2):
    return add(arg1, -arg2)

#multiplication
def mult(arg1, arg2):
    return arg1 * arg2

#division
def div(arg1, arg2):
    if (arg2 != 0):
        return arg1 / arg2
    return "Math Error"

operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div,
}
exitStatus = False

num1 = input("Insert first number: ")

while (not exitStatus):
    
    #list and choose an operator
    for operators in operations:
        print(f"\n{operators}")
    chosenOperator = input("\nChoose the operator: ")
    
    num2 = input("Insert second number: ")

    #check if any of the arguments are nulls
    if num1 == "" or num2 == "" or chosenOperator == "":
        print("Syntax Error")
        break

    function = operations[chosenOperator]
    result = function(float(num1), float(num2))
    print(f"{num1} {chosenOperator} {num2} = {result}")
    
    answer = input("Continue with the operations? yes/no: ").lower()
    if(answer != "yes"):
        exitStatus = True
        print("\nGoodbye!")
    else:
        num1 = result
        
    





# print(f"The result is: {function(num1, num2)}")
#print(f"{num1} {chosenOperator} {num2} = {function(num1, num2)}")