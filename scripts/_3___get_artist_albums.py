import os
import json

def get_album_tracks(sp):
    # read all album ids from albums/album_dict.json
    album_dict = {}
    with open('albums/album_dict.json', 'r') as f:
        album_dict = json.load(f)

    # for each album, get all track uris and save to list
    # allow for print statement that shows what album name we processed (the key of the dictionary)
    track_uris = []
    for index, album_id in enumerate(album_dict.values()):
        album_tracks = sp.album_tracks(album_id)
        print(f'Processing album {index + 1}/{len(album_dict)}: {list(album_dict.keys())[index]}')
        for track in album_tracks['items']:
            track_uris.append(track['uri'])
    
    # save track uris to .txt file
    with open('track_uris/track_uris.txt', 'w') as f:
        for track_uri in track_uris:
            f.write(f'{track_uri}\n')


# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    pass

    # Sets up API keys
    # TODO - update this function to be more dynamic
    # check if .env file exists
    # if it doesn't exist, run the setup_api_keys() function
    # if not os.path.exists('.env'):
    #     setup_api_keys()
    
    # Initializes the SpotiPy Object
    # sp = load_and_initialize_spotify()

    # # read all album ids from albums/album_dict.json
    # album_dict = {}
    # with open('albums/album_dict.json', 'r') as f:
    #     album_dict = json.load(f)

    # # for each album, get all track uris and save to list
    # # allow for print statement that shows what album name we processed (the key of the dictionary)
    # track_uris = []
    # for index, album_id in enumerate(album_dict.values()):
    #     album_tracks = sp.album_tracks(album_id)
    #     print(f'Processing album {index + 1}/{len(album_dict)}: {list(album_dict.keys())[index]}')
    #     for track in album_tracks['items']:
    #         track_uris.append(track['uri'])
    
    # # save track uris to .txt file
    # with open('track_uris/track_uris.txt', 'w') as f:
    #     for track_uri in track_uris:
    #         f.write(f'{track_uri}\n')