year = int(input("Insert the year you want to check: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0 ):
    print(f"{year} is a leap year")
else:
    print(f"{year} isn't a leap year")