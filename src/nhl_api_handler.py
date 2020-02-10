'''
Title: nhl_api_handler.py
Author: Peyton Ball
Creation Date: 02/08/2020
Last Modified: 02/09/2020
Purpose: Interacts directly with the NHL API found at
         https://nhl-score-api.herokuapp.com/
'''
# Import statements
import requests
import json
import sys
import os
import goal_horn_selector

# Init
goal_count = 0
is_initial_fetch = True
goal_horn = ""

def get_goal_horn(team_abbrv):
    global goal_horn
    goal_horn = goal_horn_selector.get_goal_horn_file(team_abbrv)

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
            print("| {} - Current Score: {} Goal(s)".format(team_abbrv, team_score), end="\r")
            if team_score > goal_count and not is_initial_fetch:
                try:
                    #os.system('afplay "{}" &> /dev/null'.format(goal_horn)) # Plays goal horn
                    os.system('afplay "{}" &> /dev/null & python3 lights_api_handler.py -t {}'.format(goal_horn, team_abbrv)) # Plays goal horn & triggers lights
                    os.system('clear')
                except:
                    print("ERROR: Goalhorn .mp3 file couldn't be found.")
                print("\n-----------------------------------------------------------------------------------")
                print("GOAL!!! GOAL!!! GOAL!!! {} has scored!".format(team_abbrv))
                print("-----------------------------------------------------------------------------------\n")
                goal_count = team_score # Updates global goal_count var to be new goal value

            else: # This is the initial fetch
                goal_count = team_score # Updates goal count to current value of live game
                is_initial_fetch = False

        elif game['status']['state'] == "FINAL" and (game['teams']['away']['abbreviation'] == team_abbrv or game['teams']['home']['abbreviation'] == team_abbrv): # Checks for winner of games that have ended
            winner_score = 0 # init value
            winner = "" # init value
            team_wins = game['currentStats']['records'][team_abbrv]['wins']
            team_losses = game['currentStats']['records'][team_abbrv]['losses']
            team_ot = game['currentStats']['records'][team_abbrv]['ot']
            pts_from_playoff = game['currentStats']['standings'][team_abbrv]['pointsFromPlayoffSpot']
            for key in game['scores']:
                if game['scores'][key] > winner_score:
                    winner = key
                    winner_score = game['scores'][key]
            if winner == team_abbrv:
                try:
                    os.system('afplay "{}" &> /dev/null & python3 lights_api_handler.py -t {}'.format(goal_horn, team_abbrv)) # Plays goal horn & triggers lights
                    #os.system('afplay "{}" &> /dev/null'.format(goal_horn)) # Plays goal horn
                    os.system('clear')
                except:
                    sys.exit("ERROR: Goalhorn .mp3 file couldn't be found.")
                print("\n-----------------------------------------------------------------------------------")
                print("{} Won!!! | New Record: {}-{}-{} | Points From Playoff: {}".format(team_abbrv, team_wins, team_losses, team_ot, pts_from_playoff))
                print("-----------------------------------------------------------------------------------\n")
            else:
                print("\n-----------------------------------------------------------------------------------")
                print("{} Lost!!! | New Record: {}-{}-{} | Points From Playoff: {}".format(team_abbrv, team_wins, team_losses, team_ot, pts_from_playoff))
                print("-----------------------------------------------------------------------------------\n")
            sys.exit("Thanks for checking in! Exiting...")

        elif game['status']['state'] == "PREVIEW" and (game['teams']['away']['abbreviation'] == team_abbrv or game['teams']['home']['abbreviation'] == team_abbrv): # Checks for games that haven't started yet
            sys.exit("\nINVALID: {} isn't playing currently. Check back later. Exiting...".format(team_abbrv))

    if team_is_playing == False:
        sys.exit("\n{} can not be found for the remainder of today's games. Check back tomorrow. Exiting...".format(team_abbrv))
