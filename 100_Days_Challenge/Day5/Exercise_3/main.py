#sum all even numbers
#both the solutions are valid

sumEven = 0
for num in range(1, 101):
    if num % 2 == 0:
        sumEven += num
print(f"The sum of all even numbers is: {sumEven}")


sumEven2 = 0
for num2 in range (2, 101, 2):
    sumEven2 += num2
print(f"The sum of all even numbers is: {sumEven2}")