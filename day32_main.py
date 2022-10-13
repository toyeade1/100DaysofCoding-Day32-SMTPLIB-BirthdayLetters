import smtplib
import datetime as dt
import random
now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    with open('quotes.txt') as data:
        quotes = data.readlines()
        random_quote = random.choice(quotes)

    my_email = 'random@gmail.com'
    my_password = 'random'
    other_email = 'random@yahoo.com'

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f'Subject:Quote of The Day\n\n{random_quote}')

