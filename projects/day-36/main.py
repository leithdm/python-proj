import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "YOUR_API_KEY"
API_KEY_NEWS = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

# Get yesterdays closing price
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = yesterdays_data['4. close']

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

#Find the difference
difference = float(yesterdays_closing_price) - float(day_before_yesterday_closing_price)
stock_up_down = None
if difference > 0:
    stock_up_down = "💹"
else:
    stock_up_down = "🔻"

#Get the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round(difference/float(yesterdays_closing_price) * 100, 2)

#"Get news/sms for stock if % increase > 3"
if abs(percentage_diff) > 3:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": API_KEY_NEWS
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {stock_up_down} {percentage_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+YOUR TWILIO PHONE',
            to='+YOUR PHONE'
        )
        print(message.status)
