import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = 'AC05a92e883b861d561df26a7f7c72369e'
auth_token = 'da7645f99e38569cf2745562c66931db'


today_date = dt.datetime.today()
yesterday = today_date.date() - dt.timedelta(6)
day_before_yesterday = today_date.date() - dt.timedelta(7)

parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'TSLA',
    'interval': '5min',
    'apikey': 'ETH58Y57R2H2F4WD',
}

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get('https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
data = response.json()

yesterday_close = float(data['Time Series (Daily)'][f'{yesterday}']['1. open'])
day_before_yesterday_open = float(data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close'])
# STEP 2: Use https://newsapi.org
news_params = {
    'q' : 'tesla',
    'from' : '2023-06-8',
    'sortBy' : 'publishedAt',
    'apiKey' : '08e6dc5a8295410ca160f9a3d783dddd'
}
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_response = requests.get('https://newsapi.org/v2/everything?', params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

first_three_news_pieces = news_data['articles'][:3]
if (yesterday_close * 5) / 100 + yesterday_close >= day_before_yesterday_open or (yesterday_close * 5) / 100 + yesterday_close < day_before_yesterday_open:
    news_list = [{'title':news['title'], 'description':news['description']} for news in first_three_news_pieces]

    ## STEP 3: Use https://www.twilio.com
    client = Client(account_sid, auth_token)
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    percentage_change = ('TSLA: 🔻2%', 'TSLA: 🔺5%', 'TSLA: 🔺10%' )
    for n in range(3):
        message = client.messages.create(
            body=f"{percentage_change[n]} \nHeadline: {news_list[n]['title']}\nBrief: {news_list[n]['description']}",
            from_="+15419098143",
            to="+233543166742"
        )
        print(message)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

