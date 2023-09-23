from modules.authentication import authenticate_app
from modules.calendar import get_events, Event, create_event
from modules.scraping import get_match_days


if __name__ == '__main__':
    credentials = authenticate_app()

    events = get_events(credentials)
    match_days = get_match_days("data/fecapa_cal_idc_2218_1.php")

    event = Event(match_days[2].localTeam.name + ' - ' + match_days[2].visitantTeam.name, match_days[2].date_time)

    # result = create_event(credentials, event.get_event())
    # '7mvig6l8jmtlmkuulphapcg16g'
    for match_day in match_days:
        print(f"Date: {match_day.date}, Hour: {match_day.hour}")
        print(f"Local Team: {match_day.localTeam}, Visitor Team: {match_day.visitantTeam}")
        print(f"Result: {match_day.result}\n")
