'''
Basic json data manipulation example.
This snippet shows how to read and write json data.
- The json data is stored in a file files/teams.json.
- The json data is read and stored in a dictionary.
- Main function is called to read the dictionary for a flag set to True.
    - Print the team name and the team members.
    - Set the flag to False for the team.
    - Set the flag to True for the next team in the dictionary.
- Write the dictionary back to the json file.
'''

import json
import os

PATENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_DIR = os.path.dirname(PATENT_DIR) + '/files/'

def check_flagged(data: list) -> tuple:
    '''Check the dictionary for a flag set to True.
    Return the team name and the team id.'''
    for team_id, team in enumerate(data):
        if team['flag']:
            print(f'Team on duty: {team["name"]}')
            print(f'Team members: {team["rooms"]}')
            team['flag'] = False
            return team['name'], team_id
    print('No team on duty found.')
    return None, -1


if __name__ == '__main__':
    # Read the json data from the file.
    with open(FILE_DIR + 'teams.json') as file_object:
        data = json.load(file_object)

    # Call the function to check the dictionary for a flag set to True.
    team_on_duty, team_on_duty_id = check_flagged(data['teams'])
    
    # Set the flag for the next team to True.
    data['teams'][team_on_duty_id + 1]['flag'] = True

    # Write the dictionary back to the json file.
    with open(FILE_DIR + 'teams.json', 'w') as file_object:
        json.dump(data, file_object, indent=2, ensure_ascii=False)
