from email.message import EmailMessage  #https://docs.python.org/3/library/email.html
import os, smtplib, re

email_sender = os.getenv('botmail')
email_password = os.environ.get('botmailpass')
email_receiver = 'mj.cupial@gmail.com'
regex_receiver = re.compile(r'^[a-z0-9_.+-]+', re.I)
nick_receiver = (regex_receiver.search(email_receiver)).group()
print(nick_receiver)

with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
    # smtp.ehlo()
    smtp.starttls()
    # smtp.ehlo()

    smtp.login(email_sender, email_password)
    subject = "It's me, Luna! :D"
    body = f"""
    Hi {nick_receiver}!\n
    I'm Luna Pybot and I was created by Maciej Cupial. It is a test message, I... I just wanted to say hello.
    Don't worry - I don't wanna hurt ya.
    Enjoy your day! <3

    BR,
    Luna Pybot
    """

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail(email_sender, email_receiver, msg)
print("message siup")