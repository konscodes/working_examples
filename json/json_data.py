'''
Basic json data manipulation example.
This snippet shows how to read and write json data.
- The json data is stored in a file files/teams.json.
- The json data is read and stored in a dictionary.
- Function is called to search the dictionary for a specific duty.
    - Print the team name and the team members.
    - Remove the duty for the team.
    - Add the duty for the next team in the dictionary.
- Write the dictionary back to the json file.
'''

import json
import os

def who_on_duty(teams: list, specific_duty) -> tuple:
    '''Check who is on duty and return the team name and team id.'''
    for team_id, team in enumerate(teams):
        if specific_duty in team['duty']:
            print(f"Team {team['name']} is on {specific_duty} duty.")
            print(f"Members: {[x['person']['english'] for x in team['rooms']]}")
            return team['name'], team_id 
    print(f"{specific_duty} duty is not found.")
    return None, -1


if __name__ == '__main__':
    PATENT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_DIR = os.path.dirname(PATENT_DIR) + '/files/'

    # Read the json data from the file.
    with open(FILE_DIR + 'teams.json') as file_object:
        data = json.load(file_object)

    # Call the function to check the dictionary for a "Garbage" duty.
    team_on_duty, team_on_duty_id = who_on_duty(data['teams'], "Garbage")
    
    # Set the "Garbage" duty for the next team.
    data['teams'][team_on_duty_id]['duty'].remove("Garbage")
    if team_on_duty_id < len(data['teams']) - 1:
        data['teams'][team_on_duty_id + 1]['duty'].append("Garbage")
    else:
        data['teams'][0]['duty'].append("Garbage")

    # Write the dictionary back to the json file.
    with open(FILE_DIR + 'teams.json', 'w') as file_object:
        json.dump(data, file_object, indent=2, ensure_ascii=False)
