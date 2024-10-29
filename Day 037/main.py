import requests
import datetime as dt
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Now you can import config
from config import Configuration

try:
    config = Configuration()
    # Use your config here
    USERNAME = config['PIXELA_USERNAME']
    TOKEN = config['TOKEN']
    GRAPH_ID = config['GRAPH_ID']
except Exception as e:
    print(f"Error: {e}")

USER_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

def create_user():
    response = requests.post(url=USER_ENDPOINT, json=USER_PARAMS)
    print(f"{response.text}")
    
def create_graph():
    graph_endpoint = f"{USER_ENDPOINT}/{USERNAME}/graphs"
    graph_params = {
        "id": GRAPH_ID,
        "name": "Coding Practice",
        "unit": "hours",
        "type": "float",
        "color": "momiji",
        "timezone": "Australia/Sydney"
    }
    graph_headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_headers)
    print(f"{response.text}")
    
def post_pixel():
    today = dt.date.today()
    formatted_date = today.strftime("%Y%m%d")
    post_pixel_endpoint = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    post_pixel_params = {
        "date": formatted_date,
        "quantity": "4"
    }
    
    post_pixel_headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=post_pixel_headers)
    print(response.text)

def update_pixel():
    today = dt.date.today()
    formatted_date = today.strftime("%Y%m%d")
    update_pixel_endpoint = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
    update_pixel_params = {
        "quantity": "16"
    }
    update_pixel_headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=update_pixel_headers)
    print(response.text)
    
def delete_pixel():
    today = dt.date.today()
    formatted_date = today.strftime("%Y%m%d")
    delete_pixel_endpoint = f"{USER_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
    delete_pixel_headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.delete(url=delete_pixel_endpoint, headers=delete_pixel_headers)
    print(response.text)
#create_user()
#create_graph()
post_pixel()
#update_pixel()
#delete_pixel()
