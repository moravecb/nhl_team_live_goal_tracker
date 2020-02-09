'''
Title: nhl_goal_tracker.py
Author: Peyton Ball
Creation Date: 02/08/2020
Last Modified: 02/08/2020
Purpose: Main file to execute to track goals of your team and alert when
         they score.
'''
# Import statements
import sys
import time
from datetime import datetime as dt
import os
import argparse
import nhl_api_handler

def nhl_goal_tracker():
    global goal_horn
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team', type=str, help="Enter team abbreviation.", default="NSH")
    parser.add_argument('-r', '--refreshrate', type=int, help="Enter the time to wait before refreshing.", default=2)
    args = parser.parse_args()
    team_name = args.team
    wait_time = args.refreshrate

    print("Starting nhl_goal_tracker...\n")
    nhl_api_handler.get_goal_horn(team_name) # Gets and sets goal horn for team specified
    while True:
        print("Fetching at {}".format(str(dt.now()).split(".")[0]), end=" ") # Print time of fetch)
        nhl_api_handler.fetch_update(team_name)
        time.sleep(wait_time)

if __name__ == '__main__':
    nhl_goal_tracker()
