from email.message import EmailMessage  #https://docs.python.org/3/library/email.html
import os, smtplib

email_sender = os.getenv('botmail')
email_password = os.environ.get('botmailpass')
email_receiver = 'mj.cupial@gmail.com'

# server = smtplib.SMTP('smtp-mail.outlook.com', 587)
# server.starttls()
# server.login(email_sender, email_password)
# server.sendmail(email_sender, email_receiver, "Welcome from Luna Pybot!")
# print('mail sent')
with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_sender, email_password)
    subject = "My first auto email! :D"
    body = "Welcome from Luna Pybot!"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(email_sender, email_receiver, msg)
print("message siup")

