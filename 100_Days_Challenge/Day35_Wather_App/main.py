import requests
import config
OPEN_METEO_ENDPOINT = "https://api.open-meteo.com/v1/forecast"

# between code 51 an code 99 are all the rain and snow occurrences on Open Meteo
DRIZZLE_CODE = 51
THUNDERSTORM_CODE = 99


if __name__=="__main__":
    response = requests.get(url=OPEN_METEO_ENDPOINT, params=config.API_PARAMS)
    response.raise_for_status()
    obtained_data = response.json()
    # print(obtained_data)
    going_to_rain = False
    
    
    # cycle codes from 6:00 to 20:00
    for code in obtained_data["hourly"]["weathercode"][6:21]:
        going_to_rain = True if (DRIZZLE_CODE<=code<=THUNDERSTORM_CODE) else False
        
    print("Bring an umbrella!") if going_to_rain else print("No need for un umbrella today")
