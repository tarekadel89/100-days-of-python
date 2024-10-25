##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import smtplib
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Configuration
CSV_PATH = 'Day 032 Birthday Wisher/birthdays.csv'
LETTER_TEMPLATE_DIR = 'Day 032 Birthday Wisher/letter_templates'
NUM_LETTER_TEMPLATES = 3
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def load_birthdays(filename):
    try:
        # Try to read the CSV file
        df = pd.read_csv(filename)
        return df.to_dict('records')
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{filename}' is empty.")
        return None
    
    except pd.errors.ParserError:
        print(f"Error: Unable to parse '{filename}'. Please ensure it's a valid CSV file.")
        return None
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None
    

def check_birthday(birthday_list):
    todays_birthdays = []
    current_month = dt.date.today().month
    current_day = dt.date.today().day
    for bithday in birthday_list:
        if bithday['month'] == current_month and bithday['day'] == current_day:
            todays_birthdays.append({"name":bithday['name'],"email":bithday['email']})
    return todays_birthdays


def read_letter_template(template_path, name):
    try:
        with open(template_path, 'r') as file:
            letter = file.read()
            # Replace [name] with the actual name
            letter = letter.replace('[NAME]', name)
            return letter
    except FileNotFoundError:
        print(f"Error: The template file '{template_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the template: {str(e)}")
        return None
 
def send_email(letter, recipient):
    username = "tarekadel89@gmail.com"
    password = "PASSWORD"

    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = recipient
        msg['Subject'] = "Happy Birthday"
        body = letter
        msg.attach(MIMEText(body, 'plain'))

        # Establish the connection
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
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

def prepare_email(todays_birthdays):
    for birthday in todays_birthdays:
        letter_path = f"{LETTER_TEMPLATE_DIR}/letter_{random.randint(1,NUM_LETTER_TEMPLATES)}.txt"
        letter = read_letter_template(letter_path, birthday['name'])
        if letter is not None:
            print(f"Sending birthday wishes to {birthday['name']} ({birthday['email']})")  # Uncomment this line to print the recipient names for debugging.  #
            send_email(letter, birthday['email'])
        

# Example usage:
birthday_list = load_birthdays(CSV_PATH)

if birthday_list is not None:
    print("Successfully loaded birthdays:")
    print(f"Loaded {len(birthday_list)} birthday records.")
    todays_birthdays = check_birthday(birthday_list)
    if todays_birthdays:
        prepare_email(todays_birthdays)  # Uncomment this line to send emails when there are birthdays today.

else:
    print("Failed to load birthday data.")






