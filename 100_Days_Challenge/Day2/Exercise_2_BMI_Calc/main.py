# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#BMI = mass / height^2
#convert the strings to floats
BMI_float = (float(weight)) / (float(height))**2

#round the BMI to 2 decimal places
print(round(BMI_float, 2)) 
