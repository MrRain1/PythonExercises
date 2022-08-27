weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:
def toFar(temp):
    return round(((temp * 9/5) + 32), 2)

weather_f = {day:toFar(temp) for (day, temp) in weather_c.items()}

print(weather_f)
