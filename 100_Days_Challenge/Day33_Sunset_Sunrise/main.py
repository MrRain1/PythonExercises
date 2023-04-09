import requests
import datetime

MY_LATITUDE = 40.749180
MY_LONGITUDE = 14.500740
FORMATTED = 0

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": FORMATTED,
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
obtained_data = response.json()

timings = {
    "sunrise": int(obtained_data["results"]["sunrise"].split("T")[1].split(":")[0]),
    "sunset": int(obtained_data["results"]["sunset"].split("T")[1].split(":")[0]),
}

for key, value in timings.items():
    print(f"{key}: {value}")
current_hour = datetime.datetime.now().hour
print(f"Current time: {current_hour}")

if timings["sunrise"] < current_hour < timings["sunset"]:
    print("It's daytime")
else:
    print("It's nighttime")
