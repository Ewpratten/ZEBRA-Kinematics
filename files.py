from os import listdir, path


def getEvents() -> list:
    return [o for o in listdir("events")]

def getTeamsForEvent(event: str) -> list:
    
    # Get and sort teams
    teams: list = [int(o[4:]) for o in listdir(path.join("events", event))]
    teams.sort()
    
    return teams

def getFilesForTeamForEvent(event: str, team: int) -> list:
    
    return [path.join("events", event, f"Team{team}", o) for o in listdir(path.join("events", event, f"Team{team}"))]