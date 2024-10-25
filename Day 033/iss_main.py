import requests
import datetime as dt


MY_LAT = 51.868820
MY_LONG = -42.209290

ISS_LOCATION_API = "http://api.open-notify.org/iss-now.json"
SUNSET_API = "https://api.sunrise-sunset.org/json"


def getISSLocation():
    response = requests.get(ISS_LOCATION_API)
    response.raise_for_status()
    iss_data = response.json()
    return (float(iss_data["iss_position"]["latitude"]), float(iss_data["iss_position"]["longitude"]))
    
def isSunDown():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Australia/Sydney"
    }
    response = requests.get(SUNSET_API, params=parameters)
    response.raise_for_status()
    sunset_data = response.json()
    
    sunset_hour = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise_hour = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    curr_hour = dt.datetime.now().hour
    
    if curr_hour > sunset_hour or curr_hour < sunrise_hour:
        return True
    return False

def isISSOnSight(iss_location):
    print(iss_location)
    if MY_LAT-5 <= iss_location[0] <= MY_LAT+5 and MY_LONG-5 <= iss_location[1] <= MY_LONG+5:
        return True
    return False
    

if isSunDown():
    iss_location = getISSLocation()
    if isISSOnSight(iss_location):
        print("The ISS is currently on sight.")
    else:
        print("The ISS is not currently on sight.") 