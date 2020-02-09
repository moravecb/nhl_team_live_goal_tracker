import requests
import json
import sys
import time
from datetime import datetime as dt
import os
import argparse
import goal_horn_selector

goal_count = 0
is_initial_fetch = True
goal_horn = ""

def fetch_update(team_abbrv):
    # Pull in global vars
    global is_initial_fetch
    global goal_count
    global goal_horn

    team_is_playing = False # Assume team isn't valid until verified
    response = requests.get('https://nhl-score-api.herokuapp.com/api/scores/latest')
    data = response.json()

    ### Used to read json data being returned
    #with open('data.json', 'w', encoding='utf-8') as f:
        #json.dump(data['games'], f, ensure_ascii=False, indent=4)

    for game in data['games']:
        if game['status']['state'] == "LIVE" and (game['teams']['away']['abbreviation'] == team_abbrv or game['teams']['home']['abbreviation'] == team_abbrv): # If team is playing
            team_is_playing = True
            team_score = game['scores'][team_abbrv]
            print("{} - Current Score: {} Goal(s)\n".format(team_abbrv, team_score))

            if team_score > goal_count and not is_initial_fetch:
                print("------------------")
                print("GOAL!!!!!")
                print("------------------\n")
                try:
                    os.system('afplay "{}"'.format(goal_horn)) # Plays goal horn
                except:
                    print("ERROR: Goalhorn .mp3 file couldn't be found.")
                goal_count = team_score # Updates global goal_count var to be new goal value

            else: # This is the initial fetch
                goal_count = team_score # Updates goal count to current value of live game
                is_initial_fetch = False

        elif game['status']['state'] == "FINAL" and (game['teams']['away']['abbreviation'] == team_abbrv or game['teams']['home']['abbreviation'] == team_abbrv): # Checks for winner of games that have ended
            winner_score = 0 # init value
            winner = "" # init value
            for key in game['scores']:
                if game['scores'][key] > winner_score:
                    winner = key
                    winner_score = game['scores'][key]
            if winner == team_abbrv:
                print("------------------")
                print("{} Won!!!".format(team_abbrv))
                print("------------------")
                try:
                    os.system('afplay "{}"'.format(goal_horn)) # Plays goal horn
                    sys.exit("Exiting...")
                except:
                    sys.exit("ERROR: Goalhorn .mp3 file couldn't be found.")

        elif game['status']['state'] == "PREVIEW" and (game['teams']['away']['abbreviation'] == team_abbrv or game['teams']['home']['abbreviation'] == team_abbrv): # Checks for games that haven't started yet
            sys.exit("INVALID: {} isn't playing currently. Check back later. Exiting...".format(team_abbrv))

    if team_is_playing == False:
        sys.exit("ERROR: {} can not be found for the remainder of today's games. Check back tomorrow. Exiting...".format(team_abbrv))

def goal_scraper():
    global goal_horn
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team', type=str, help="Enter team abbreviation.", default="NSH")
    parser.add_argument('-r', '--refreshrate', type=int, help="Enter the time to wait before refreshing.", default=2)
    args = parser.parse_args()
    team_name = args.team
    wait_time = args.refreshrate
    goal_horn = goal_horn_selector.get_goal_horn_file(team_name) # Gets goal horn file

    print("Starting goal_scraper...\n")
    while True:
        print("Fetching at {}".format(str(dt.now()).split(".")[0])) # Print time of fetch)
        fetch_update(team_name)
        time.sleep(wait_time)

if __name__ == '__main__':
    goal_scraper()
