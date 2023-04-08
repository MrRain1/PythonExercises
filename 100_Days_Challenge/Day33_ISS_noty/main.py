import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()

obtained_data = response.json()

longitude = obtained_data["iss_position"]["longitude"]
latitude = obtained_data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)