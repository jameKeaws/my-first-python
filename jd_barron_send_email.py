import smtplib, ssl
from email.mime.text import MIMEText

# https://realpython.com/python-send-email/
# https://mailtrap.io/blog/python-send-email-gmail/#:~:text=To%20send%20an%20email%20with,Transfer%20Protocol%20(SMTP)%20server.
smtp_server = "smtp.gmail.com"
port = 465
sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"
password = input("Type your password and press Enter:")

message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender_email, password)
       smtp_server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    # smtp_server.quit()
    print("I think we sent an email")