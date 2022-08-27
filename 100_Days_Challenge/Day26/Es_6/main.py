# new_dict = {new_key: new_val for item in list}
# new_dict = {new_key: new_val for (key,value) in dict.items()}


import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

student_score = {name: random.randint(20,100) for name in names}

print(student_score)

passed_students = {name:score for (name,score) in student_score.items() if score>=60}

print(passed_students)

