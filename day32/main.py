import datetime as dt
import random
import smtplib

import pandas

birthday_people = []
now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
for row in data.iterrows():
    if row[1].month == now.month and row[1].day == now.day:
        birthday_people.append({"name": row[1].person_name, "email": row[1].email})

if birthday_people:
    with open("birthday_quotes.txt", "r") as file:
        quotes = file.readlines()

    my_email = "maxxxxxxverstappen@gmail.com"
    password = "pwxu inmm gouh fizw"

    for person in birthday_people:
        birthday_quote = random.choice(quotes).strip()

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                my_email,
                person["email"],
                "Subject:Happy Birthday!\n\nDear "
                + person["name"]
                + ",\n"
                + birthday_quote
                + "\nMax",
            )
