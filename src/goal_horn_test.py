import os
import goal_horn_selector
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--team', help="Enter team abbreviation.", default="NSH")
args = parser.parse_args()
team_name = args.team

goal_horn = goal_horn_selector.get_goal_horn_file(team_name)

try:
    os.system('afplay "{}" &> /dev/null'.format(goal_horn)) # Plays goal horn
except:
    print("ERROR: Goalhorn .mp3 file couldn't be found.")
