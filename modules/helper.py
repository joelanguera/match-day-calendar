import re
import os
import configparser

CURRENT_DIRECTORY = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(CURRENT_DIRECTORY, '../config/config.ini')


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    return config


def clean_text(text):
    return re.sub(r'[^\x20-\xFF]+', '', text)
