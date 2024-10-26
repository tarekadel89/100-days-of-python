import requests

parameters ={
    "amount": 10,
    "type": "boolean",
}

TRIVIA_API_URL = "https://opentdb.com/api.php"
question_data = []
response = requests.get(TRIVIA_API_URL, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
