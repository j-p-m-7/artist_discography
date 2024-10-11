import os
import json
from pathlib import Path


## - Add a function to clear the jsons folder
## TODO 
#     # clear jsons folder
#     # for file in files:
#     #     os.remove(f'data/{file}')
## TODO 




def load_json(file_path):
    """Helper function to load a JSON file."""
    print(f"Loading JSON file: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def get_album_ids(albums_json):
    """Extract album_ids from the JSON data."""
    print("Extracting album_ids from JSON data...")
    album_ids = [album['id'] for album in albums_json['data']]
    return album_ids

def get_tracks_from_album(sp, album_id):
    """Fetch all tracks from an album using the album_id."""
    print(f"Fetching tracks for album_id: {album_id}")
    album_tracks = sp.album_tracks(album_id)
    return album_tracks['items']

def process_albums_and_singles(sp):
    """Main process to extract album_ids, fetch tracks, and save to final JSON."""
    print("Processing albums and singles...")
    # Load the albums and singles JSONs
    albums_json = load_json('data/albums/artist_albums.json')
    singles_json = load_json('data/albums/artist_singles.json')

    # Extract album_ids from both albums and singles
    album_ids = get_album_ids(albums_json)
    single_ids = get_album_ids(singles_json)
    
    # Combine album_ids and single_ids
    all_album_ids = album_ids + single_ids
    
    # Initialize final JSON to hold all track data
    final_json = {"tracks": []}

    # Loop through each album_id and fetch all tracks
    for album_id in all_album_ids:
        print(f"Processing tracks for album_id: {album_id}")
        album_tracks = get_tracks_from_album(sp, album_id)
        final_json["tracks"].extend(album_tracks)

    # Save the final tracks JSON to file
    tracks_json = json.dumps(final_json, indent=4)
    with open(f'data/tracks/artist_tracks.json', 'w') as f:
        f.write(tracks_json)

    print("All tracks processed and saved.")

def process_features(sp, artist_id):
    """Main process to extract feature_ids, fetch tracks, and save to final JSON."""
    # Load the features JSON
    features_json = load_json('data/albums/artist_features.json')

    # Filter items where type is 'album' or 'single'
    filtered_data = [item for item in features_json['data'] if item['album_type'] in ['album', 'single']]

    # convert to json with key "data"
    filtered_data = {"data": filtered_data}

    # Extract feature_ids from features
    feature_ids = get_album_ids(filtered_data)
    
    # Initialize final JSON to hold all track data
    final_json = {"tracks": []}

    # Loop through each feature_id and fetch all tracks containing the artist
    for feature_id in feature_ids:
        print(f"Processing tracks for feature_id: {feature_id}")
        data = get_tracks_from_album(sp, feature_id)
        
        # Load to json object with key "tracks"
        data = {"tracks": data}

        artist_tracks = [track for track in data['tracks'] if any(artist['id'] == artist_id for artist in track['artists'])]
        final_json["tracks"].extend(artist_tracks)

    # Save the final tracks JSON to file
    tracks_json = json.dumps(final_json, indent=4)
    with open(f'data/tracks/artist_tracks_features.json', 'w') as f:
        f.write(tracks_json)

    print("All feature tracks processed and saved.")

# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    from envs import *

    # Sets up API keys
    if not os.path.exists('.env'):
       setup_api_keys()
    
    # Initializes the SpotiPy Object
    sp = load_and_initialize_spotify()
    artist_id = '5K4W6rqBFWDnAN6FQUkS6x'
    
    #process_albums_and_singles(sp)
    process_features(sp, artist_id)
