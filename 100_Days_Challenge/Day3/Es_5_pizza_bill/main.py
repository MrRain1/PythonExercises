# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totalBill = 0

if size != "":
    if size.lower() == "s":
        totalBill += 15
    elif size.lower() == "m":
        totalBill += 20
    else:
        totalBill += 25

    if add_pepperoni.lower() == "y":
        totalBill +=2

    if extra_cheese.lower() == "y":
        totalBill +=1
    
    print(f"Yout final bill is: ${totalBill}")










