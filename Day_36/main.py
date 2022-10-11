import requests

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
data_list = [value for key, value in data.items()]
yesterday_data = data_list[0]
yesterday_data_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_data_closing_price = day_before_yesterday_data['4. close']

difference = abs(float(yesterday_data_closing_price) - float(day_before_yesterday_data_closing_price))

diff_percentage = (difference / float(yesterday_data_closing_price)) * 100

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if diff_percentage > 0:
    news_parameter = {
        'apiKey':NEWS_API,
        'qInTitle':COMPANY_NAME,
    }


    requests.get(NEWS_ENDPOINT, params=news_parameter)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



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
