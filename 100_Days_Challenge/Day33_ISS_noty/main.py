import requests
import datetime
from config import PARAMETERS, ERROR_PERCENTAGE


def is_overhead(iss_latitude, iss_longitude):
    """Function that verifies if the ISS is in range of the coordinates of your position
    by using the coordinates obtained from the API and your coordinates imported from the config file.
    Returns True if the ISS is in range, otherwise False.

    Args:
        iss_latitude (float): ISS latitude
        iss_longitude (float): ISS longitude

    Returns:
        bool: True if ISS in range, otherwise False
    """
    min_lat= PARAMETERS["lat"] * (1-ERROR_PERCENTAGE)
    max_lat= PARAMETERS["lat"] * (1+ERROR_PERCENTAGE)
    
    min_lng= PARAMETERS["lng"] * (1-ERROR_PERCENTAGE)
    max_lng= PARAMETERS["lng"] * (1+ERROR_PERCENTAGE)
    
    iss_in_range= min_lat<=iss_latitude<=max_lat and min_lng<=iss_longitude<=max_lng
    return iss_in_range

if __name__=="__main__":
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_obtained_data = iss_response.json()
    
    longitude = float(iss_obtained_data["iss_position"]["longitude"])
    latitude = float(iss_obtained_data["iss_position"]["latitude"])
    
    sunrise_sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params= PARAMETERS)
    sunrise_sunset_response.raise_for_status()
    sunrise_sunset_data = sunrise_sunset_response.json()
    
    timings = {
        "sunrise": int(sunrise_sunset_data["results"]["sunrise"].split("T")[1].split(":")[0]),
        "sunset": int(sunrise_sunset_data["results"]["sunset"].split("T")[1].split(":")[0]),
    }
    current_hour = datetime.datetime.now().hour
    
    if (is_overhead(iss_latitude=latitude, iss_longitude=longitude)) and not (timings["sunrise"]<current_hour<timings["sunset"]):
        print("You can observe the ISS cruising the night sky!")
    else:
        print("Sorry the ISS is not yet observable.")

