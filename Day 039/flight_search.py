import requests
from datetime import datetime, timedelta

class FlightSearch:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = None
        self.base_url = "https://test.api.amadeus.com"

    def get_access_token(self):
        """Get new access token from Amadeus API"""
        url = f"{self.base_url}/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            token_info = response.json()
            self.access_token = token_info['access_token']
            # Set expiration time (subtract 5 minutes as safety margin)
            expires_in = token_info.get('expires_in', 1800)  # default 30 minutes
            self.token_expires_at = datetime.now() + timedelta(seconds=expires_in - 300)
            return self.access_token
        else:
            raise Exception(f"Failed to get access token: {response.text}")

    def ensure_valid_token(self):
        """Check if token is expired or missing and refresh if needed"""
        if (not self.access_token or 
            not self.token_expires_at or 
            datetime.now() >= self.token_expires_at):
            return self.get_access_token()
        return self.access_token

    def get_city_iataCode(self, city):
        """
        Returns the IATA code for a given city.
        If the city is not found, returns None.
        """
        try:
            # Ensure we have a valid token before making the request
            self.ensure_valid_token()
            
            url = f"{self.base_url}/v1/reference-data/locations/cities"
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
            params = {
                "keyword": city,
                "max": "1"
            }
            
            response = requests.get(url, headers=headers, params=params)
            
            # Check for token expiration error
            if response.status_code == 401:
                error_code = response.json().get('errors', [{}])[0].get('code')
                if error_code == 38192:  # Token expired error
                    # Get new token and retry the request once
                    self.get_access_token()
                    headers["Authorization"] = f"Bearer {self.access_token}"
                    response = requests.get(url, headers=headers, params=params)
            
            # Process the response
            if response.status_code == 200:
                data = response.json()
                if data.get('data'):
                    return data['data'][0].get('iataCode')
            return None

        except Exception as e:
            print(f"Error getting IATA code: {str(e)}")
            return None
        
    def search_deals(self, origin, destination, departure_date, max_price, currency, return_date=None, ):
        try:
            # Ensure we have a valid token before making the request
            self.ensure_valid_token()
            
            url = f"{self.base_url}/v2/shopping/flight-offers"
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
            params = {
                "originLocationCode": origin,
                "destinationLocationCode": destination,
                "departureDate": departure_date,
                "returnDate": return_date,
                "adults": "1",
                "maxPrice": max_price,
                "currencyCode": currency,
                "max": "1"
            }
            
            response = requests.get(url, headers=headers, params=params)
            
            # Check for token expiration error
            if response.status_code == 400 or response.status_code == 500:
                print(response.json().get('errors'))
            
            # Process the response
            if response.status_code == 200:
                if response != None:
                    return response.json()['data'][0]['price']['total']
            return None

        except Exception as e:
            print(f"Error getting IATA code: {str(e)}")
            return None