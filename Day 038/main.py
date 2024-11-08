import requests
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Now you can import config
from config import Configuration

try:
    config = Configuration()
    # Use your config here
    NutritionIX_API_Key = config['NutritionIX_API_Key']
    NutritionIX_APP_ID =  config['NutritionIX_APP_ID']
    SHEETY_API_URL =  config['SHEETY_API_URL']
    SHEETY_API_TOKEN = config['SHEETY_API_TOKEN']
except Exception as e:
    print(f"Error: {e}")
    
EXERCISE_NATURAL_LANGUAGE_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_exercise_data(query):
    api_headers = {
        "x-app-id": NutritionIX_APP_ID,
        "x-app-key": NutritionIX_API_Key,
    }
    
    params = {
        "query": query
    }
    
    response = requests.post(url=EXERCISE_NATURAL_LANGUAGE_API_ENDPOINT, json=params, headers=api_headers)
    response.raise_for_status()
    
    workouts = []
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    for e in response.json()["exercises"]:
        workouts.append({
            "date": current_date,
            "time": current_time,
            "exercise": e["name"],
            "duration": e["duration_min"],
            "calories": e["nf_calories"],
            
        })
    return workouts

def post_workout_googleSheet(workouts):
    
    for workout in workouts:
        params = {
            "workout": {
                "date": workout["date"],
                "time": workout["time"],
                "exercise": workout["exercise"],
                "duration": workout["duration"],
                "calories": workout["calories"],
            }
        }
        api_headers = {"Authorization": SHEETY_API_TOKEN}
        response = requests.post(url=SHEETY_API_URL, json=params, headers=api_headers)
        response.raise_for_status()
        print(response.text)

exercise_description = input("Please, describe your exercise in your language: ")
workouts = None
workouts = get_exercise_data(exercise_description)
print(workouts)
if workouts != None:
    post_workout_googleSheet(workouts)