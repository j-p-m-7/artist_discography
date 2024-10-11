import os
import json
from pathlib import Path


def load_json(file_path):
    """Helper function to load a JSON file."""
    print(f"Loading JSON file: {file_path}")
    with open(file_path, 'r') as f:
        return json.load(f)

def get_album_ids_and_names(albums_json):
    """Extract album_ids and album names from the JSON data."""
    albums_info = [(album['id'], album['name']) for album in albums_json['data']]
    return albums_info

def get_tracks_from_album(sp, album_id):
    """Fetch all tracks from an album using the album_id."""
    album_tracks = sp.album_tracks(album_id)
    return album_tracks['items']

def process_albums_and_singles(sp):
    """Main process to extract album_ids, fetch tracks, and save to final JSON."""

    # Load the albums and singles JSONs
    albums_json = load_json('data/albums/artist_albums.json')
    singles_json = load_json('data/albums/artist_singles.json')

    # Extract album_ids and names from both albums and singles
    albums_info = get_album_ids_and_names(albums_json)
    singles_info = get_album_ids_and_names(singles_json)

    # Combine album info from albums and singles
    all_albums_info = albums_info + singles_info

    # Initialize final JSON to hold all track data
    final_json = {"tracks": []}

    # Loop through each album and fetch all tracks
    for album_id, album_name in all_albums_info:
        print(f"Processing tracks for album: {album_name} (ID: {album_id})")
        album_tracks = get_tracks_from_album(sp, album_id)
        final_json["tracks"].extend(album_tracks)
        print(f"Total tracks processed: {len(album_tracks)}")

    # Save the final tracks JSON to file
    tracks_json = json.dumps(final_json, indent=4)
    with open(f'data/tracks/artist_tracks.json', 'w') as f:
        f.write(tracks_json)

    print("All tracks processed and saved.\n\n\n")

def process_features(sp, artist_id):
    """Main process to extract feature_ids, fetch tracks, and save to final JSON."""
    # Load the features JSON
    features_json = load_json('data/albums/artist_features.json')

    # Filter items where type is 'album' or 'single'
    filtered_data = [item for item in features_json['data'] if item['album_type'] in ['album', 'single']]

    # convert to json with key "data"
    filtered_data = {"data": filtered_data}

    # Extract feature_ids from features
    feature_ids = get_album_ids_and_names(filtered_data)
    
    # Initialize final JSON to hold all track data
    final_json = {"tracks": []}

    # Loop through each album and fetch all tracks
    for feature_id, feature_name in feature_ids:
        print(f"Processing tracks for feature: {feature_name} (ID: {feature_id})")
        data = get_tracks_from_album(sp, feature_id)
        
        # Load to json object with key "tracks"
        data = {"tracks": data}

        feature_tracks = [track for track in data['tracks'] if any(artist['id'] == artist_id for artist in track['artists'])]
        final_json["tracks"].extend(feature_tracks)

        print(f"Total tracks processed: {len(feature_tracks)}")

    # Save the final tracks JSON to file
    tracks_json = json.dumps(final_json, indent=4)
    with open(f'data/tracks/artist_tracks_features.json', 'w') as f:
        f.write(tracks_json)

    print("All feature tracks processed and saved.\n\n\n")


if __name__ == '__main__':
    pass
