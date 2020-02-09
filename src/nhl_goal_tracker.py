import sys
import time
from datetime import datetime as dt
import os
import argparse
import nhl_api_handler
import goal_horn_selector

goal_count = 0
is_initial_fetch = True
goal_horn = ""

def nhl_goal_tracker():
    global goal_horn
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team', type=str, help="Enter team abbreviation.", default="NSH")
    parser.add_argument('-r', '--refreshrate', type=int, help="Enter the time to wait before refreshing.", default=2)
    args = parser.parse_args()
    team_name = args.team
    wait_time = args.refreshrate
    goal_horn = goal_horn_selector.get_goal_horn_file(team_name) # Gets goal horn file

    print("Starting nhl_goal_tracker...\n")
    while True:
        print("Fetching at {}".format(str(dt.now()).split(".")[0]), end=" ") # Print time of fetch)
        nhl_api_handler.fetch_update(team_name)
        time.sleep(wait_time)

if __name__ == '__main__':
    nhl_goal_tracker()
