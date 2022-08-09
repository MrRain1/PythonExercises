#define new function

#function with no input args
def hello():
    print("Hello World!")
    
hello()


#function with input args
def hello_name(name):
    print(f"Hello {name}")
    
hello_name("Alice")
hello_name("Corrado")

#function that returns a value
def plus_One(number):
    return number + 1

print(f"1+1 is {plus_One(1)}")

#the value "None" is a non-value, that is the default return value of 
#"void" functions 

#the print() function can take peculiar arguments like end="something" to
#specify a new ending value insted of the default \n
#or the argument sep="something" to concatenate multiple strings insted
#of the default white space