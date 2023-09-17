from modules.authentication import authenticate_app
from modules.calendar import get_events
from modules.scraping import get_match_days


if __name__ == '__main__':
    credentials = authenticate_app(
        './credentials/client_secret_501958182067-kglkrtk62jmcsae2dojk84jf8e9celmp.apps.googleusercontent.com.json')

    events = get_events(credentials)
    match_days = get_match_days("data/fecapa_cal_idc_2218_1.php")

    for match_day in match_days:
        print(f"Date: {match_day.date}, Hour: {match_day.hour}")
        print(f"Local Team: {match_day.localTeam}, Visitor Team: {match_day.visitantTeam}")
        print(f"Result: {match_day.result}\n")
