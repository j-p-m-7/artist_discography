import os
import shutil

from scripts.envs import *

from scripts._1___get_artist_music import *
from scripts._2___process_artist_albums import *
from scripts._3___get_song_ids import *
from scripts._4___add_tracks_to_playlist import *
from scripts._5___ascii import *


# Sets artist name as an environment variable
def set_artist_name_as_env_var():
        # Take input from the user
        artist_name = input("Enter the artist's name: ")

        # Convert the artist name to title case (capitalize each word)
        artist_name_title = artist_name.title()

        # Set it as an environment variable
        os.environ['ARTIST'] = artist_name_title

        # Print the environment variable to verify it's set
        print(f"Environment variable set: ARTIST={os.environ['ARTIST']}")

def clear_data_folders():
    """Clears the contents of the data/albums, data/tracks, and data/uris directories."""
    directories = ['data/albums', 'data/tracks', 'data/uris']

    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)  # Remove the entire directory
            os.makedirs(directory)    # Recreate the directory as empty
            print(f"Cleared: {directory}")

# Makes parts of the code easier to read
def prints(name, obj=None):
    if not obj:
        print()
        print('-'*50, name, '-'*50)
    else:
        print('-'*50 + '-'*(len(name)+2) + '-'*50)
        print()

# Main Function
def main():
     # Sets up API keys
    if not os.path.exists('.env'):
        setup_api_keys()
    

    set_artist_name_as_env_var()

    # Initializes the SpotiPy Object
    sp = load_and_initialize_spotify()

    print('\nStarting the process to collect all tracks for', os.getenv('ARTIST') + '...')



    prints("Step 1")
    artist_id = get_artist_id(sp)
    get_artist_albums(sp, artist_id)
    get_artist_singles(sp, artist_id)
    get_artist_features(sp, artist_id)
    prints("Step 1", '-')


    prints("Step 2")
    process_albums_and_singles(sp)
    process_features(sp, artist_id)
    prints("Step 2", '-')


    prints("Step 3")
    get_track_uris()
    prints("Step 3", '-')


    prints("Step 4")
    add_tracks_to_playlist(sp)
    clear_data_folders()
    prints("Step 4", '-')


    prints("Step 5")
    asciiify()
    prints("Step 5", '-')

    

if __name__ == '__main__':
    main()
    