import os
from twilio.rest import Client
import requests

ACCOUNT_SID = "AC3fa133bb4aa764b11cba58db5d036a54"
AUTH_TOKEN = "158c09ba3081e2e4b094a6e220109e1a"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API = "6443794787c24c238652f58bf84c693b"
parameters = {
    "function":"TIME_SERIES_DAILY",
    "apikey":"1MIVJZMBYNROCAWB",
    "symbol": STOCK_NAME,
}
API_KEY = "1MIVJZMBYNROCAWB"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
#Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_data_closing_price = yesterday_data['4. close']
#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']
#Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = (float(yesterday_data_closing_price) - float(day_before_yesterday_data_closing_price))
up_down = None
if difference > 0:
    up_down = "^"
#Two of ^^ means a down symbol for this project :)
else:
    up_down = "^^"
#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round(difference / float(yesterday_data_closing_price)) * 100

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percentage) > 0:
    news_parameter = {
        'apiKey':NEWS_API,
        'qInTitle':COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameter)
    article = news_response.json()['articles']

    # Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = article[:3]
    print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_article = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\n Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    #TODO 9. - Send each article as a separate message via Twilio. 
    # Download the helper library from https://www.twilio.com/docs/python/install


    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ[ACCOUNT_SID]
    auth_token = os.environ[AUTH_TOKEN]
    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages \
                        .create(
                            body=article,
                            from_='YOUR TWILIO PHONE NUMBER',
                            to='THE PHONE YOU VERIFIED IT WITH'
                        )

        print(message.sid)



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
