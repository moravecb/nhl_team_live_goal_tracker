'''
Title: team_color_selector.py
Author: Peyton Ball
Creation Date: 02/09/2020
Last Modified: 02/21/2020
Purpose: Attempts to choose the 2 primary colors for the team specified in the
         method's parameter.
'''
# Import statements
import sys

def get_team_colors(team_abbrv):
    team_colors = {
        "ANA": ["#FF9933","#FFD700"],
        "BOS": ["#FFB81C","#FFFFFF"],
        "BUF": ["#002654","#FCB514"],
        "CAR": ["#CC0000","#A2AAAD"],
        "CGY": ["#C8102E","#E8b923"],
        "CHI": ["#CF0A2C","#00833E"],
        "COL": ["#6F263D","#236192"],
        "CBJ": ["#002654","#CE1126"],
        "DAL": ["#228B22","#8F8F8C"],
        "DET": ["#CE1126","#FFFFFF"],
        "EDM": ["#041E42","#FF9933"],
        "FLA": ["#041E42","#C8102E"],
        "LAK": ["#D3D3D3","#A2AAAD"],
        "MIN": ["#228B22","#228B22A6192E"],
        "MTL": ["#AF1E2D","#192168"],
        "NJD": ["#CE1126","#FFFFFF"],
        "NSH": ["#FFB81C","#192168"],
        "NYI": ["#00539B","#FF9933"],
        "NYR": ["#0038A8","#CE1126"],
        "OTT": ["#C52032","#C2912C"],
        "PHI": ["#FF9933","#FFFFFF"],
        "PHX": ["#8C2633","E2D6B5"],
        "PIT": ["#CFC493","#FCB514"],
        "SJS": ["#00CED1","#FF9933"],
        "STL": ["002F87","FCB514"],
        "TBL": ["#002868","#FFFFFF"],
        "TOR": ["#00205B","#FFFFFF"],
        "VAN": ["#192168","#228B22"],
        "VGK": ["#FFD700","#333F42"],
        "WPG": ["#192168","#FFFFFF"],
        "WSH": ["#192168","#C8102E"],
    }
    try:
        return team_colors[team_abbrv]
    except:
        sys.exit("ERROR: {} is not a valid team abbreviation. Exiting...".format(team_abbrv))
