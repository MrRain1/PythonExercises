# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sumHeigths = 0
medHeigth = 0

for count in student_heights:
    sumHeigths += count

medHeigth = round(sumHeigths / len(student_heights) , 2)
print(f"The average student heigth is: {medHeigth} cm")