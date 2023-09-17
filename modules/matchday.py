class MatchDay:
    def __init__(self, date, hour, match_day_number, local_team, visitant_team, result):
        self.date = date
        self.hour = hour
        self.match_day_number = match_day_number
        self.localTeam = local_team
        self.visitantTeam = visitant_team
        self.result = None if len(result) <= 3 else result


class Team:
    def __init__(self, full_name):
        lines = full_name.strip().split('\n')
        self.name = lines[0]
        self.shortName = lines[1]
