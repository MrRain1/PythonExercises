#Write your code below this line 👇
from pickle import FALSE, TRUE


def prime_checker(number):
    isPrime = 1
    for index in range(1, number+1):
        if( (index != 1 and index != number) and (number % index == 0)):
            isPrime = 0
    
    if(isPrime):
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



