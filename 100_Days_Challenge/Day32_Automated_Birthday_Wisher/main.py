# import smtplib

import datetime as dt

# username = "sadhhhhq599@yrg43gae.q4qga"
# password="aqerhaer"


# connection = smtplib.SMTP(host="<stp server>", port= 465)
# connection.starttls() # => securiong the connection
# connection.login(user  = username, password=password)
# connection.sendmail(from_addr= username, to_addrs= "<mail address>", msg="Subject: Test Mail from python\n\n Hello boy")

# connection.close()

print(dt.datetime.now())

dateObj = dt.datetime.now()
year = dateObj.year
print(year)

date_of_birth = dt.datetime(year= 1945, month= 9, day = 6)
print(date_of_birth)