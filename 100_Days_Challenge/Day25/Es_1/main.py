# import csv
import pandas

temps = []

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
    
#     for index in data:
#         if index[1] != "temp":
#             temps.append(int(index[1]))
        
# print(temps)

data = pandas.read_csv("./weather_data.csv")

temp_list = data["temp"].to_list()

# brute way to calculate the mean

# total = 0
# for index in range(len(temp_list)):
#     total +=temp_list[index]

# avg_temp = total/ len(temp_list)
# print(f"{round(avg_temp, 2)}°C")

# # using the inbuilt sum() function
# avg_temp = sum(temp_list)/ len(temp_list)
# print(f"{round(avg_temp, 2)}°C")

# using the mean method in pandas

avg_temp = data["temp"].mean()
print(f"{round(avg_temp, 2)}°C")

maximum_temp = data["temp"].max()
print(f"{round(maximum_temp, 2)}°C")

minimum_temp = data["temp"].min()
print(f"{round(minimum_temp, 2)}°C")

print(data[data.day == "Monday"])
print(data[data.temp == maximum_temp])

data_dic = {
    "students":["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

student_scores = pandas.DataFrame(data_dic)
print(student_scores)