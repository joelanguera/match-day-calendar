import re


def clean_text(text):
    return re.sub(r'[^\x20-\xFF]+', '', text)

