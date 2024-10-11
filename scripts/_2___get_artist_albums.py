import os
import json
from pathlib import Path

def get_album_ids():
    # read all album ids from all jsons in jsons folder in order of creation
    path = 'jsons'
    files = sorted(os.listdir(path), key=lambda file: os.path.getctime(os.path.join(path, file)))
    
    # add album names and ids to dictionary
    album_dict = {}
    for file in files:
        if file.endswith('.json'):
            with open(f'jsons/{file}', 'r') as f:
                album_json = json.load(f)
                for album in album_json['items']:
                    album_dict[album['name']] = album['id']

    # clear jsons folder
    # for file in files:
    #     os.remove(f'jsons/{file}')

    # save album names and ids to .json file
    with open('albums/album_dict.json', 'w') as f:
        json.dump(album_dict, f, indent=4)

    print("Acquired each albums Spotify id")

# Main Function
# Filter this function to only run the functions you want to test
# IE if you only want to run the Setlist API functions, comment out the Spotify API functions using the '#' symbol
if __name__ == '__main__':
    pass

    # Sets up API keys

    #if not os.path.exists('.env'):
    #    setup_api_keys()
    
    # Initializes the SpotiPy Object
    # sp = load_and_initialize_spotify()

    # path = 'jsons'
    # files = sorted(os.listdir(path), key=lambda file: os.path.getctime(os.path.join(path, file)))
    
    # # add album names and ids to dictionary
    # album_dict = {}
    # for file in files:
    #     if file.endswith('.json'):
    #         with open(f'jsons/{file}', 'r') as f:
    #             album_json = json.load(f)
    #             for album in album_json['items']:
    #                 album_dict[album['name']] = album['id']

    # # save album names and ids to .json file
    # with open('albums/album_dict.json', 'w') as f:
    #     json.dump(album_dict, f, indent=4)