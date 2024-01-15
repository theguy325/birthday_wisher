import smtplib
import datetime
import random
from quotes import all_quotes

my_birthday = datetime.datetime(year=1995, month=1, day=14)
message = random.choice(all_quotes)

if datetime.datetime.now().month == my_birthday.month and datetime.datetime.now().day == my_birthday.day:
    my_email = "sendernishant@gmail.com"
    my_password = "wyoehtipnawizghf"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(to_addrs='5511nishant@gmail.com', from_addr=my_email, msg=f"Subject: Happy Birthday!!\n\n{message}")



print("It's completed!")