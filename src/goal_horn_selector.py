'''
Title: goal_horn_selector.py
Author: Peyton Ball
Creation Date: 02/08/2020
Last Modified: 02/08/2020
Purpose: Attempts to locate the goal horn for the team specified in the
         method's parameter.
'''

import sys

def get_goal_horn_file(team_abbrv):
    goal_horn = {
        "ANA": "Goal_Horn_Files/2020/Anaheim Ducks 2020 Goal Horn.mp3",
        "BOS": "Goal_Horn_Files/2020/Boston Bruins 2020 Goal Horn.mp3",
        "BUF": "Goal_Horn_Files/2020/Buffalo Sabres 2020 Goal Horn.mp3",
        "CAR": "Goal_Horn_Files/2020/Carolina Hurricanes 2020 Goal Horn.mp3",
        "CGY": "Goal_Horn_Files/2020/Calgary Flames 2020 Goal Horn.mp3",
        "CHI": "Goal_Horn_Files/2020/Chicago Blackhawks 2020 Goal Horn.mp3",
        "COL": "Goal_Horn_Files/2020/Colorado Avalanche 2020 Goal Horn.mp3",
        "CBJ": "Goal_Horn_Files/2020/Columbus Blue Jackets 2020 Goal Horn.mp3",
        "DAL": "Goal_Horn_Files/2020/Dallas Stars 2020 Goal Horn.mp3",
        "DET": "Goal_Horn_Files/2020/Detroit Red Wings 2020 Goal Horn.mp3",
        "EDM": "Goal_Horn_Files/2020/Edmonton Oilers 2020 Goal Horn.mp3",
        "FLA": "Goal_Horn_Files/2020/Florida Panthers 2020 Goal Horn.mp3",
        "LAK": "Goal_Horn_Files/2020/Los Angeles Kings 2020 Goal Horn.mp3",
        "MIN": "Goal_Horn_Files/2020/Minnesota Wild 2020 Goal Horn.mp3",
        "MTL": "Goal_Horn_Files/2020/Montreal Canadiens 2020 Goal Horn.mp3",
        "NJD": "Goal_Horn_Files/2020/New Jersey Devils 2020 Goal Horn.mp3",
        "NSH": "Goal_Horn_Files/2020/Nashville Predators 2020 Goal Horn.mp3",
        "NYI": "Goal_Horn_Files/2020/New York Islanders 2020 Goal Horn (Barclays Center).mp3",
        "NYR": "Goal_Horn_Files/2020/New York Rangers 2020 Goal Horn.mp3",
        "OTT": "Goal_Horn_Files/2020/Ottawa Senators 2020 Goal Horn.mp3",
        "PHI": "Goal_Horn_Files/2020/Philadelphia Flyers 2020 Goal Horn.mp3",
        "PHX": "Goal_Horn_Files/2020/Arizona Coyotes 2020 Goal Horn.mp3",
        "PIT": "Goal_Horn_Files/2020/Pittsburgh Penguins 2020 Goal Horn.mp3",
        "SJS": "Goal_Horn_Files/2020/San Jose Sharks 2020 Goal Horn.mp3",
        "STL": "Goal_Horn_Files/2020/St. Louis Blues 2020 Goal Horn.mp3",
        "TBL": "Goal_Horn_Files/2020/Tampa Bay Lightning 2020 Goal Horn.mp3",
        "TOR": "Goal_Horn_Files/2020/Toronto Maple Leafs 2020 Goal Horn.mp3",
        "VAN": "Goal_Horn_Files/2020/Vancouver Canucks 2020 Goal Horn.mp3",
        "VGK": "Goal_Horn_Files/2020/Vegas Golden Knights 2020 Goal Horn.mp3",
        "WPG": "Goal_Horn_Files/2020/Winnipeg Jets 2020 Goal Horn.mp3",
        "WSH": "Goal_Horn_Files/2020/Washington Capitals 2020 Goal Horn.mp3"
    }
    try:
        return goal_horn[team_abbrv]
    except:
        sys.exit("ERROR: {} is not a valid team abbreviation. Exiting...".format(team_abbrv))
