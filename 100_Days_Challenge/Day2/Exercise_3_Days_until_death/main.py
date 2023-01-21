# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

MONTHS_IN_YEAR = 12
WEEKS_IN_YEAR = 52
DAYS_IN_YEAR = 365

ageAsInt = int(age)
yearsLeft = 90 - ageAsInt

monthsLeft = yearsLeft * MONTHS_IN_YEAR
weeksLeft = yearsLeft * WEEKS_IN_YEAR
daysLeft = yearsLeft * DAYS_IN_YEAR

#Use fString to include different types in a string
print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthsLeft} months left")



