from bs4 import BeautifulSoup
from .helper import clean_text
from .matchday import MatchDay
from .matchday import Team
import requests
import logging


def make_post_request(url, data, headers):
    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        logging.info("Response code 200 on requested url: '%s'.", url)
        return response.text
    else:
        logging.error("Response code '%s' on requested url: '%s'.", response.status_code, url)
        return None


def make_get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        logging.info("Response code 200 on requested url: '%s'.", url)
        return response.text
    else:
        logging.error("Response code '%s' on requested url: '%s'.", response.status_code, url)
        return None


def get_match_days(filename):
    with open(filename) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    tables = soup.find_all('table')
    match_days = []

    for table in tables:
        if 'MANRESA' in table.get_text():
            for row in table.find_all('tr'):
                if 'MANRESA' not in row.text:
                    continue

                columns = row.find_all('td')
                date = clean_text(columns[1].text)
                hour = clean_text(columns[2].text)
                match_day_number = clean_text(columns[4].text)
                local_team = Team(columns[6].text)
                visitant_team = Team(columns[8].text)
                result = clean_text(columns[11].text)

                match_day = MatchDay(date=date, hour=hour, match_day_number=match_day_number, local_team=local_team,
                                     visitant_team=visitant_team, result=result)
                match_days.append(match_day)
    logging.info("File scrapped: OK")
    return match_days
