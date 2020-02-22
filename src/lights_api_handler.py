'''
Title: lights_api_handler.py
Author: Peyton Ball
Creation Date: 02/09/2020
Last Modified: 02/09/2020
Purpose: Attempts to choose the 2 primary colors for the team specified in the
         method's parameter.
'''
# Import statements
import requests
import argparse
import goal_horn_selector
from mutagen.mp3 import MP3
import time
import team_color_selector

# Arg parser for CLI
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--team', type=str, help="Enter team abbreviation.", default="NSH")
args = parser.parse_args()
team_name = args.team

def strobe_light(team_abbrv):
    goal_horn = goal_horn_selector.get_goal_horn_file(team_abbrv)
    goal_horn_length = round(MP3(goal_horn).info.length)
    #print(goal_horn_length)

    token = "###INSERT API TOKEN HERE###"
    headers = {
        "Authorization": "Bearer %s" % token,
    }
    team_colors = team_color_selector.get_team_colors(team_abbrv)
    team_color_1 = team_colors[0]
    team_color_2 = team_colors[1]

    data = {
        "period": 1,
        "cycles": goal_horn_length,
        "from_color": team_color_1,
        "color": team_color_2,
        "power_on": "true"
    }

    payload_off = {"Power": "off"}
    payload_on = {"Power": "on"}

    try:
        response = requests.post('https://api.lifx.com/v1/lights/all/effects/pulse', data=data, headers=headers)
        #print(response.text)
        #print(data)
        #turn_on = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload_on, headers=headers)
        #lights_off = requests.put(url="https://api.lifx.com/v1/lights/all/state", data=payload_off, headers=headers)
    except:
        print("ERROR: No lights configured or invalid token.")

strobe_light(team_name)
