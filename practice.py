from nba_api.stats.endpoints import ScoreboardV2
from nba_api.live.nba.endpoints import scoreboard
from datetime import date, timedelta
import pandas as pd
import re

#Today's Score Board
todays_scoreboard = scoreboard.ScoreBoard()

todays_scoreboard_api_response = todays_scoreboard.get_dict()['scoreboard']

#prints the 4 keys available =========
#for x in todays_scoreboard_api_response:
  #  print(x)


#prints a key's value such as 'games'======
#print(todays_scoreboard_api_response['games'])


# trying to access the 'first' and 'second' row of data?======
'''=====
test_row = todays_scoreboard_api_response['games']

if test_row:
    first_row = test_row[0]
    print(f'First Row Data: {first_row}')
    second_row = test_row[1]
    print(f'=======Second Row Data: {second_row}')
'''





'''
#yesteday's date function 
try:
    yesterday = date.today() - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", yesterday_date)
except AssertionError:
    print("Wrong date!")



#scoreboard function 
try:
    games = ScoreboardV2(game_date=yesterday_date, league_id='00')
    games_header = games.get_data_frames()[0]

    pd.options.display.max_columns = None  # Show all columns
    #pd.options.display.max_columns = 20 #or set a specific amount.
    print("Game Header:")
    print(games_header)  # Now print the DataFrame directly

except Exception as e:
    print(f'An error occurred: {e}')'''



##trying to iterate through the nested lists within the scoreboard['games'] response dictionary which contains most of the data 

test_rows = todays_scoreboard_api_response['games']

#printing 76ers
print(test_rows[3]['homeTeam']['teamName'])
#printing opponents of 76ers
print(test_rows[3]['awayTeam']['teamName'])



try:
    lakers_found = False
    search_team = 'Lakers'

    for row in test_rows:
        away_team = row.get('awayTeam', {}).get('teamName', None)
        home_team = row.get('homeTeam', {}).get('teamName', None)
        print("away team:====", away_team)
        print("home team:====", home_team)
    
        if away_team and search_team in away_team:
            print(f'The {search_team} are playing against: {home_team}')
            lakers_found = True
            break
        elif home_team and search_team in home_team:
            print(f"The {search_team} will feel right at home..")
            print(f".. as they take on the {away_team}")
            lakers_found = True
            break
    if not lakers_found:
        print(f'{search_team} could not be found')

except Exception as e:
    print(f'An error occured: {e}')


