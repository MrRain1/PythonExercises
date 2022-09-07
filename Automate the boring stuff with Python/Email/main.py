import smtplib

# create connection obj
connection = smtplib.SMTP("smtp.mail.yahoo.com", 465)

#
connection.ehlo() 
connection.starttls()
connection.login("brunodu99@yahoo.it", "DarkCubo99")
connection.sendmail("brunodu99@yahoo.it", "assassin125412@outlook.com", "Test Mail\n\nHello, this is an automatic python mail\n\nBruno")
connection.quit()

# import imapclient
# connection = imapclient.IMAPClient("imap.google.com", ssl= True) 
# connection.login("mail", "password")
# connection.select_folder("INBOX", readonly = True)
# UIDs = connection.search([""])
# print(UIDs)
# connection.fetch("", "")