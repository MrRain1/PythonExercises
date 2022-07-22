#Love calculator

# 🚨 Don't change the code below 👇
from matplotlib.pyplot import sci


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#counting the occurrence of each letter in each name
#maybe there is a better way to do it?
t_occurrence = name1.lower().count("t") + name2.lower().count("t")
r_occurrence = name1.lower().count("r") + name2.lower().count("r")
u_occurrence = name1.lower().count("u") + name2.lower().count("u")
e_occurrence = name1.lower().count("e") + name2.lower().count("e")
l_occurrence = name1.lower().count("l") + name2.lower().count("l")
o_occurrence = name1.lower().count("o") + name2.lower().count("o")
v_occurrence = name1.lower().count("v") + name2.lower().count("v")

score1 = t_occurrence + r_occurrence + u_occurrence + e_occurrence
score2 = l_occurrence + o_occurrence + v_occurrence + e_occurrence

#join the two numbers togheter
totalScore = int(str(score1) + str(score2))

if totalScore < 10 or totalScore > 90:
    print(f"Your score is {totalScore}, you go together like coke and mentos.")
elif totalScore >= 40 and totalScore <= 50:
    print(f"Youre score is {totalScore}, you are alright togheter.")
else:
    print(f"Your score is {totalScore}")