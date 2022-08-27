student_dic = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_frame = pandas.DataFrame(student_dic)

# for (key, val) in student_frame.items():
#     print(val)
  
# loop through rows of a data frame

for (index, row) in student_frame.iterrows():
    if row.student == "Angela":
        print(row.score)