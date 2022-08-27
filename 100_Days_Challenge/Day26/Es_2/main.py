import numbers


numbers = [1,1,2,3,5,8,12,21,24,55]

squared_numbers = [num**(2) for num in numbers if num > 0]

print(squared_numbers)