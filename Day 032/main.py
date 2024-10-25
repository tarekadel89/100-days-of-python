import smtplib
from smtplib import SMTPException
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
    
def send_quote(quoteText):
    username = "tarekadel89@gmail.com"
    password = "PASSWORD"

    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = "tarekadel89@gmail.com"
        msg['Subject'] = "Your Monday Motivation"
        body = quoteText
        msg.attach(MIMEText(body, 'plain'))

        # Establish the connection
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(username, password)
            connection.send_message(msg)
        print("Email sent successfully")

    except SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except TimeoutError as e:
        print(f"Timeout error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


quotes = []
try:
    with open("Day 032/quotes.txt", "r", encoding="utf-8") as quotesFile:
        quotes = quotesFile.readlines()
except FileNotFoundError:
    print("Quotes file not found.")
else:
    curr_day = dt.datetime.now().weekday()
    if curr_day == 0:
        quote = random.choice(quotes)
        send_quote(quote)