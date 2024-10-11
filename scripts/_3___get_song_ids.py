import os
import json

# open data/tracks/ and for all files with .json extension, load the json file, extract uri from each track
# and write the uri to a .txt file

def get_track_uris():
    # get all files in data/tracks/
    files = os.listdir('data/tracks/')
    # filter files to only include .json files
    files = [file for file in files if file.endswith('.json')]

    # for each file, load the json, extract the uri from each track, and write the uri to a .txt file
    track_uris = []
    for file in files:
        with open(f'data/tracks/{file}', 'r') as f:
            data = json.load(f)
            for track in data['tracks']:
                track_uris.append(track['uri'])

    # write all track uris to a .txt file
    with open('data/uris/track_uris.txt', 'w') as f:
        for track_uri in track_uris:
            f.write(f'{track_uri}\n')

    print("\nProcessed all song IDs\n")

if __name__ == '__main__':
    pass
