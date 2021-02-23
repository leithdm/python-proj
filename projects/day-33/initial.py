import requests
from tkinter import *
from datetime import datetime

# RESPONSES
#1: information
#2: success
#3: redirection
#4: client error
#5: server error

# 1. ISS LAT/LONG
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
# # better to just use requests module rather that re-invent the wheeel like above
# response.raise_for_status()
# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

# 2. KANYE AS A SERVICE...
# basic code
# response = requests.get("https://api.kanye.rest")
# response.raise_for_status()
# print(response.json()["quote"])

# def get_quote():
#     response = requests.get("https://api.kanye.rest")
#     response.raise_for_status()
#     quote = response.json()["quote"]
#     canvas.itemconfig(quote_text, text=quote)
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Click for Kanye", width=250, font=("Arial", 20, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

# 3. SUNRISE AND SUNSET
# https://sunrise-sunset.org/api
# response = requests.get(url="https://api.sunrise-sunset.org/json?lat=53.2626911&lng=-6.1240941")

MY_LAT = 59.2626911
MY_LONG = -8.1240941

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

# If the ISS is close to my current position
# and its currently dark, then send an email to me to look up