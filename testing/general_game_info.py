# testing a different mlb stats api

import statsapi
from datetime import datetime
import pytz

team = statsapi.lookup_team("Padres")
team_id = team[0]['id']
# print(team_id)

try:
    game = statsapi.schedule(team=team_id)[0]
    # game = statsapi.schedule(date="4/27/2026", team=team_id)[0]
except IndexError:
    print("Do not play today")
    exit(1)

# print(game)

print(f"{game['away_name']} @ {game['home_name']}")

status = game['status']

home_team = {
    "name" : game['home_name'],
    "abbreviation" : "test",
    "score" : game['home_score']
}

away_team = {
    "name" : game['home_name'],
    "abbreviation" : "TEST",
    "score" : game['home_score']
}

if status == 'Final':
    # winner = home_team if home_score > away_score else away_team
    winner = home_team if home_team['score'] > away_team['score'] else away_team
    print(f'{status}: {winner['score']}')
else:
    game_datetime = game['game_datetime']
    utc_dt = datetime.strptime(game_datetime, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.UTC)
    pacific_tz = pytz.timezone("America/Los_Angeles")
    pacific_dt = utc_dt.astimezone(pacific_tz)
    time_only = pacific_dt.strftime('%I:%M %p')
    print(f"{time_only}")
    print(f"{game['away_probable_pitcher']} vs {game['home_probable_pitcher']}")
