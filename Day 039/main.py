#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import sys
from pathlib import Path
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Now you can import config
from config import Configuration

try:
    config = Configuration()
    # Use your config here
    SHEETY_FLIGHT_SHEET_ID =  config['SHEETY_FLIGHT_SHEET_ID']
    SHEETY_FLIGHT_API_TOKEN = config['SHEETY_FLIGHT_API_TOKEN']
    AMADEUS_CLIENT_ID = config['AMADEUS_CLIENT_ID']
    AMADEUS_CLIENT_SECRET = config['AMADEUS_CLIENT_SECRET']
except Exception as e:
    print(f"Error: {e}")
    
ORIGIN_CITY = "SYD"
CURRENCY = "AUD"
TOMORROW = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
SIX_MONTH = (datetime.strptime(TOMORROW, '%Y-%m-%d') + relativedelta(months=6)).strftime('%Y-%m-%d')

fs = FlightSearch(AMADEUS_CLIENT_ID, AMADEUS_CLIENT_SECRET)
#dm = DataManager(SHEETY_FLIGHT_SHEET_ID, SHEETY_FLIGHT_API_TOKEN, fs)
#data = dm.get_data()
data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 1710, 'id': 2}, {'city': 'Frankfurt', 'iataCode': 'FRA', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': 'HKG', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': 'DBN', 'lowestPrice': 378, 'id': 10}]
#print(data)
for i in range(1):
    lowest_price = fs.search_deals(ORIGIN_CITY, data[i]['iataCode'],TOMORROW, data[i]['lowestPrice'], CURRENCY, SIX_MONTH)
    if lowest_price != None:
        print(f"Lowest price from {data[i]['iataCode']} to {ORIGIN_CITY} is {lowest_price} {CURRENCY}")
        #dm.update_lowest_price(data[i]['id'], lowest_price)
        #dm.send_notification(f"Lowest price from {data[i]['city']} to {ORIGIN_CITY} is {lowest_price} {CURRENCY}")

