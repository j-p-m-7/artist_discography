import os
import json


def get_artist_id(sp):
    artist = os.getenv('ARTIST')
    artist_json = sp.search(q=artist, type='artist')
    artist_id = artist_json['artists']['items'][0]['id']

    print("\nArtist ID for artist", artist, "is", artist_id, "\n")

    return artist_id

def get_artist_albums(sp, artist_id):
    final_json = {"data": []}
    
    counter = 0
    offset = 0

    while True:
        # Fetch albums using the same method but filtering for 'album' type
        artist_albums = sp.artist_albums(artist_id, include_groups='album', limit=50, offset=offset)
        if artist_albums['items'] == []:
            break

        print(f"Processing", len(artist_albums['items']), "albums...")

        # Extend the final_json data with the albums fetched
        final_json["data"].extend(artist_albums["items"])

        counter += len(artist_albums['items'])
        offset += len(artist_albums['items'])

        # Optional break condition (e.g., if you want to limit the number of albums fetched)
        if counter > 100:
            break

    # Save the final JSON with all albums to a single file
    artist_albums_json = json.dumps(final_json, indent=4)
    with open(f'data/albums/artist_albums.json', 'w') as f:
        f.write(artist_albums_json)

    print("All albums acquired")
    print("Total albums acquired:", counter, "\n")
    
def get_artist_singles(sp, artist_id):
    final_json = {"data": []}

    counter = 0
    offset = 0

    while True:
        # Fetch the artist singles using the same method as features
        artist_singles = sp.artist_albums(artist_id, include_groups='single', limit=50, offset=offset)
        if artist_singles['items'] == []:
            break

        print(f"Processing", len(artist_singles['items']), "singles...")

        # Extend the final_json data with the singles fetched
        final_json["data"].extend(artist_singles["items"])

        counter += len(artist_singles['items'])
        offset += len(artist_singles['items'])

    # Save the final JSON with all singles to a file
    artist_singles_json = json.dumps(final_json, indent=4)
    with open(f'data/albums/artist_singles.json', 'w') as f:
        f.write(artist_singles_json)

    print("All singles acquired")
    print("Total singles acquired:", counter, "\n")

def get_artist_features(sp, artist_id):
    final_json = {"data": []}

    counter = 0
    offset = 0

    while True:
        artist_features = sp.artist_albums(artist_id, include_groups='appears_on', limit=50, offset=offset)
        if artist_features['items'] == []:
            break

        print("Processing", len(artist_features['items']), "features...")
        final_json["data"].extend(artist_features["items"])

        counter += len(artist_features['items'])
        offset += len(artist_features['items'])

    # save json to file
    artist_features_json = json.dumps(final_json, indent=4)
    with open(f'data/albums/artist_features.json', 'w') as f:
        f.write(artist_features_json)

    print("All features acquired")
    print("Total features acquired:", counter, "\n")


if __name__ == '__main__':
    pass
