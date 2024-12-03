import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


'''sender_email = ""
receiver_email = ""
message = """\
Subject: Real Python

This message is sent from Python."""

port = 465  # For SSL
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("", password)
    # TODO: Send email here
    server.sendmail(sender_email, receiver_email, messagecwc)


sender_email = ""
receiver_email = ""
password = input("Type your password and press enter:")


# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a>
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
# MIMEMultipart.message.attach(part1)
# MIMEMultipart.message.attach(part2)


context = ssl.create_default_context

# python3 -m smtpd -c DebuggingServer -n localhost:1025 start a localhost

#with smtplib.SMTP_SSL("smtp.gmail", 465, context = context) as server:
with smtplib.SMTP_SSL("localhost", 1025, context = context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())



smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = input("Type your email address and press enter: ")
# sender_email = sender_email + "@gmail.com"
receiver_email = sender_email
password = input("Type your password and press enter: ")
message = input("Type your message and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()
    '''

email = ""

with smtplib.SMTP("localhost", 1025) as server:
    subject = "Fifa"
    body = "Are you up for Fifa Tomorrow?"

    msg = f'Subject: {subject} \n\n {body}'
    server.sendmail(email, '', msg)
