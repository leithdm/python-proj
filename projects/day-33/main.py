import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.2626911
MY_LONG = -6.1240941
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

# If the ISS is close to current position
# and its currently dark, then send an email to say 'look up'
def iss_overhead():
    return abs(iss_latitude-MY_LAT) <= 5 and abs(iss_longitude) <= 5

def is_dark():
    return time_now >= sunset or time_now <= sunrise

while True:
    # run the script every minute
    time.sleep(60)
    if iss_overhead() and is_dark():
        # send an email
        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Look up!\n\nThe ISS should be overhead."
            )
