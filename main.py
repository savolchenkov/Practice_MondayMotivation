# import smtplib
#
# my_email = "sergeicorleone91@gmail.com"
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="savolchenkov@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1991, month=10, day=11)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

MY_EMAIL = "sergeicorleone91@gmail.com"
PASSWORD = "erklwzdusqzdyueo"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com",  port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="savolchenkov@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{quote}")


