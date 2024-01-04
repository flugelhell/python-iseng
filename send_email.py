import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sender@gmail.com"  # Enter your address
receiver_email = "receiver@gmail.com"  # Enter receiver address
password = 'password'  # input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# tambahin image in body and attachment
