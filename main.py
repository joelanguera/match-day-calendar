from modules.authentication import *
from modules.calendar import *
from modules.email_handler import Email
from modules.scraping import *
from modules.data_handler import *
import logging
from modules.helper import *

CONFIG = get_config()


if __name__ == '__main__':
    logging.basicConfig(filename='logs/my_program.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

    credentials = authenticate_app()

    url = 'http://www.server2.sidgad.es/fecapa/fecapa_cal_idc_2218_1.php'
    response = make_post_request(url, dict(CONFIG['FECAPA_POST_DATA']), headers=dict(CONFIG['FECAPA_POST_HEADERS']))
    if not response:
        logging.error("Error retrieving data from url: {}".format(url))
        exit()
    save_to_file('data/fecapa_cal_idc_2218_1.php', response)

    calendar_events = get_events(credentials)

    fecapa_events = get_match_days("data/fecapa_cal_idc_2218_1.php")
    saved_events_id_list = load_or_create_json_from_file("data/match_day_event.json")
    message_text = ""
    for fecapa_event in fecapa_events:
        saved_event_id = saved_events_id_list.get(fecapa_event.match_day_number)
        calendar_event = next((evento for evento in calendar_events.get('items', []) if evento['id'] == saved_event_id), None)
        if not calendar_event:
            new_event = Event(fecapa_event.localTeam.name + ' - ' + fecapa_event.visitantTeam.name,
                              fecapa_event.match_day_number, fecapa_event.date_time)
            result = create_event(credentials, new_event.get_event())
            save_event_match_day(fecapa_event.match_day_number, result['id'])

        else:
            new_event = Event(fecapa_event.localTeam.name + ' - ' + fecapa_event.visitantTeam.name,
                              fecapa_event.match_day_number, fecapa_event.date_time)
            if calendar_event['start']['dateTime'] != new_event.start_datetime.isoformat():
                old_datetime = calendar_event['start']['dateTime']
                calendar_event['start']['dateTime'] = new_event.start_datetime.isoformat()
                calendar_event['end']['dateTime'] = new_event.end_datetime.isoformat()

                message_text += (f"Partit: {new_event.summary}\n"
                                 f"   Antic horari: {old_datetime}\n"
                                 f"   Nou horari: {new_event.start_datetime.isoformat()}\n\n")
                update_event(credentials, saved_event_id, calendar_event)
    if message_text:
        subject = "Actualització d'horaris partits"
        email = Email("joel.anguera@gmail.com", subject, message_text)
        email.send()
