
from datetime import datetime
import pandas as pd
import random
from email.message import EmailMessage
import ssl
import smtplib

PLACEHOLDER = '[NAME]'
MY_EMAIL = "from.muhammadfarhan@gmail.com"
MY_PASSWORD = "wcwplcwwvrqitngr"


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthdays_data = pd.read_csv("./birthdays.csv")
birthday_list = birthdays_data.to_dict(orient='records')

today = datetime.now()

for birthday in birthday_list:
    if today.month == birthday['month'] and today.day == birthday['day']:
        file_path = f"./letter_templates/letter_{random.randint(1, 10)}.txt"
        with open(file_path) as letter:
            letter_content = letter.read()
            letter_content = letter_content.replace(PLACEHOLDER, birthday['name'])
        em = EmailMessage()
        em['From'] = MY_EMAIL
        em['To'] = birthday['email']
        em['Subject'] = "Happy Birthday!"
        body = letter_content
        em.set_content(body)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', context=context) as con:
            con.login(MY_EMAIL, MY_PASSWORD)
            con.sendmail(MY_EMAIL, birthday['email'], em.as_string())
print("All Done!")



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# import smtplib
#
# my_email = "muhammad_farhanmalik@yahoo.com"
# password = ""
#
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="muhammad_farhanmalik@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()
# # Note: Use your phone to sign in and 2-Step Verification are both turned off
# #--------------------------------------------------
#
# import datetime as dt
# datetime = dt.datetime()
# now = datetime.now()
# year = now.year
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=2002, month=5, day=1)
#
#
# with open("quotes.txt" as quotes:
# 	quote_list = quotes.readlines()
# 	random_quote = random.choice(quote_list)

# Note: On the Less secure app access
