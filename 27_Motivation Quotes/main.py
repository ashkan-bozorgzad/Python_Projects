#To run and test the code you need to update 3 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.


import datetime as dt
import smtplib
import random

my_email = "YOUR EMAIL"
password = "YOUR PASSWORD"
TODAY = 0

now = dt.datetime.now()

with open("quotes.txt", mode="r") as file:
    all_quotes = file.readlines()
    quote = random.choice(all_quotesS)

if now.weekday() == TODAY:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Today Motivation\n\n{quote}",
                            )
# import smtplib
#
# my_email = "@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="@outlook.com",
#                         msg="Subject:hello\n\nThis is a test to send and email.",
#                         )

# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# print(type(now))
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=1991, month=4, day=23,)
# print(date_of_birth)



