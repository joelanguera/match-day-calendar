import pickle
import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/calendar']
CURRENT_DIRECTORY = os.path.dirname(__file__)
SERVICE_ACCOUNT_FILE = os.path.join(CURRENT_DIRECTORY, '../credentials/client_secret_501958182067-kglkrtk62jmcsae2dojk84jf8e9celmp.apps.googleusercontent.com.json')
TOKEN_FILE_PATH = os.path.join(CURRENT_DIRECTORY, '../credentials/token.pickle')


def authenticate_app():
    try:
        with open(TOKEN_FILE_PATH, 'rb') as token_file:
            credentials = pickle.load(token_file)

    except (FileNotFoundError, pickle.UnpicklingError):
        flow = InstalledAppFlow.from_client_secrets_file(SERVICE_ACCOUNT_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)

    with open(TOKEN_FILE_PATH, 'wb') as token_file:
        pickle.dump(credentials, token_file)

    return credentials
