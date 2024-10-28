import requests
import datetime as dt
from twilio.rest import Client
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Now you can import config
from config import Configuration

try:
    config = Configuration()
    # Use your config here
    account_sid = config['account_sid']
    auth_token = config['auth_token']
    twilio_from = config['twilio_from']
    my_phone = config['my_phone']
    APPID= config['APPID']
except Exception as e:
    print(f"Error: {e}")


MY_LAT = -33.868820
MY_LONG = 151.209290
CNT = 6
UOM = "metric"


API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_PARAMS = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": CNT,    
    "units": UOM,
    "appid": APPID,

}


def get_weather_data():
    weather_data = []
    response = requests.get(API_URL, params=API_PARAMS)
    response.raise_for_status()
    all_data = response.json()
    for key, value in all_data.items():
        if key == "list":
            for item in value:
                weather_data.append({
                    "dt_txt": item["dt_txt"],
                    "weather": item["weather"][0]["main"].lower()  # 0 if no rain in the forecasted hour
                })
    return weather_data


def check_rain(weather_data):
    for time_stamp in weather_data:
        time_stamp_hr = int(time_stamp["dt_txt"].split(" ")[1].split(":")[0])
        curr_hr = dt.datetime.now().hour
        if time_stamp_hr > curr_hr and time_stamp["weather"] == "clear":
            return time_stamp['dt_txt'] 
    
def send_sms(rain_time):
    msg_text = f"It is expected to rain at {rain_time.split(" ")[1]}"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= twilio_from,
        body = msg_text,
        to= my_phone
    )

rain_time = check_rain(get_weather_data())
if rain_time != None:
    send_sms(rain_time)