import sys
import requests
from twilio.rest import Client
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

# Now you can import config
from config import Configuration

try:
    config = Configuration()
    # Use your config here
    ALPHA_ADVANTAGE_API_KEY = config['ALPHA_ADVANTAGE_API_KEY']
    NEWS_API_KEY = config['NEWS_API_KEY']
    account_sid = config['account_sid']
    auth_token = config['auth_token']
    twilio_from = config['twilio_from']
    my_phone = config['my_phone']
except Exception as e:
    print(f"Error: {e}")
    
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


# Note: You'll need to replace 'TSLA', 'Tesla Inc', and 'your_alpha_vantage_api_key' with your actual stock ticker, company name, and Alpha Vantage API key.

def track_stock_price():
    if datetime.now().weekday() == 0 or datetime.now().weekday() == 6: # no notification during the weekends
        print("It's weekend, no need to check stock price.")
        #return None @TODO: uncomment this line
    alphavantage_api_url = "https://www.alphavantage.co/query"
    api_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": ALPHA_ADVANTAGE_API_KEY
    }
    respons = requests.get(alphavantage_api_url, params=api_parameters)
    respons.raise_for_status()
    data = respons.json()["Time Series (Daily)"]
    last_two_data_points = dict(list(data.items())[:2])
    closing_values = [float(entry['4. close']) for entry in list(data.values())[:2]]
    percentage_change = ((closing_values[0] - closing_values[1]) / closing_values[1]) * 100
    if percentage_change > 1: # @TODO change to 5
        return percentage_change
    return None

def get_company_news():
    print("Getting company news")
    company_news = []
    newsapi_api_url = "https://newsapi.org/v2/everything"
    api_parameters = {
        "q": COMPANY_NAME,
        "from": (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d"),
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    respons = requests.get(newsapi_api_url, params=api_parameters)
    respons.raise_for_status()
    data = respons.json()["articles"]
    for i in range(3):
        company_news.append((data[i]["title"], data[i]["description"]))
    return company_news

def send_sms(change_percentage, company_news):

    msg_text = "TSLA: "
    if change_percentage > 0:
        msg_text += f"▲ {change_percentage:.1f}%\n"
    else:
        msg_text += f"🔻{abs(change_percentage):.1f}%\n"
    for n in company_news:
        msg_text += f"Headline: {n[0]}\nBrief: {n[1]}\n\n"
    
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_= twilio_from,
        body = msg_text,
        to= my_phone
    )
    
    
change_percentage = track_stock_price()
if change_percentage is not None:
    company_news = get_company_news()
    send_sms(change_percentage, company_news)
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

