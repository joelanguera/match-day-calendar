import base64
from email.mime.text import MIMEText
from googleapiclient.discovery import build
import logging
import os
import configparser

CURRENT_DIRECTORY = os.path.dirname(__file__)
CONFIG_FILE_PATH = os.path.join(CURRENT_DIRECTORY, '../credentials/email_credentials.ini')


def send_message(service, user_id, message):
    try:
        message = service.users().messages().send(userId=user_id, body=message).execute()
        logging.info('Message sent: {}'.format(message['id']))
    except Exception as e:
        logging.info('Error sending message: {}'.format(e))


class Email:
    def __init__(self, recipient_email, subject, message_text):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_PATH)

        self.sender_email = config.get('EMAIL', 'SENDER_EMAIL')
        self.sender_password = config.get('EMAIL', 'SENDER_PASSWORD')
        self.recipient_email = recipient_email
        self.subject = subject
        self.message_text = message_text

    def send(self, credentials):
        service = build('gmail', 'v1', credentials=credentials)

        message = self._create_message()

        send_message(service, 'me', message)

    def _create_message(self):
        message = MIMEText(self.message_text)
        message["to"] = self.recipient_email
        message["from"] = self.sender_email
        message["subject"] = self.subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
