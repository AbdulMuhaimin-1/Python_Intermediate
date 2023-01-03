import datetime as dt
import random
import smtplib

my_email = 'kinghaimin10@gmail.com'
password = 'mgcffmmwdpjpszgh'

today = dt.datetime.now()
current_day = today.weekday()

if current_day == 1:
    with open('quotes.txt', 'r') as data:
        quotes_list = data.readlines()
        quote_to_send = random.choice(quotes_list)

    with open('emails.txt') as email:
        for mail in email:
            print(mail)
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=mail,
                    msg=f'Subject: MOTIVATION OF THE DAY\n{quote_to_send}'
                )
