#calculator program recursive

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

def calculator():
    global exitStatus
    if exitStatus:
        print("\nGoodbye!")
        return
    else:
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
                exitStatus = True
                break
            
            function = operations[chosenOperator]
            result = function(float(num1), float(num2))
            print(f"{num1} {chosenOperator} {num2} = {result}")
            
            answer = input("Continue with the operations? yes/no/anything to restart: ").lower()
            if(answer == "no"):
                exitStatus = True
                calculator()
            elif(answer =="yes"):
                num1 = result
            else:
                calculator()
                
calculator()