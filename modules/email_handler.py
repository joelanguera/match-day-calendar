import logging
import os
import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


CURRENT_DIRECTORY = os.path.dirname(__file__)
CONFIG_FILE_PATH = os.path.join(CURRENT_DIRECTORY, '../credentials/email_credentials.ini')


class Email:
    def __init__(self, recipient_email, subject, message_text):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.sender_email = config.get('EMAIL', 'SENDER_EMAIL')
        self.sender_password = config.get('EMAIL', 'SENDER_PASSWORD')
        self.recipient_email = recipient_email
        self.subject = subject
        self.message_text = message_text

    def send(self):
        message = self._create_message()
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, self.recipient_email, message.as_string())
            server.close()
            logging.info('Message sent: {}'.format(message['id']))

        except Exception as e:
            logging.info('Error sending message: {}'.format(e))

    def _create_message(self):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.recipient_email
        message["Subject"] = self.subject
        message.attach(MIMEText(self.message_text, 'plain'))
        return message
