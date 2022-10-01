##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd 
import random
from datetime import datetime 
import smtplib 

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('./bd.csv')
birthday_dict= {(data_row['month'], data_row['day']): data_row for index, data_row in data.items()}
if today_tuple in birthday_dict:
    pass


