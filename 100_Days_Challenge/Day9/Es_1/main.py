student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {
    
}

#TODO-2: Write your code below to add the grades to student_grades.👇

for keys in student_scores:
    student_grades.setdefault(keys, "")
    if student_scores[keys] >= 91 and student_scores[keys] <= 100:
        student_grades[keys] = "Outstanding"
    
    elif student_scores[keys] >= 81 and student_scores[keys] <= 90:
        student_grades[keys] = "Exceeds Expectations"
    
    elif student_scores[keys] >= 71 and student_scores[keys] <= 80:
        student_grades[keys] = "Acceptable"
    
    else:
        student_grades[keys] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)

