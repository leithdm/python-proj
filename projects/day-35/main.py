import requests
from twilio.rest import Client
import os

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("API_KEY")
account_sid = "AC3498c176e98b94370ceb8b2557bc2e5d"
auth_token = "d98f3a60052b23da8d84dcc29d54e553"

LAT = 53.2626911
LONG = -6.1240941

parameters = {
    "lat" : LAT,
    "lon" : LONG,
    "exclude" : "current,minutely,daily",
    "appid" : API_KEY
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
# make use of slice to get the first 12 elements from array
weather_data = response.json()["hourly"][:12]
# print(weather_data)

will_rain = False
new_list = [hour["weather"][0]["id"] for hour in weather_data]
for id in new_list:
    if id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='+15168537810',
        to='+353873980798'
    )
    print(message.status)
