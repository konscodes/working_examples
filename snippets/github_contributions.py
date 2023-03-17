import requests

# Set the username of the user whose contributions calendar you want to see
username = "konscodes"

# Set the API endpoint URL
url = f"https://api.github.com/users/{username}/events"

# Make the API request
response = requests.get(url)

# Check the status code of the response
if response.status_code != 200:
    print("Failed to retrieve data")
else:
    # Get the data
    data = response.json()

    # Create a dictionary to store the contribution counts by date
    contributions = {}

    # Iterate through the events
    for event in data:
        # Check if the event is a PushEvent (indicating a contribution)
        if event["type"] == "PushEvent":
            # Get the date of the event
            date = event["created_at"][:10]  # Get only the date, not the time
            # Increment the contribution count for the date
            if date in contributions:
                contributions[date] += 1
            else:
                contributions[date] = 1

    # Print the contributions calendar
    for date, count in contributions.items():
        print(f"{date}: {count} contributions")
