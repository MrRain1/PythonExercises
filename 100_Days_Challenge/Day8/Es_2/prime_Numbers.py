def prime_checker(number):
    isPrime = 1
    for index in range(1, number+1):
        if( (index != 1 and index != number) and (number % index == 0)):
            isPrime = 0
    
    if(isPrime):
        print(f"\n{number} is prime")
    else:
        print(f"\n{number} is not prime")

for index in range(1,101):
    prime_checker(index)