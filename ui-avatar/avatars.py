import requests
from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
img_output_path = script_parent / 'img'
name_file_path = script_parent / 'names.txt'

# Create the 'img' directory if it doesn't exist
img_output_path.mkdir(parents=True, exist_ok=True)

# Define the API URL
api_url = "https://ui-avatars.com/api/"

# Function to generate avatars for a given name
def generate_avatar(name):
    # Replace spaces in the name with '+'
    name = name.replace(" ", "+")
    
    # Construct the full API URL
    avatar_url = f"{api_url}?background=random&name={name}"
    
    try:
        # Send a GET request to the API with SSL verification enabled
        response = requests.get(avatar_url, verify=True)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to generate avatar for {name}")
            return None
    except requests.exceptions.SSLError as e:
        print(f"SSL Error: {e}")
        return None

# Function to prompt the user and proceed or not on SSL error
def handle_ssl_error(name):
    user_input = input("SSL certificate verification failed. Do you want to proceed anyway? (y/n): ").strip().lower()
    if user_input == 'y':
        try:
            # Send a GET request to the API with SSL verification disabled
            return generate_avatar(name)
        except requests.exceptions.SSLError as e:
            print(f"SSL Error: {e}")
            return None
    else:
        return None

# Read names from the text file
with open(name_file_path, "r") as file:
    names = file.readlines()

# Generate avatars for each name and save them as image files
for name in names:
    name = name.strip()  # Remove leading/trailing whitespace
    avatar = generate_avatar(name) if generate_avatar(name) else handle_ssl_error(name)
    
    if avatar:
        # Save the avatar as an image file with the name
        with open(img_output_path / f"{name}.png", "wb") as img_file:
            img_file.write(avatar)
            print(f"Avatar generated for {name}")

print("Avatar generation complete.")
