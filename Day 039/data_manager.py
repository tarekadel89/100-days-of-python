import requests
from flight_search import FlightSearch

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, sheet_id, sheety_api_token, flight_search):
        self.sheet_id = sheet_id
        self.api_token = sheety_api_token
        self.flight_search = flight_search
        
    def get_data(self):
        api_header = {"Authorization": self.api_token}
        response = requests.get(url = self.sheet_id, headers = api_header)
        response.raise_for_status()
        rows = response.json()['prices']
        for row in rows:
            if row['iataCode'] == '':
                city_iataCode = self.flight_search.get_city_iataCode(row['city'])
                row['iataCode'] = city_iataCode
                self.update_row_iataCode(row['id'], city_iataCode)
        return rows
    
    def update_row_iataCode(self, row_id, iataCode):
        put_api_url = f"{self.sheet_id}/{row_id}"
        api_header = {"Authorization": self.api_token}
        api_body = {
            "price": {
                "iataCode": iataCode,
            }
        }
        response = requests.put(url=put_api_url, json=api_body, headers=api_header)
        response.raise_for_status()