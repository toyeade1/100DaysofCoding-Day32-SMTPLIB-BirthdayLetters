
import datetime as dt
import pandas as pd
import random
import smtplib

today_date = dt.datetime.now()
today_month = today_date.month
today_day = today_date.day
today = (today_month, today_day)

date = pd.read_csv('birthdays.csv')
date_dict = date.to_dict()
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in date.iterrows()}

if today in birthday_dict:
    random_choice = random.randint(1, 3)
    birthday_person = birthday_dict[today]
    file_path = f'./letter_templates/letter_{random_choice}.txt'
    with open(file_path) as file:
        content = file.read()
        name = birthday_person['name']
        content = content.replace("name", name)
        content = content.replace('Angela', 'Toye')

    my_email = 'randomEmail@gmail.com'
    my_password = 'RandomPassword'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f'Subject: Happy Birthday {name}!!\n\n{content}')
