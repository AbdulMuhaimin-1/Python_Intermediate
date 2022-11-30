import datetime as dt
import random
import smtplib

my_email = 'kinghaimin10@gmail.com'
password = 'mgcffmmwdpjpszgh'

current_date_and_time = dt.datetime.now()
current_day = current_date_and_time.weekday()

if current_day == 2:
    with open('quotes.txt', 'r') as data:
        quotes_list = data.readlines()
        quote_to_send = random.choice(quotes_list)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='yussif.muhaimin4@gmail.com',
                msg=f'Subject: MOTIVATION OF THE DAY\n{quote_to_send}'
            )


# import smtplib
#
# my_email = 'kinghaimin10@gmail.com'
# password = 'mgcffmmwdpjpszgh'
# #
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='queenhaimin@yahoo.com',
#         msg='Subject:Hello\n\nHi there.'
#     )
#     connection.close()

# import datetime as dt
#
# current_date_and_time = dt.datetime.now()
# current_year = current_date_and_time.year
# current_month = current_date_and_time.month
# day = current_date_and_time.weekday()
# print(day)
# print(current_month)
# # if current_year == 2022:
# #     print("Good")
# # else:
# #     print("Bad")
# # print(current_date_and_time)
# # print(current_year)
#
# date_of_birth = dt.datetime(year=1995, month=9, day=14, hour=4)
# print(date_of_birth)

