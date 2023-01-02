##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import os, random
import smtplib

my_email = 'kinghaimin10@gmail.com'
password = 'mgcffmmwdpjpszgh'
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()

for days in data.day:
    if days == today.day:
        for month in data.month:
            if month == today.month:
                birthday_details = data[data.day == days]

                # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
                messages_list = random.choice(os.listdir('./letter_templates'))
                with open(f'letter_templates/{messages_list}') as message:
                    no_name_wish = message.read()
                    name = birthday_details['name'].to_list()
                    insert_name = no_name_wish.replace('[NAME]', name[0])
                    # print(insert_name)

                # 4. Send the letter generated in step 3 to that person's email address.
                with smtplib.SMTP('smtp.gmail.com') as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs='yussif.muhaimin4@gmail.com',
                        msg=f'Subject: HAPPY BIRTHDAY\n{insert_name}'
                    )



