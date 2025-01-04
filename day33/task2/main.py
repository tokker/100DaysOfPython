import requests
from datetime import datetime

MY_LAT = 47.503368
MY_LONG = 19.084207

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

sunrise_response = requests.get(url="https://api.sunrise-sunset.org/json", params = parameters)
sunrise_response.raise_for_status()
sunrise_data = sunrise_response.json()
sunrise_time = datetime.strptime(sunrise_data["results"]["sunrise"], "%I:%M:%S %p").time()
sunset_time = datetime.strptime(sunrise_data["results"]["sunset"], "%I:%M:%S %p").time()
if not sunrise_time < datetime.now().time() < sunset_time:
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if iss_latitude-5 <= MY_LAT <= iss_latitude+5 and iss_longitude-5 <= MY_LONG <= iss_longitude+5:
        print("The ISS is currently over your location.")
    else:
        print("The ISS is not currently over your location.")
    print(f"The ISS is at coordinates ({iss_latitude}, {iss_longitude}).")