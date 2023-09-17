from google_auth_oauthlib.flow import InstalledAppFlow


def authenticate_app(credentials_json):
    scopes = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file(
        credentials_json,
        scopes=scopes
    )
    credentials = flow.run_local_server(port=0)
    with open('token.json', 'w') as token_file:
        token_file.write(credentials.to_json())
    return credentials


