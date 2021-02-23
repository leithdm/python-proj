import smtplib
import datetime as dt
from random import choice, randint
import pandas

# The main issue with this code is security. They security settings of gmail account has to be
# lowered in order for this to work
my_email = "TEST@gmail.com"
password = "PASSWORD"

# BASICS
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # transport layer security encrypts email
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="TEST@gmail.com",
#         msg="Subject: Hello\n\n This is the body of my email"
#     )

# now = dt.datetime.now()
# land_on_moon = dt.datetime(year=1969, month=7, day=20)
# print(now)
# print(land_on_moon)


# MINI-PROJECT: send a motivational quote every 'x' (e.g. Monday) day of the week
# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     # read from .txt file and convert to a list
#     with open("quotes.txt") as quotes_file:
#         quotes_list = quotes_file.readlines()
#         quote = choice(quotes_list)
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         # transport layer security encrypts email
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="TEST@gmail.com",
#             msg=f"Subject: Motivational Quote\n\n {quote}"
#         )
#

# test-code below taken from main.py
# this is the meat of the code. Nice use of tuple to get data in format wanted
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
birthday_person = birthdays_dict[(2, 23)] #sample month/day from birthdays.csv
# choose a random letter template
file_path = f"letter_templates/letter_{randint(1,3)}.txt"
with open(file_path) as letter_file:
    contents = letter_file.read()
    print(type(contents)) #its a string. Dont use readlines() here !
    # nice use of replace
    contents = contents.replace("[NAME]", birthday_person["name"])
    print(contents)