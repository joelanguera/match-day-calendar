import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2 import service_account
from datetime import datetime
import logging

GCALENDAR_SCOPE = ['https://www.googleapis.com/auth/calendar']
GMAIL_SCOPE = ['https://www.googleapis.com/auth/gmail.send']
CURRENT_DIRECTORY = os.path.dirname(__file__)
SERVICE_ACCOUNT_FILE = os.path.join(CURRENT_DIRECTORY, '../credentials/client_secret_501958182067-kglkrtk62jmcsae2dojk84jf8e9celmp.apps.googleusercontent.com.json')
GOOGLE_APPLICATION_CREDENTIALS = os.path.join(CURRENT_DIRECTORY, '../credentials/matchday-399222-0debd6b10c87.json')
TOKEN_FILE_PATH = os.path.join(CURRENT_DIRECTORY, '../credentials/token.pickle')


def get_gmail_credentials():
    credentials = service_account.Credentials.from_service_account_file(
        GOOGLE_APPLICATION_CREDENTIALS, scopes=GMAIL_SCOPE
    )
    return credentials


def authenticate_app():
    try:
        with open(TOKEN_FILE_PATH, 'rb') as token_file:
            credentials = pickle.load(token_file)
            if credentials.expiry <= datetime.utcnow():
                credentials = renew_token()
                logging.info("Access token renewed")

    except (FileNotFoundError, pickle.UnpicklingError):
        credentials = renew_token()
        logging.info("Access token renewed")

    with open(TOKEN_FILE_PATH, 'wb') as token_file:
        pickle.dump(credentials, token_file)

    return credentials


def renew_token():
    flow = InstalledAppFlow.from_client_secrets_file(SERVICE_ACCOUNT_FILE, GCALENDAR_SCOPE)
    credentials = flow.run_local_server(port=0)
    return credentials
