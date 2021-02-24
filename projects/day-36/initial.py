import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Twitter"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "YOUR_API_KEY"
API_KEY_NEWS = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
today = datetime.now().date()
yesterday = str(today - timedelta(1))
two_days_ago = str(today - timedelta(2))

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()["Time Series (Daily)"]
yesterdays_close = float(data[yesterday]['4. close'])
print(yesterdays_close)

#TODO 2. - Get the day before yesterday's closing stock price

two_days_ago_close = float(data[two_days_ago]['4. close'])
print(two_days_ago_close)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = round(abs(yesterdays_close - two_days_ago_close), 2)
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_diff = round(difference/yesterdays_close * 100, 2)
print(percentage_diff)
if percentage_diff > 5:
    print("get news")


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

parameters = {
    "q": STOCK_NAME,
    "from": today,
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWS
}

response = requests.get(NEWS_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()["articles"][:3]
# print(data)

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
new_list = [[{'title': item['title']}, {'description' : item['description']}] for item in data]
article_one = new_list[0]
article_one_title = article_one[0]['title']
print(article_one)
article_one_description = article_one[1]['description']
print(article_one_description)
print(article_one_title)

#TODO 9. - Send each article as a separate message via Twilio.
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body=f"{STOCK_NAME}: {percentage_diff}%\n"
         f"{article_one_title}\n"
         f"{article_one_description}",
    from_='+15168537810',
    to='+353873980798'
)
print(message.status)
