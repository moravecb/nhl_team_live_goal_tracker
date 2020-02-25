# nhl_team_live_goal_tracker
- This tool actively fetches from a public API (https://github.com/peruukki/nhl-score-api/blob/master/README.md) for updates on your team's goal and triggers the team's goal horn and lights flashing the team's 2 primary colors in the event of a goal/win. 
- When the game ends, the updated record and points from a playoffs spot are displayed for your team. 
- If you search for your team and they have already played, the win/loss status of your team will be displayed alongside your team's updated record and points from a playoffs spot.

## Parameters:
- **-t (--team)**: Your team's abbreviation (e.g. NSH)
- **-r (--refreshrate)**: The time (in seconds) to wait before refreshing/sending a new API request (e.g. 2)
- **-d (--detailed)**: Provides detailed information about the game with each goal scored.

## Files:
- **detailed_nhl_api_handler.py**: Parses and processes the basic data and additional details returned from the API (e.g. who scored the goal, what goal of the season was it for them).
- **goal_horn_selector.py**: Returns the .mp3 for the specified team's goalhorn song.
- **goal_horn_test.py**: Tests the functionality of the goalhorn and the lights for the specified team.
- **lights_api_handler.py**: Interacts with LIFX API to trigger lights.
- **nhl_api_handler.py**: Parses and processes the data returned from the API.
- **nhl_goal_tracker.py**: Main script used for full functionality (triggering goal horn and lights during live games).
- **team_color_selector.py**: Returns the 2 primary colors of the specified team.

## Goal Horn Songs Disclaimer:
- I do not own the rights to any goal horns uploaded to this repo. All rights are reserved by the respective owner.
- Note: *"Copyright Disclaimer Under Section 107 of the Copyright Act 1976, allowance is made for "fair use" for purposes such as criticism, comment, news reporting, teaching, scholarship, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, educational or personal use tips the balance in favor of fair use."*
