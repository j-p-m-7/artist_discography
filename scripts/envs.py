import os
from dotenv import load_dotenv

import spotipy 
from spotipy.oauth2 import SpotifyOAuth

# Loads environment variables
load_dotenv()

# Reads the .env file and returns a dictionary of the environment variables
def read_env_file():
    env_vars = {}
    if os.path.exists('.env'):
        with open('.env', 'r') as env_file:
            lines = env_file.readlines()
            for line in lines:
                key, value = line.strip().split('=', 1)
                env_vars[key] = value
    return env_vars

# Sets up the API keys for Spotify and Setlist
def setup_api_keys():
    print("Setting up API keys for Spotify and Setlist.")

    env_vars = read_env_file()

    spotify_client_id = input(f"Enter your Spotify Client ID [{env_vars.get('SPOTIFY_CLIENT_ID', '')}]: ") or env_vars.get('SPOTIFY_CLIENT_ID', '')
    spotify_client_secret = input(f"Enter your Spotify Client Secret [{env_vars.get('SPOTIFY_CLIENT_SECRET', '')}]: ") or env_vars.get('SPOTIFY_CLIENT_SECRET', '')
    spotify_redirect_uri = input(f"Enter your Spotify Redirect URI [{env_vars.get('SPOTIFY_REDIRECT_URI', '')}]: ") or env_vars.get('SPOTIFY_REDIRECT_URI', '')
    setlist_api_key = input(f"Enter your Setlist API Key [{env_vars.get('SETLIST_API_KEY', '')}]: ") or env_vars.get('SETLIST_API_KEY', '')

    # No indentation for env_content to avoid unwanted spaces in the file
    env_content = (
        f"SPOTIFY_CLIENT_ID={spotify_client_id}\n"
        f"SPOTIFY_CLIENT_SECRET={spotify_client_secret}\n"
        f"SPOTIFY_REDIRECT_URI={spotify_redirect_uri}\n"
        f"SETLIST_API_KEY={setlist_api_key}"
    )

    with open('.env', 'w') as env_file:
        env_file.write(env_content)

    print(".env file created successfully with your API keys!")

# Creates the Spotipy object instance
def load_and_initialize_spotify():
    load_dotenv()

    # Gets Spotify credentials from .env
    CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
    CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
    SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')

    # Sets user scopes
    scope = 'user-read-currently-playing user-read-private user-read-email playlist-read-private playlist-modify-public playlist-modify-private'

    # Initializes an instance of the Spotify class as an object
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URI,
                                                   scope=scope))
    return sp


if __name__ == '__main__':
    setup_api_keys()
    sp = load_and_initialize_spotify()
    print(sp.current_user())