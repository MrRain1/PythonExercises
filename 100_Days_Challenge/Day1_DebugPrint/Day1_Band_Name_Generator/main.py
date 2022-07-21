petName=""
cityName=""
#1. Create a greeting for your program.
print("Hello! Wellcome to the band name generator!")
#2. Ask the user for the city that they grew up in.
while cityName =="":
    print("Could you tell me in what city did your grow up in?")
    cityName = input()
#3. Ask the user for the name of a pet.
while petName =="":
    print("Could you tell me the name of your pet?")
    petName = input()

#4. Combine the name of their city and pet and show them their band name.
print("The name of your band is: The "+ cityName + " " + petName)