# testing mlb stats api

import mlbstatsapi
import datetime

mlb = mlbstatsapi.Mlb()

# Desired team
TEAM_NAME = "San Diego Padres" #  Change this to get schedule for other teams
TEAM_ID = mlb.get_team_id(TEAM_NAME)[0]
team = mlb.get_team(team_id=TEAM_ID)

# Check if team is playing today
today = str(datetime.date.today())
# today = str(datetime.date.today() + datetime.timedelta(days=1))
schedule = mlb.get_schedule(date=today, team_id=TEAM_ID)

if schedule == None: # If team does not play today, check tomorrow
    tomorrow = str(datetime.date.today() + datetime.timedelta(days=1))
    schedule = mlb.get_schedule(date=tomorrow, team_id=TEAM_ID)

dates = schedule.dates[0]
game = dates.games[0]

# game_json = game.model_dump_json(indent=2)
# with open('game_data.json', 'w') as f:
#     f.write(game_json)


HOME_TEAM = game.teams.home.team.name
HOME_TEAM_ID = game.teams.home.team.id

AWAY_TEAM = game.teams.away.team.name
AWAY_TEAM_ID = game.teams.away.team.id

print(AWAY_TEAM + " @ " + HOME_TEAM)

GAME_STATUS = game.status.detailed_state

HOME_TEAM_SCORE = game.teams.home.score
AWAY_TEAM_SCORE = game.teams.away.score
print(GAME_STATUS)
if(GAME_STATUS == "Final"): # Game has ended
    # Determine winner
    if HOME_TEAM_SCORE > AWAY_TEAM_SCORE:
        WINNER = HOME_TEAM
        WINNER_SCORE = HOME_TEAM_SCORE
        WINNER_ABBREV = mlb.get_team(team_id=HOME_TEAM_ID).abbreviation
        
        LOSER = AWAY_TEAM
        LOSER_SCORE = AWAY_TEAM_SCORE
        LOSER_ABBREV = mlb.get_team(team_id=AWAY_TEAM_ID).abbreviation
    else:
        WINNER = AWAY_TEAM
        WINNER_SCORE = AWAY_TEAM_SCORE
        WINNER_ABBREV = mlb.get_team(team_id=AWAY_TEAM_ID).abbreviation
        
        LOSER = HOME_TEAM
        LOSER_SCORE = HOME_TEAM_SCORE
        LOSER_ABBREV = mlb.get_team(team_id=HOME_TEAM_ID).abbreviation        
    print("RESULT: " + WINNER_ABBREV + " " + str(WINNER_SCORE) + ", " + LOSER_ABBREV + " " + str(LOSER_SCORE))    
elif(GAME_STATUS == "Scheduled" or GAME_STATUS == "Warmup"): # Game has not started
    
    game_location = game.venue.name
    print("Location: " + game_location)
    print("Time: ")
    print("Pitchers: ")
else: # Game currently ongoing
    print("Score: " + str(HOME_TEAM_SCORE) + " - " + str(AWAY_TEAM_SCORE))
    print("Inning: ")
    print("Current Pitcher: ")
    print("Current Batter: ")