import smtplib
import datetime as dt 
import random


MY_EMAIL = "example@gmail.com"
PASSWORD = 'testpassword'

now = dt.datetime.now()
week_day = now.weekday()

if week_day == 5:
    with open('quotes.txt') as quotes_files:
        all_qutoes = quotes_files.readlines()
        quote = random.choice(all_qutoes)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=MY_EMAIL, 
                            msg=f"Subject: Motivational quotes \n\n{quote}")
        