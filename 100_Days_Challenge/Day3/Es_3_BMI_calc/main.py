# 🚨 Don't change the code below 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

UNDERWEIGHT = 18.5
NORMAL_WEIGHT = 25
SLIGHT_OVERWEIGHT = 30
OBESE = 35



#BMI = mass (kg) / height^2 (m^2)
#convert the strings to floats
BMI_float = (weight) / (height)**2
rounded_BMI = round(BMI_float , 2)


#round the BMI to 2 decimal places
if BMI_float <= UNDERWEIGHT:
    print(f"Your BMI is: {rounded_BMI}, you are underweight")

elif BMI_float > UNDERWEIGHT and BMI_float <= NORMAL_WEIGHT:
    print(f"Your BMI is: {rounded_BMI}, you have a normal wight")

elif BMI_float > NORMAL_WEIGHT and BMI_float <= SLIGHT_OVERWEIGHT:
    print(f"Your BMI is: {rounded_BMI}, you are slightly overweight")

elif BMI_float > SLIGHT_OVERWEIGHT and BMI_float <= OBESE:
    print(f"Your BMI is: {rounded_BMI}, you are obese")

else:
    print(f"Your BMI is: {rounded_BMI}, you are clinically obese")