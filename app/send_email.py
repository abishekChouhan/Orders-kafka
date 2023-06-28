import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import MAIL_FROM, MAIL_TO, MAIL_PASSWORD


class EmailException(Exception):
    pass


def send_email(email_to, subject, body):
    try:
        message = MIMEMultipart()
        message['From'] = MAIL_FROM
        message['To'] = email_to
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(MAIL_FROM, MAIL_PASSWORD)
        text = message.as_string()
        session.sendmail(MAIL_FROM, MAIL_TO, text)
        session.quit()
    except Exception as e:
        raise EmailException(e)
