import json
import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
MATCH_DAY_EVENT_FILE = os.path.join(CURRENT_DIRECTORY, '../data/match_day_event.json')


def save_event_match_day(match_day_number, event_id):
    try:
        with open(MATCH_DAY_EVENT_FILE, 'r') as file:
            match_day_event_data = json.load(file)
    except FileNotFoundError:
        match_day_event_data = {}
    except json.decoder.JSONDecodeError:
        match_day_event_data = {}

    match_day_event_data[match_day_number] = event_id

    with open(MATCH_DAY_EVENT_FILE, 'w') as file:
        json.dump(match_day_event_data, file)


def get_event_match_day(match_day_number):
    try:
        with open(MATCH_DAY_EVENT_FILE, 'r') as file:
            match_day_event_data = json.load(file)
            return match_day_event_data.get(match_day_number)
    except FileNotFoundError:
        return None


def load_json_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def load_or_create_json_from_file(filename):
    try:
        with open(filename, 'r') as file:
            match_day_event_data = json.load(file)
            return match_day_event_data
    except FileNotFoundError:
        match_day_event_data = {}
    except json.decoder.JSONDecodeError:
        match_day_event_data = {}

    with open(filename, 'w') as file:
        json.dump(match_day_event_data, file)

    return match_day_event_data


def save_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)


def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
