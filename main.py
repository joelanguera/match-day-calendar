from modules.authentication import *
from modules.calendar import *
from modules.scraping import *
from modules.data_handler import *


if __name__ == '__main__':
    response = request_webpage('http://www.server2.sidgad.es/fecapa/fecapa_cal_idc_2218_1.php')
    if not response:
        exit()
    save_to_file('data/fecapa_cal_idc_2218_1.php', response)

    credentials = authenticate_app()
    calendar_events = get_events(credentials)

    fecapa_events = get_match_days("data/fecapa_cal_idc_2218_1.php")
    saved_events_id_list = load_or_create_json_from_file("data/match_day_event.json")
    for fecapa_event in fecapa_events:
        saved_event_id = saved_events_id_list.get(fecapa_event.match_day_number)
        calendar_event = next((evento for evento in calendar_events.get('items', []) if evento['id'] == saved_event_id), None)
        if not calendar_event:
            new_event = Event(fecapa_event.localTeam.name + ' - ' + fecapa_event.visitantTeam.name,
                              fecapa_event.match_day_number, fecapa_event.date_time)
            result = create_event_dry_run(credentials, new_event.get_event())
            save_event_match_day(fecapa_event.match_day_number, result.id)

        else:
            new_event = Event(fecapa_event.localTeam.name + ' - ' + fecapa_event.visitantTeam.name,
                              fecapa_event.match_day_number, fecapa_event.date_time)
            if calendar_event['start']['dateTime'] != new_event.start_datetime:
                calendar_event['start']['dateTime'] = new_event.start_datetime.isoformat()
                calendar_event['end']['dateTime'] = new_event.end_datetime.isoformat()
                update_event(credentials, saved_event_id, calendar_event)
