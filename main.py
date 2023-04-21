# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

from datetime import datetime
import pandas as pd
import random
from email.message import EmailMessage
import ssl
import smtplib

PLACEHOLDER = '[NAME]'
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

birthdays_data = pd.read_csv("birthdays.csv")
birthday_list = birthdays_data.to_dict(orient='records')

today = datetime.now()

for birthday in birthday_list:
    if today.month == birthday['month'] and today.day == birthday['day']:
        file_path = f"./letter_templates/letter_{random.randint(1, 10)}.txt"
        with open(file_path) as letter:
            letter_content = letter.read()
            letter_content = letter_content.replace(PLACEHOLDER, birthday['name'])
        msg = EmailMessage()
        msg['From'] = MY_EMAIL
        msg['To'] = birthday['email']
        msg['Subject'] = "Happy Birthday!"
        body = letter_content
        msg.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS", context=context) as connection:
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(MY_EMAIL, birthday['email'], msg.as_string())
       
