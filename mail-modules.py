from email.message import EmailMessage  #https://docs.python.org/3/library/email.html
import os, ssl, smtplib
def send_email():
    email_sender = os.getenv('BOTMAIL')
    email_password = os.environ.get('BOTPASS')
    email_receiver = 'mj.cupial@gmail.com'
    subject = "Welcome form Fifi Bot!"
    body = """
    This is my first mail sent to you. I'm so excited! :D
    """
    # em = EmailMessage()
    # em['From'] = email_sender
    # em['To'] = email_receiver
    # em['subject'] = subject
    # em.set_content(body)
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465, context=context) as smtp:
    #     smtp.login(email_sender, email_password)
    #     smtp.sendmail(email_sender, email_receiver, em.as_string())

    server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, subject)
    print('mail sent')
send_email()